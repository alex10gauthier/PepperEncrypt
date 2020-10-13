# This class represents a user of the system


class User:

    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password

    def get_user_name(self):
        return self.user_name

    def get_password(self):
        return self.user_password

    def set_user_name(self, new_name):
        self.user_name = new_name

    def set_user_password(self, new_password):
        self.user_password = new_password
