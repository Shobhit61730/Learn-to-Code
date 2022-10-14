from scram_auth import ScramAdapter

username ='abc@gmail.com'
password = "******"
host_url = "xyz.com/ui"

scram_obj = ScramAdapter(username, password, host_url)
auth_token = scram_obj.fetch_auth_token()
print("Generated Scram auth token ", auth_token)