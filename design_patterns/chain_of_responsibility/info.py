from log_processor import LogProcessor


class Info(LogProcessor):
    def __init__(self, next_log_processor):
        super().__init__(next_log_processor)

    def log(self, log_level, message):
        if log_level == "INFO":
            print(f"INFO: {message}")
        else:
            super().log(log_level, message)
