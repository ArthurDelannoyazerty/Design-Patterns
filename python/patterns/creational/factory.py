from abc import ABC, abstractmethod

# ---------------------------------------------------------------------------- #
#                                Abstract Class                                #
# ---------------------------------------------------------------------------- #

# ---------------------------------- Product --------------------------------- #
class Serializer(ABC):
    @abstractmethod
    def serialize(self, data, format):
        pass

# ---------------------------------- Creator --------------------------------- #
class Exporter(ABC):
    @abstractmethod
    def get_serializer(self) -> Serializer:
        pass

    def export(self, data, format):
        serializer = self.get_serializer()
        return serializer.serialize(data, format)
    

# ---------------------------------------------------------------------------- #
#                                Concrete Class                                #
# ---------------------------------------------------------------------------- #

# ---------------------------------- Product --------------------------------- #
class JsonSerializer(Serializer):
    def serialize(self, data, format):
        if format == 'JSON':
            print('PRODUCT: Serialized to JSON')
        else:
            raise ValueError("Unsupported format")

class XmlSerializer(Serializer):
    def serialize(self, data, format):
        if format == 'XML':
            print('PRODUCT: Serialized to XML')
        else:
            raise ValueError("Unsupported format")

# ---------------------------------- Creator --------------------------------- #
class JsonExporter(Exporter):
    def get_serializer(self) -> Serializer:
        return JsonSerializer()

class XmlExporter(Exporter):
    def get_serializer(self) -> Serializer:
        return XmlSerializer()


# ---------------------------------------------------------------------------- #
#                                  Main/Client                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":

    class Song:
        def __init__(self, song_id, title, artist):
            self.song_id = song_id
            self.title = title
            self.artist = artist
    
    # The data object to be serialized
    song = Song(1, 'title', 'artist')
    
    # --- Client wants to serialize to JSON ---
    print("--- Using the JSON Exporter ---")
    json_exporter_factory = JsonExporter()
    json_exporter_factory.export(song, 'JSON')
    
    print("\n" + "="*30 + "\n")

    # --- Client wants to serialize to XML ---
    print("--- Using the XML Exporter ---")
    xml_exporter_factory = XmlExporter()
    xml_exporter_factory.export(song, 'XML')


# ---------------------------------- Output ---------------------------------- #

# --- Using the JSON Exporter ---
# PRODUCT: Serialized to JSON
#
# ==============================
#
# --- Using the XML Exporter ---
# PRODUCT: Serialized to XML