class LogProcessor:
    def __init__(self, next_log_processor):
        self.next_log_processor = next_log_processor

    def log(self, log_level, message):
        if self.next_log_processor:
            self.next_log_processor.log(log_level, message)
