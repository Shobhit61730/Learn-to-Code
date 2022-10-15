# POST API

import random, string

long_url = "https://www.xyz.com/***/2324343/******"
domain = "https://www.xyz.com"

# create hash for given long url
hash_string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
while(alreadyExist(hash_string)):
    hash_string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))

insert_in_db(domain, long_url, hash_string)
short_url = domain +'/'+ hash_string
print(short_url)




# GET API
short_url = 'https://www.xyz.com/uJULXaaBWjkkShTe'

# search key in db
long_url = get_long_url_from_db(short_url)
print(long_url)