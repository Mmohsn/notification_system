from datetime import datetime

class Notification:
    def __init__(self, title: str, message: str, timestamp: datetime = datetime.now(), read_status: bool = False):
        pass

    def mark_as_read(self):
        pass

    def __str__(self):
        pass

