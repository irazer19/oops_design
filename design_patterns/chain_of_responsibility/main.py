"""
The chain of responsibility pattern passes the responbility from one object to another.
Ex: If the Info class is not able to handle Debug logs, then it will ask its parent class to handle it, meaning
that it will simply assume that the parent class can handle it.
Every concrete class such as "Info" inherits from a parent class, and passes the next possible handler in the
constructer of the parent.

Here the log_processor is the parent class which calls the next handler which is provided in its constructer.

"""


from info import Info
from debug import Debug
from error import Error


logger = Info(
    next_log_processor=Debug(next_log_processor=Error(next_log_processor=None))
)

logger.log("INFO", "My info message")
logger.log("DEBUG", "My debug message")
logger.log("ERROR", "My error message")
