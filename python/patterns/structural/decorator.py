import abc

# ---------------------------------------------------------------------------- #
#                                Abstract Class                                #
# ---------------------------------------------------------------------------- #
class IDataManager(abc.ABC):
    @abc.abstractmethod
    def write_data(self, filename: str, data: bytes):
        pass

    @abc.abstractmethod
    def read_data(self, filename: str) -> bytes:
        pass


# ---------------------------------------------------------------------------- #
#                                Concrete Class                                #
# ---------------------------------------------------------------------------- #
class SimpleFileManager(IDataManager):
    """The Concrete Component"""
    def write_data(self, filename: str, data: bytes):
        print("SimpleFileManager: Writing raw data.")

    def read_data(self, filename: str) -> bytes:
        print("SimpleFileManager: Reading raw data.")
        return b"raw data"


class DataManagerDecorator(IDataManager):
    """The Base Decorator """
    _wrapped_component: IDataManager = None

    def __init__(self, component: IDataManager):
        self._wrapped_component = component

    def write_data(self, filename: str, data: bytes):
        self._wrapped_component.write_data(filename, data)

    def read_data(self, filename: str) -> bytes:
        return self._wrapped_component.read_data(filename)


class CompressionDecorator(DataManagerDecorator):
    """Concrete Decorator"""
    def write_data(self, filename: str, data: bytes):
        print("CompressionDecorator: Compressing data.")
        compressed_data = b"compressed"
        super().write_data(filename, compressed_data)

    def read_data(self, filename: str) -> bytes:
        compressed_data = super().read_data(filename)
        print("CompressionDecorator: Decompressing data.")
        decompressed_data = b"decompressed"
        return decompressed_data
    
class EncryptionDecorator(DataManagerDecorator):
    """Concrete Decorator"""
    def __init__(self, component: IDataManager):
        super().__init__(component)
        self._key = 0xAB  # A simple, fixed XOR key

    def write_data(self, filename: str, data: bytes):
        print("EncryptionDecorator: Encrypting data.")
        encrypted_data = bytes([b ^ self._key for b in data])
        super().write_data(filename, encrypted_data)

    def read_data(self, filename: str) -> bytes:
        encrypted_data = super().read_data(filename)
        print("EncryptionDecorator: Decrypting data.")
        decrypted_data = bytes([b ^ self._key for b in encrypted_data])
        return decrypted_data


# ---------------------------------------------------------------------------- #
#                                  Client/Main                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    my_data = b"This is my super secret and highly important data that needs to be secured."
    filename = "secret.dat"

    file_manager = SimpleFileManager()                          # The component
    compressed_manager = CompressionDecorator(file_manager)     # The concrete decorator
    final_manager = EncryptionDecorator(compressed_manager)     # The concrete decorator

    print("--- Writing data through the decorator stack ---")
    final_manager.write_data(filename, my_data)
    
    print("\n--- Reading data back through the same decorator stack ---")
    retrieved_data = final_manager.read_data(filename)

# ---------------------------------- Output ---------------------------------- #
# --- Writing data through the decorator stack ---
# EncryptionDecorator: Encrypting data.
# CompressionDecorator: Compressing data.
# SimpleFileManager: Writing raw data.
# 
# --- Reading data back through the same decorator stack ---
# SimpleFileManager: Reading raw data.
# CompressionDecorator: Decompressing data.
# EncryptionDecorator: Decrypting data.