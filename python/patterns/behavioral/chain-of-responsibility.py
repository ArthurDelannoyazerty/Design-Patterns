from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

# ---------------------------------------------------------------------------- #
#                                Abstract class                                #
# ---------------------------------------------------------------------------- #
class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        """Return the next handler in the chain."""
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

# ---------------------------------------------------------------------------- #
#                                Concrete class                                #
# ---------------------------------------------------------------------------- #

# --------------------------------- Handlers --------------------------------- #
class InfoHandler(AbstractHandler):
    def handle(self, request:str) -> str:
        if request.startswith("info"):
            pass
        else:
            return super().handle(request)

class ErrorHandler(AbstractHandler):
    def handle(self, request:str) -> str:
        if request.startswith("error"):
            print("ERROR", request)
        else:
            return super().handle(request)

class FailureHandler(AbstractHandler):
    def handle(self, request:str) -> str:
        if request.startswith("failure"):
            print("FAILURE", request)
        else:
            return super().handle(request)

# ---------------------------- Handler controller ---------------------------- #
class Logger:
    def __init__(self):
        failure_handler = FailureHandler()
        error_handler = ErrorHandler()
        info_handler = InfoHandler()

        info_handler\
            .set_next(error_handler) \
            .set_next(failure_handler)

        self.default_handler = info_handler

    def log(self, message):
        self.default_handler.handle(message)


# ---------------------------------------------------------------------------- #
#                                     Main                                     #
# ---------------------------------------------------------------------------- #
def main():
    requests = [
        "info: this is an info message",
        "error: this is an error message",
        "failure: this is a failure message",
        "unknown: this is an unknown message"]
    
    logger = Logger()
    for request in requests:
        print(f"\nClient: {request}")
        logger.log(request)


if __name__ == "__main__":
    main()

# ------------------------------ Output ------------------------------ #
# Client: info: this is an info message
#
# Client: error: this is an error message    
# ERROR error: this is an error message      
#
# Client: failure: this is a failure message 
# FAILURE failure: this is a failure message 
#
# Client: unknown: this is an unknown message