import secrets
import string

def generate_token(length):
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(length))
    return token

if __name__ == '__main__':
    for 1, 10:
        token = generate_token(1000)
        print(token)