import requests
from hashlib import sha256
from base64 import b64decode, standard_b64encode
from binascii import unhexlify, b2a_base64
import hmac

class ScramAdapter:

    def __init__(self, username, password, host_url) -> None:
        self.username = username
        self.password = password
        self.host = host_url

    
    def __handshake(self):
        
        # create client hello message
        encoded_username = base64_no_padding(self.username)
        client_hello_message = c.HELLO_STRING % (encoded_username)
        # send handshake request
        hello_msg_response = requests.get(self.host, headers={'Authorization': client_hello_message},verify=False) 
        # parse response handshake token and encoding algo
        status_code =  hello_msg_response.status_code
        if status_code!=401:
            raise Exception("Invalid response received while handshake authentication")
        else:
            server_response = hello_msg_response.headers[c.HEADER_AUTH_PARAMETER]
            header_response = server_response.split(",")
            algorithm = regex_after_equal(header_response[1])
            algorithm_name = algorithm.replace("-", "").lower()
            if algorithm_name == "sha256":
                self.__algorithm = sha256
                self.__algorithm_name = "sha256"
            else:
                raise Exception("SHA not implemented")

            self.__handshake_token = regex_after_equal(header_response[0])


    def __first_message(self):

        nonce = get_nonce()
        self.__client_first_msg = "n=%s,r=%s" % (self.username, nonce)
        client_first_msg_encoded = base64_no_padding(self.__client_first_msg)
        auth_message = c.CLIENT_FIRST_MESSAGE % (self.__handshake_token,client_first_msg_encoded)
        first_msg_response = requests.get(self.host, headers={'Authorization': auth_message},verify=False)
        status_code =  first_msg_response.status_code
        if status_code!=401:
            raise Exception("Invalid response received while first message authentication")
        else:
            header_response = first_msg_response.headers[c.HEADER_AUTH_PARAMETER]
            tab_header = header_response.split(",")
            server_data = regex_after_equal(tab_header[0])
            missing_padding = len(server_data) % 4
            if missing_padding != 0:
                server_data += "=" * (4 - missing_padding)

            server_data = b64decode(server_data).decode()
            tab_response = server_data.split(",")
            self.__server_first_msg = server_data
            self.__server_nonce = regex_after_equal(tab_response[0])
            self.__server_salt = regex_after_equal(tab_response[1])
            self.__server_iterations = regex_after_equal(tab_response[2])

    def __second_message(self):

        client_final_no_proof = "c=%s,r=%s" % (standard_b64encode(b"n,,").decode(),self.__server_nonce)
        auth_msg = "%s,%s,%s" % (self.__client_first_msg,self.__server_first_msg,client_final_no_proof)
        client_key = hmac.new(
            unhexlify(
                salted_password(self.__server_salt, self.__server_iterations, self.__algorithm_name, self.password)
            ),
            "Client Key".encode("UTF-8"),
            self.__algorithm,
        ).hexdigest()

        stored_key = hash_sha256(unhexlify(client_key), self.__algorithm)
        client_signature = hmac.new(
            unhexlify(stored_key), auth_msg.encode("utf-8"), self.__algorithm
        ).hexdigest()
        client_proof = xor(client_key, client_signature)
        client_proof_encode = b2a_base64(unhexlify(client_proof)).decode()
        client_final = client_final_no_proof + ",p=" + client_proof_encode
        client_final_base64 = base64_no_padding(client_final)

        final_msg = c.CLIENT_SECOND_MESSAGE % (self.__handshake_token,client_final_base64)

        self.second_msg_response = requests.get(self.host, headers={'Authorization': final_msg},verify=False)


    def __validate(self):

        server_response = self.second_msg_response.headers[c.HEADER_AUTH_INFO]
        tab_response = server_response.split(",")
        auth_token = regex_after_equal(tab_response[0])
        auth = c.AUTH_TOKEN_STRING % auth_token
        return auth


    def fetch_auth_token(self):

        try:
            self.__handshake() 
            self.__first_message()
            self.__second_message()
            auth_token = self.__validate()
            return auth_token

        except Exception as e:
            print("Error occured while fetching auth token using Scram")
            raise e
    