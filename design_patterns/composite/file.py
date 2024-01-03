from file_system import Filesystem


class File(Filesystem):
    def __init__(self, name):
        self.name = name

    def ls(self):
        print(f"Filename: {self.name}")
