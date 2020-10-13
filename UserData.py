# Class that represents the data that the user will input on the application.
from InputtedData import InputtedData
from User import User


class UserData(InputtedData):

    def __init__(self, data, user):
        InputtedData.__init__(self, data, user)

    def add_data(self, data):
        self.data = data

    def remove_data(self):
        self.data = None

    def get_data(self):
        return self.data


def main():
    print("What is your name?")
    person_name = raw_input("Insert your user name")
    print("What is your password?")
    person_password = raw_input("What is your password?")

    print("What data do you want to input?")
    user_input = raw_input("Enter your data...")

    print("Making the user data object")
    user1 = User(person_name, person_password)
    user1data = UserData(user_input, user1)
    print("The data is: " + user1data.get_data())
    print("Now removing the data: ")
    user1data.remove_data()
    new_data = raw_input("Add new data:")
    user1data.add_data(new_data)
    print("The new data is: " + user1data.get_data())


if __name__ == "__main__":
    main()
