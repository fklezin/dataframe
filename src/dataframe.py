import csv
from tabulate import tabulate
from src.series import Series


class DataFrame:
    def __init__(self, series_dict):
        if not isinstance(series_dict, dict):
            raise Exception("Not a dict!")
        # Check for value type series in columns
        series_dtype = [col for col in series_dict.values() if not isinstance(col, Series)]
        if len(series_dtype) > 0:
            raise Exception("All columns are not Series!")

        self.series = series_dict

    def __getitem__(self, query):
        if type(query) in Series.SUPPORTED_DTYPES:
            if query in self.get_column_headers():
                return self.series[query]
            raise Exception("No such column!")
        if isinstance(query, Series):
            result = {}
            for key, series in self.series.items():
                result[key] = series[query]
            return DataFrame(result)

        raise Exception("Wrong query!")

    def __setitem__(self, column, series):
        if isinstance(column, str) and isinstance(series, Series):
            self.series["column"] = series
        else:
            raise Exception("Wrong query!")

    def __str__(self):
        table = tabulate(self.series, headers=self.get_column_headers())
        return "\n" + table + "\n"

    def get_column_headers(self):
        return list(self.series.keys())

    def get_column_types(self):
        dtypes = [(col, series.data_type) for col, series in self.series.items()]
        return dtypes

    def get_series_length(self):
        header = list(self.get_column_headers())[0]
        return len(self.series[header].values)


# Parse a Data Frame from a csv file
def from_csv(csv_path, delimiter=",", header=False):
    series_dict = {}
    with open(csv_path, "r") as file:
        reader = csv.reader(file, delimiter=delimiter, quoting=csv.QUOTE_NONNUMERIC)
        rows = [row for row in reader]
        file.close()
    if header:
        header = rows.pop(0)
    else:
        header = [str(col) for col in range(0, len(rows[0]))]

    for col, head in enumerate(header):
        series_dict[head] = Series([(row[col]) for row in rows])

    return DataFrame(series_dict)
