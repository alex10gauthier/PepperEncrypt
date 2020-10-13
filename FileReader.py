# This class reads from a file and returns the information in it as a string


class FileReader:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        f = open(self.file_name, 'r')
        file_string = ''
        for x in f:
            file_string += x
        f.close()
        return file_string

    def write_to_file(self, encrypted_data):
        f = open(self.file_name, 'w')
        f.write(encrypted_data)
        f.close()


def main():
    reader = FileReader('testing.txt')
    print(reader.read_file())


if __name__ == '__main__':
    main()