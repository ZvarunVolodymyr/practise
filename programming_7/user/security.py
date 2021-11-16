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
        step *= 29
    return num


def JWT_encode(s, to_file=''):
    load_dotenv(find_dotenv('.gitignore/security.env'))
    keyword = os.getenv('KEYWORD')
    # s["exp"] = (datetime.datetime.now() + datetime.timedelta(days=1)).timestamp()
    encoded = jwt.encode(s, keyword, algorithm="HS256")
    if to_file != '':
        try:
            file = open(to_file, 'w')
            file.write(encoded)
            file.close()
        except:
            raise ValueError('файлу для запису токена не існує')

    return encoded


def JWT_decode(s):
    load_dotenv(find_dotenv('.gitignore/security.env'))
    keyword = os.getenv('KEYWORD')
    try:
        return jwt.decode(s, keyword, algorithms="HS256")
    except:
        raise ValueError('токен не валідний')


def read_token(file_with_token="token.txt"):
    try:
        file = open('token.txt', 'r')
        token = file.read()
        file.close()
    except:
        token = None

    return token


def remove_token(file_with_token="token.txt"):
    try:
        file = open(file_with_token, 'w')
        file.write(' ')
        file.close()
    except:
        pass