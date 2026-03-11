import pandas as pd

class ExcelReader:

    def get_data(self, file, sheet):
        df = pd.read_excel(file, sheet_name=sheet)
        df.columns = df.columns.str.strip()
        return df