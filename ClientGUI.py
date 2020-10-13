# This is the main client driver that runs the program in graphical user interface format.
# Still some inconsistencies to clean up.
from Tkinter import *
from FileReader import FileReader
from User import User
from UserData import UserData
from Encrypter import Encrypter
from EncryptedData import EncryptedData
from Decrypter import Decrypter


class ClientGUI:

    def __init__(self, on):
        self.on = on
        self.encrypt_choice = False
        self.decrypt_choice = True
        self.root = Tk()
        self.file_name = ''
        self.encrypted_data = None
        self.e = None
        self.user1 = User('Alex10Gauthier', 'algau')

        if self.on:
            self.entry = Entry(self.root, justify=LEFT)
            self.entry.pack()
            self.root.title('Pepper Encrypt')
            self.root.geometry('500x400')
            self.root.configure(bg='wheat2')

            e = IntVar()
            d = IntVar()

            Label(self.root, text='Enter a valid file name then choose an option: ', justify=LEFT, padx=20,
                  bg='wheat2', fg='steel blue').pack()

            Label(self.root, text='Choose an option:', justify=LEFT, padx=20, bg='wheat2', fg='steel blue').pack()

            Label(self.root, text='Top Button - Encrypt your data', justify=LEFT, padx=20, bg='wheat2',
                  fg='steel blue').pack()
            Label(self.root, text='Bottom Button - Decrypt your data', justify=LEFT, padx=20, bg='wheat2',
                  fg='steel blue').pack()
            Label(self.root, text='Press the white button to start the program', justify=LEFT,
                  padx=20, bg='wheat2', fg='steel blue').pack()

            Button(self.root, text='ENTER', padx=20, bg='wheat2', command=self.perform_encrypt).pack()

            Button(self.root, text='DECRYPT', padx=20, bg='wheat2', command=self.perform_decrypt).pack()

            self.root.mainloop()

    def perform_encrypt(self):
        self.file_name = self.entry.get()
        reader = FileReader(self.file_name)
        string_info = reader.read_file()
        user_data = UserData(string_info, self.user1)
        self.e = Encrypter(user_data)
        key = self.e.get_key()
        self.encrypted_data = EncryptedData(self.e.encrypt(), self.user1, key)
        reader.write_to_file(self.encrypted_data.get_data())

    def perform_decrypt(self):
        reader = FileReader(self.file_name)
        encrypted_data = EncryptedData(reader.read_file(), self.user1, self.e.get_key())
        decrypter = Decrypter(encrypted_data)
        reader.write_to_file(decrypter.decrypt())


def main():
    ClientGUI(True)
    

if __name__ == '__main__':
    main()
