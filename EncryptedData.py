# Class to represent the data when it is already encrypted. Has methods to get a new key for your data
# and to send to the unencrypter method of the encrypter class.


class EncryptedData:

    def __init__(self, data, user, key):
        self.data = data
        self.user = user
        self.key = key

    def get_data(self):
        return self.data

    def get_user(self):
        return self.user

    def get_key(self):
        return self.key




