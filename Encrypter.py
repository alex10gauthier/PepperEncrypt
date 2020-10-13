# This is the class that encrypts the data that the user inputs and makes a key for use in process.
import random
import string
from UserData import UserData
from User import User


class Encrypter:

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.key = ''
        self.encrypt_key = ''
        for i in range(0, 10):
            self.encrypt_key += random.choice(string.ascii_letters)

    def encrypt(self):
        result = ''
        raw_message = self.raw_data.get_data()
        j = 0
        for i in range(0, len(raw_message)):
            if j < len(self.encrypt_key) - 1:
                j += 1
            else:
                j = 1

            c = raw_message[i]
            if ord(c) + 3 + ord(self.encrypt_key[j]) <= 255:
                result += chr(ord(c) + 3 + ord(self.encrypt_key[j]))
            else:
                result += chr(ord(c) + 3)
        return result

    def get_key(self):
        return self.encrypt_key


def main():
    user = User('alex10gauthier', 'password99')
    user_data = UserData('My name is Alex Gauthier', user)

    encrypt = Encrypter(user_data)
    print(encrypt.encrypt())


if __name__ == '__main__':
    main()
