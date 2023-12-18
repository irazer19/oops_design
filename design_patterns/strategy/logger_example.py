"""
Whenever there is a need to choose an object from other similar objects, we need to use strategy design pattern.
We create concrete classes of similar objects, and at runtime we decide which conrete class object will be used.


"""


from abc import ABC, abstractmethod


# Strategy Interface
class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass


# Concrete Strategy 1
class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(f"Logging to console: {message}")


# Concrete Strategy 2
class FileLogger(Logger):
    def log(self, message: str) -> None:
        with open("log.txt", "a") as f:
            f.write(f"Logging to file: {message}\n")


####################################################
####################################################


# Context, we pass the logger instance to this class
class Application:
    def __init__(self, logger: Logger) -> None:
        self._logger = logger

    def set_logger(self, logger: Logger) -> None:
        self._logger = logger

    def execute(self, message: str) -> None:
        self._logger.log(message)


# Client code, deciding console logger usage at the runtime!
app = Application(ConsoleLogger())
app.execute("Hello, World!")  # Logs to console
