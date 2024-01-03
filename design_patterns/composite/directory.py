from file_system import Filesystem


class Directory(Filesystem):
    def __init__(self, name):
        self.name = name
        self.file_system = []

    def ls(self):
        print(f"Directory: {self.name}")
        for file_system in self.file_system:
            file_system.ls()

    def add(self, file_system):
        self.file_system.append(file_system)
