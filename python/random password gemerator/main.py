import random
import string

def generate_password(length=12):
    if length <= 0:
        raise ValueError("Password length must be greater than zero.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.SystemRandom().choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = 12  
    print("Generated Password:", generate_password(length))
