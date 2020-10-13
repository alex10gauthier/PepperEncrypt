from EncryptedData import EncryptedData
from User import User
from UserData import UserData
from Encrypter import Encrypter


class Decrypter:

    def __init__(self, encrypted_data):
        self.encrypted_data = encrypted_data

    def decrypt(self):
        result = ''
        encrypted_message = self.encrypted_data.data
        j = 0

        for i in range(0, len(encrypted_message)):
            if j < len(self.encrypted_data.get_key()) - 1:
                j += 1
            else:
                j = 1

            c = encrypted_message[i]
            if ord(c) - 3 - ord(self.encrypted_data.get_key()[j]) >= 0:
                result += chr(ord(c) - 3 - ord(self.encrypted_data.get_key()[j]))
            else:
                result += chr(ord(c) - 3)
        return result


def main():
    user = User('alex10gauthier', 'password99')
    user_data = UserData('My name is Alex Gauthier', user)

    encrypter = Encrypter(user_data)
    encrypted_string = encrypter.encrypt()
    key = encrypter.get_key()
    encrypted_data = EncryptedData(encrypted_string, user, key)
    decrypter = Decrypter(encrypted_data)
    print(decrypter.decrypt())


if __name__ == '__main__':
    main()
