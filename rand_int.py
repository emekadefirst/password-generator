import random as r
import string as s

def gen_password():

    
    # Generate 2 random integers
    random_integers = ''.join(str(r.randint(0, 9)) for _ in range(2))
    
    return random_integers 

def user():
    password = gen_password()
    name = input("Your name:" )
    print(f"{name} {password}")
    
user()
 