import abc
import json
from io import StringIO


# ---------------------------------------------------------------------------- #
#                                 Absract Class                                #
# ---------------------------------------------------------------------------- #

# ----------------------------- Abstract Products ---------------------------- #
class DataParser(abc.ABC):
    @abc.abstractmethod
    def parse(self, data: str):
        pass

class DataRenderer(abc.ABC):
    @abc.abstractmethod
    def render(self, data) -> str:
        pass

# ------------------------------ Absract Factory ----------------------------- #
class DataProcessingFactory(abc.ABC):
    @abc.abstractmethod
    def create_parser(self) -> DataParser:
        pass

    @abc.abstractmethod
    def create_renderer(self) -> DataRenderer:
        pass



# ---------------------------------------------------------------------------- #
#                                Concrete Class                                #
# ---------------------------------------------------------------------------- #

# --------------------------------- Products --------------------------------- #
class JSONDataParser(DataParser):
    def parse(self, data: str):
        return json.loads(data)

class JSONDataRenderer(DataRenderer):
    def render(self, data) -> str:
        return json.dumps(data, indent=4)


class CSVDataParser(DataParser):
    def parse(self, data: str):
        lines = data.strip().split('\n')
        header = lines[0].split(',')
        parsed_data = [
            dict(zip(header, row.split(','))) for row in lines[1:]
        ]
        return parsed_data

class CSVDataRenderer(DataRenderer):
    def render(self, data) -> str:
        if not data:
            return ""
        output = StringIO()
        # Write header
        header = data[0].keys()
        output.write(','.join(header) + '\n')
        
        # Write rows
        for row in data:
            output.write(','.join(str(row[key]) for key in header) + '\n')
            
        return output.getvalue().strip()


# --------------------------------- Factories -------------------------------- #
class JSONDataProcessingFactory(DataProcessingFactory):
    def create_parser(self) -> DataParser:
        return JSONDataParser()

    def create_renderer(self) -> DataRenderer:
        return JSONDataRenderer()


class CSVDataProcessingFactory(DataProcessingFactory):
    def create_parser(self) -> DataParser:
        return CSVDataParser()

    def create_renderer(self) -> DataRenderer:
        return CSVDataRenderer()

# ---------------------------------------------------------------------------- #
#                                  Main/client                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":

    def process_and_export_data(factory: DataProcessingFactory, raw_data: str):
        # Use the factory to create the necessary products
        parser = factory.create_parser()
        renderer = factory.create_renderer()

        # Perform the operations
        parsed_data = parser.parse(raw_data)
        
        # Example: Add a new record to the data
        parsed_data.append({"id": "3", "name": "Charlie", "email": "charlie@example.com"})
        
        rendered_data = renderer.render(parsed_data)

        print(f"--- Processing with {factory.__class__.__name__} ---")
        print("Exported Data:")
        print(rendered_data)
        print("\n")


    # The application can choose which factory to use at runtime.
    # Example 1: Exporting to JSON
    json_raw_data = '''
        [
            {
                "id": "1",
                "name": "Alice",
                "email": "alice@example.com"
            },
            {
                "id": "2",
                "name": "Bob",
                "email": "bob@example.com"
            }
        ]
    '''
    json_factory = JSONDataProcessingFactory()
    process_and_export_data(json_factory, json_raw_data.strip())
    
    # Example 2: Exporting to CSV
    csv_raw_data = """
        id,name,email
        1,Alice,alice@example.com
        2,Bob,bob@example.com
    """
    csv_factory = CSVDataProcessingFactory()
    process_and_export_data(csv_factory, csv_raw_data.strip())

# ----------------------------------- Ouput ---------------------------------- #

# --- Processing with JSONDataProcessingFactory ---
# Exported Data:
# [
#     {
#         "id": "1",
#         "name": "Alice",
#         "email": "alice@example.com"
#     },
#     {
#         "id": "2",
#         "name": "Bob",
#         "email": "bob@example.com"  
#     },
#     {
#         "id": "3",
#         "name": "Charlie",
#         "email": "charlie@example.com"
#     }
# ]
#
#
# --- Processing with CSVDataProcessingFactory ---
# Exported Data:
# id,name,email
# 1,Alice,alice@example.com
# 2,Bob,bob@example.com
# 3,Charlie,charlie@example.com