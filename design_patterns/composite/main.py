"""
In composite design pattern, if the object structure follows a tree like structure then we may use composite pattern.
Ex: A file system has either a file or directory inside it. Now a directory can also have files and another directory.
We see that only two possible objects can exist. 1. Leaf node(files), 2. Composed node(directory) again.

We will have a common interface called ls() method in a file_system class. Now whether its a file or a directory, both
are file_system type class because they inherit from file_system and implement ls() method.

We start by first creating a directory, and add either a file or directory inside.

"""


from file import File
from directory import Directory


def run():
    movies = Directory("movies")
    titanic = File("Titanic")
    movies.add(titanic)

    action_movies = Directory("Action Movies")
    avengers = File("Avengers")
    iron_man = File("Iron Man")
    action_movies.add(avengers)
    action_movies.add(iron_man)
    movies.add(action_movies)

    movies.ls()
    pass


if __name__ == "__main__":
    run()
