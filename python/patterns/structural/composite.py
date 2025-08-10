import abc

# ---------------------------------------------------------------------------- #
#                                 Abstact Class                                #
# ---------------------------------------------------------------------------- #
class FileSystemComponent(abc.ABC):
    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name
    
    @abc.abstractmethod
    def get_size(self) -> int:
        pass

    # These methods are relevant for composites (directories)
    # but are included here to provide a common interface.
    def add(self, component: 'FileSystemComponent'):
        raise NotImplementedError("This operation is not supported.")

    def remove(self, component: 'FileSystemComponent'):
        raise NotImplementedError("This operation is not supported.")


# ---------------------------------------------------------------------------- #
#                                Concrete Class                                #
# ---------------------------------------------------------------------------- #
class File(FileSystemComponent):
    """The Leaf"""
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self._size = size

    def get_size(self) -> int:
        print(f"Calculating size of file '{self.get_name()}': {self._size} bytes")
        return self._size

class Directory(FileSystemComponent):
    """The Composite"""
    def __init__(self, name: str):
        super().__init__(name)
        self._children: list[FileSystemComponent] = []

    def add(self, component: 'FileSystemComponent'):
        self._children.append(component)

    def remove(self, component: 'FileSystemComponent'):
        self._children.remove(component)

    def get_size(self) -> int:
        total_size = 0
        for child in self._children:
            total_size += child.get_size()
        print(f"Total size for directory '{self.get_name()}' is {total_size} bytes.")
        return total_size


# ---------------------------------------------------------------------------- #
#                                  Client/Main                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    file1 = File("document.txt", 100)
    file2 = File("image.jpg", 500)
    file3 = File("archive.zip", 1000)
    
    sub_dir = Directory("Pictures")
    sub_dir.add(file2)
    
    root_dir = Directory("My Documents")
    root_dir.add(file1)
    root_dir.add(sub_dir)
    root_dir.add(file3)

    print("--- Getting size of a single file ---")
    file1.get_size()

    print("\n--- Getting total size of the entire root directory ---")
    total_disk_space = root_dir.get_size()
    print(f"\n=> Total disk space used by '{root_dir.get_name()}': {total_disk_space} bytes")

# ---------------------------------- Output ---------------------------------- #
# --- Getting size of a single file ---
# Calculating size of file 'document.txt': 100 bytes     
#
# --- Getting total size of the entire root directory ---
# Calculating size of file 'document.txt': 100 bytes     
# Calculating size of file 'image.jpg': 500 bytes        
# Total size for directory 'Pictures' is 500 bytes.      
# Calculating size of file 'archive.zip': 1000 bytes     
# Total size for directory 'My Documents' is 1600 bytes. 
#
# => Total disk space used by 'My Documents': 1600 bytes 