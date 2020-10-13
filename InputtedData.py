# This is the skeleton class for user's data that will be inputted on the
# application.


class InputtedData:

    def __init__(self, data, user):
        self.data = data
        self.user = user

    def add_data(self, data):
        self.data = data

    def remove_data(self):
        self.data = ""

    def get_data(self):
        return self.data


def main():
    input_data = InputtedData("Hello World", "Alex Gauthier")
    print(input_data.get_data())
    input_data.remove_data()
    print("Data was removed")


if __name__ == "__main__":
    main()
