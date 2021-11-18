from dotenv import find_dotenv, load_dotenv
import os
import jwt
import datetime

def hash(s):
    load_dotenv(find_dotenv('.gitignore/security.env'))
    prime_number = int(os.getenv('NUMBER'))
    num = 0
    step = 1
    for i in range(len(s)):
        num += ord(s[i]) * step
        step *= prime_number
    return num


def JWT_encode(s, to_file=''):
    load_dotenv(find_dotenv('.gitignore/security.env'))
    keyword = os.getenv('KEYWORD')
    encoded = jwt.encode(s, keyword, algorithm="HS256")

    return encoded


def JWT_decode(s):
    load_dotenv(find_dotenv('.gitignore/security.env'))
    keyword = os.getenv('KEYWORD')
    try:
        return jwt.decode(s, keyword, algorithms="HS256")
    except:
        raise ValueError('токен не валідний')

