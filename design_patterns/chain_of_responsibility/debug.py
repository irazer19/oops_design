from log_processor import LogProcessor


class Debug(LogProcessor):
    def __init__(self, next_log_processor):
        super().__init__(next_log_processor)

    def log(self, log_level, message):
        if log_level == "DEBUG":
            print(f"DEBUG: {message}")
        else:
            super().log(log_level, message)
