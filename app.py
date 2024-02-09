import random as r
import string as s

def gen_password():
    ul = s.ascii_uppercase
    ll = s.ascii_lowercase
    punctuation = s.punctuation
    
    first_letter = ''.join(r.sample(ul, 4))
    second_letter = ''.join(r.sample(ll, 4))
    
    comma = ''.join(r.sample(punctuation, 4))
    all_value = first_letter + second_letter + comma
    password = list(all_value)
    r.shuffle(password)
    
    shuffled_password = ''.join(password)
    return shuffled_password
    
def user():
    password = gen_password()  
    name = input("Your name:" )
    print(f"{name} this is your password '{password}'")
    
user()
