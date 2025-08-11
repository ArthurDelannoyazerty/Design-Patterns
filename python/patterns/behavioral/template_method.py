from abc import ABC, abstractmethod

# ---------------------------------------------------------------------------- #
#                                Abstract Class                                #
# ---------------------------------------------------------------------------- #
class ReportGenerator(ABC):
    def generate_report(self, input_path: str, output_path: str):
        print(f"--- Starting report generation for {self.__class__.__name__} ---")
        
        data = self._load_data(input_path)
        print("Step 1: Data loaded successfully.")

        analysis_result = self._analyze_data(data)
        print("Step 2: Data analysis complete.")

        self._save_report(analysis_result, output_path)
        print("Step 3: Report saved successfully.")
        
        print("--- Report generation finished. ---\n")

    def _analyze_data(self, data: list[dict]) -> dict:
        print('Analyzing data...')

    @abstractmethod
    def _load_data(self, path: str) -> list[dict]:
        pass

    @abstractmethod
    def _save_report(self, analysis: dict, path: str):
        pass


# ---------------------------------------------------------------------------- #
#                                Concrete Class                                #
# ---------------------------------------------------------------------------- #
class CsvReportGenerator(ReportGenerator):
    def _load_data(self, path: str) -> list[dict]:
        print(f"Loading data from CSV file: {path}")

    def _save_report(self, analysis: dict, path: str):
        print(f"Saving report to CSV file: {path}")


class JsonReportGenerator(ReportGenerator):
    def _load_data(self, path: str) -> list[dict]:
        print(f"Loading data from JSON file: {path}")

    def _save_report(self, analysis: dict, path: str):
        print(f"Saving report to JSON file: {path}")


# ---------------------------------------------------------------------------- #
#                                  Main/Client                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    csv_processor = CsvReportGenerator()
    csv_processor.generate_report("sales.csv", "csv_report.txt")

    json_processor = JsonReportGenerator()
    json_processor.generate_report("sales.json", "json_report.json")

# ---------------------------------- Output ---------------------------------- #
# --- Starting report generation for CsvReportGenerator ---
# Loading data from CSV file: sales.csv
# Step 1: Data loaded successfully.
# Analyzing data...
# Step 2: Data analysis complete.
# Saving report to CSV file: csv_report.txt
# Step 3: Report saved successfully.
# --- Report generation finished. ---
# 
# --- Starting report generation for JsonReportGenerator ---
# Loading data from JSON file: sales.json
# Step 1: Data loaded successfully.
# Analyzing data...
# Step 2: Data analysis complete.
# Saving report to JSON file: json_report.json
# Step 3: Report saved successfully.
# --- Report generation finished. ---