# This is the skeleton class for the interface that will run the program for the user.

from User import User
from UserData import UserData
from Encrypter import Encrypter
from EncryptedData import EncryptedData
from Decrypter import Decrypter


class Client:

    def __init__(self, online):
        self.online = online

    def start_session(self):

        if self.online:
            print('Hi, this program will ask you to enter the data you want '
                  + 'encrypted and then give it to you encrypted.')

            username = raw_input('Please enter your username: ')
            password = raw_input('Please enter your password: ')
            user = User(username, password)
            inputted_text = raw_input('Please enter the data that you want encrypted: ')

            user_data = UserData(inputted_text, user)

            encrypter = Encrypter(user_data)
            encrypted_string = encrypter.encrypt()
            key = encrypter.get_key()
            encrypted_data = EncryptedData(encrypted_string, user, key)

            print('Your encrypted data is: ' + encrypted_data.get_data())
            print('The key for your encrypted data is: ' + encrypted_data.get_key())

            decrypter = Decrypter(encrypted_data, key)
            print('Here is the decrypted data: ')
            print(decrypter.decrypt())


def main():
    client = Client(True)
    client.start_session()


if __name__ == '__main__':
    main()
