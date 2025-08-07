import abc

# ---------------------------------------------------------------------------- #
#                                Abstract Class                                #
# ---------------------------------------------------------------------------- #

# ----------------------------- Abstract Builder ----------------------------- #
class LoggerConfigBuilder(abc.ABC):
    @abc.abstractmethod
    def set_log_level(self, level: str):
        pass

    @abc.abstractmethod
    def enable_file_logging(self, file_path: str):
        pass

    @abc.abstractmethod
    def enable_console_logging(self):
        pass

    @abc.abstractmethod
    def set_message_format(self, msg_format: str):
        pass

    @abc.abstractmethod
    def get_config(self) -> 'LoggerConfig' :
        pass


# ---------------------------------------------------------------------------- #
#                                Concrete Class                                #
# ---------------------------------------------------------------------------- #

# ---------------------------------- Product --------------------------------- #
class LoggerConfig:
    def __init__(self):
        self.log_level = "INFO"
        self.log_to_file = False
        self.log_to_console = True
        self.log_file_path = None
        self.message_format = "[{timestamp}] [{level}]: {message}"

    def __str__(self):
        return (
            f"LoggerConfig(Level: {self.log_level}, "
            f"Log to Console: {self.log_to_console}, "
            f"Log to File: {self.log_to_file}, "
            f"File Path: {self.log_file_path or 'N/A'}, "
            f"Format: '{self.message_format}')"
        )

# ----------------------------- Concrete Builder ----------------------------- #

class ConcreteLoggerConfigBuilder(LoggerConfigBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._config = LoggerConfig()

    def set_log_level(self, level: str) -> 'ConcreteLoggerConfigBuilder':
        self._config.log_level = level
        return self

    def enable_file_logging(self, file_path: str) -> 'ConcreteLoggerConfigBuilder':
        self._config.log_to_file = True
        self._config.log_file_path = file_path
        return self

    def enable_console_logging(self) -> 'ConcreteLoggerConfigBuilder':
        self._config.log_to_console = True
        return self
        
    def set_message_format(self, msg_format: str) -> 'ConcreteLoggerConfigBuilder':
        self._config.message_format = msg_format
        return self

    def get_config(self) -> LoggerConfig:
        config = self._config
        self.reset()  # Reset for the next build
        return config

# --------------------------------- Director --------------------------------- #
class LoggerDirector:
    def __init__(self, builder: LoggerConfigBuilder):
        self._builder = builder

    def build_debug_config(self):
        self._builder.set_log_level("DEBUG").enable_console_logging()

    def build_production_config(self):
        self._builder.set_log_level("ERROR").enable_file_logging("/var/log/app.log")


# ---------------------------------------------------------------------------- #
#                                  Main/Client                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    builder = ConcreteLoggerConfigBuilder()

    # --- Use Case 1: Client builds a custom configuration step-by-step ---
    print("Building a custom logger configuration...")
    custom_config = (
        builder.set_log_level("INFO")
        .enable_file_logging("my_app.log")
        .set_message_format("{level} - {message}")
        .get_config()
    )
    print(f"Created custom config: {custom_config}\n")


    # --- Use Case 2: Client uses the Director for a pre-defined configuration ---
    print("Using a Director to build a debug logger configuration...")
    director = LoggerDirector(builder)
    
    director.build_debug_config()
    debug_config = builder.get_config()
    print(f"Created debug config: {debug_config}\n")

    print("Using a Director to build a production logger configuration...")
    director.build_production_config()
    production_config = builder.get_config()
    print(f"Created production config: {production_config}\n")


# ---------------------------------- Output ---------------------------------- #
# Building a custom logger configuration...
# Created custom config: LoggerConfig(Level: INFO, Log to Console: True, Log to File: True, File Path: my_app.log, Format: '{level} - {message}')
#
# Using a Director to build a debug logger configuration...
# Created debug config: LoggerConfig(Level: DEBUG, Log to Console: True, Log to File: False, File Path: N/A, Format: '[{timestamp}] [{level}]: {message}')
#
# Using a Director to build a production logger configuration...
# Created production config: LoggerConfig(Level: ERROR, Log to Console: True, Log to File: True, File Path: /var/log/app.log, Format: '[{timestamp}] [{level}]: {message}')