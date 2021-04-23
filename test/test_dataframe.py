import unittest
from src.dataframe import DataFrame, from_csv
from src.dataframe import Series


class DataFrameTest(unittest.TestCase):
    def setUp(self):
        self.series_str_mock = ["X4E", "T3B", "F8D", "C7X", "VR4"]
        self.series_int_mock = [1, -2, 12312, 122, 0]
        self.series_float_mock = [1.123, 100.0, -300.123, 0.0, 0.0]
        self.series_bool_mock = [True, False, True, True, False, None]
        self.series_err_mock = [True, 2, "asd", True, False, None]

    def test_init(self):
        DataFrame({
            "int": Series(self.series_int_mock),
            "float": Series(self.series_float_mock),
            "str": Series(self.series_str_mock)})

    def test_from_csv(self):
        df_deniro = from_csv("data/deniro.csv", header=True)
        self.assertEqual(df_deniro.get_column_headers(), ["Year", "Score", "Title"])
        self.assertEqual(df_deniro.get_series_length(), 87)


if __name__ == '__main__':
    unittest.main()
