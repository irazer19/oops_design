from log_processor import LogProcessor


class Error(LogProcessor):
    def __init__(self, next_log_processor):
        super().__init__(next_log_processor)

    def log(self, log_level, message):
        if log_level == "ERROR":
            print(f"ERROR: {message}")
        else:
            super().log(log_level, message)
