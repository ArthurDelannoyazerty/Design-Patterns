from abc import ABC, abstractmethod
from datetime import datetime

# ---------------------------------------------------------------------------- #
#                                Abstract Class                                #
# ---------------------------------------------------------------------------- #
class Subscriber(ABC):
    @abstractmethod
    def update(self, message: str, level: str) -> None:
        pass

# ---------------------------------------------------------------------------- #
#                                Concrete Class                                #
# ---------------------------------------------------------------------------- #
class ConsoleSubscriber(Subscriber):
    def update(self, message: str, level: str) -> None:
        print(f"[CONSOLE] {datetime.now()}: [{level.upper()}] - {message}")


class FileSubscriber(Subscriber):
    def __init__(self, filename: str):
        self.filename = filename

    def update(self, message: str, level: str) -> None:
        # Write your file here
        print(f"[{self.__class__.__name__}] Notified and wrote to {self.filename}")


class LoggerPublisher:
    _observers: list[Subscriber] = []

    def attach(self, observer: Subscriber) -> None:
        if observer not in self._observers:
            print(f"Logger: Attached observer - {observer.__class__.__name__}")
            self._observers.append(observer)

    def detach(self, observer: Subscriber) -> None:
        print(f"Logger: Detached observer - {observer.__class__.__name__}")
        self._observers.remove(observer)

    def _notify(self, message: str, level: str) -> None:
        print("\nLogger: Notifying all attached observers...")
        for observer in self._observers:
            observer.update(message, level)

    def log(self, level: str, message: str) -> None:
        print(f"Logger: New log entry created -> '{message}'")
        self._notify(message, level)

# ---------------------------------------------------------------------------- #
#                                 Main / Client                                #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    logger = LoggerPublisher()

    console_subscriber = ConsoleSubscriber()
    file_subscriber = FileSubscriber("app.log")
    
    logger.attach(console_subscriber)
    logger.attach(file_subscriber)

    logger.log("info", "User successfully logged in.")
    logger.log("warning", "Disk space is running low.")
    
    logger.detach(console_subscriber)
    
    logger.log("error", "Failed to connect to the database.")

# ---------------------------------- Output ---------------------------------- #
# Logger: Attached observer - ConsoleSubscriber
# Logger: Attached observer - FileSubscriber
# Logger: New log entry created -> 'User successfully logged in.'
#
# Logger: Notifying all attached observers...
# [CONSOLE] 2025-07-30 13:48:19.102765: [INFO] - User successfully logged in.
# [FileSubscriber] Notified and wrote to app.log
# Logger: New log entry created -> 'Disk space is running low.'
#
# Logger: Notifying all attached observers...
# [CONSOLE] 2025-07-30 13:48:19.103763: [WARNING] - Disk space is running low.
# [FileSubscriber] Notified and wrote to app.log
# Logger: Detached observer - ConsoleSubscriber
# Logger: New log entry created -> 'Failed to connect to the database.'
#
# Logger: Notifying all attached observers...
# [FileSubscriber] Notified and wrote to app.log