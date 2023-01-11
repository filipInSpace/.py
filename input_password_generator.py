
#Author: Filip Navrkal

import random
import string

#Generates a random password of the specified length   
def generate_password(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == '__main__':
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print(f"Generated password of length {password_length}: {password}")
