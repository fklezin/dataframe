import unittest
from src.series import Series


class SeriesTest(unittest.TestCase):

    def setUp(self):
        self.series_str_mock = ["X4E", "T3B", "F8D", "C7X", "VR4"]
        self.series_int_mock = [1, -2, 12312, 122, 0]
        self.series_float_mock = [1.123, 100.0, -300.123, 0.0, 0.0]
        self.series_numeric_mock = [1.1, -2, 12312.1, 122.2, 0]
        self.series_bool_mock = [True, False, True, True, False, None]
        self.series_err_mock = [True, 2, "asd", True, False, None]

    def test_init(self):
        self.assertEqual(Series(self.series_str_mock).data_type, str)
        self.assertEqual(Series(self.series_float_mock).data_type, float)
        self.assertEqual(Series(self.series_int_mock).data_type, int)
        self.assertEqual(Series(self.series_bool_mock).data_type, bool)
        self.assertEqual(Series(self.series_numeric_mock).data_type, float)
        with self.assertRaises(TypeError):
            Series(self.series_err_mock)

    def test_comparisons(self):
        series_comparison_1 = Series([0, 2, 4, 6, 8])
        series_comparison_2 = Series([-1, 5, 4, 5, 4])
        self.assertTrue((series_comparison_1 == series_comparison_2)[2])
        self.assertTrue((series_comparison_1 > series_comparison_2)[4])
        self.assertTrue((series_comparison_1 <= series_comparison_2)[1])
        self.assertTrue((series_comparison_1 <= series_comparison_2)[2])
        self.assertTrue((series_comparison_1 != series_comparison_2)[0])

        self.assertFalse((series_comparison_1 != series_comparison_2)[2])
        self.assertFalse((series_comparison_1 > series_comparison_2)[1])

    def test_expressions(self):
        series_expression_1 = Series([0, 6, 4.1])
        series_expression_2 = Series([-1, 5, 1])
        self.assertEqual((series_expression_1 + series_expression_2).values, [-1, 11, 5.1])
        self.assertEqual((series_expression_1 * series_expression_2).values, [0, 30, 4.1])
        self.assertEqual((series_expression_1 / series_expression_2).values, [0, 1.2, 4.1])
        self.assertEqual((series_expression_1 // series_expression_2).values, [0, 1, 4])
        self.assertEqual((series_expression_1 - 100).values, [-100, -94, -95.9])

    def test_bool(self):
        series_bool_1 = Series([True, False, True])
        series_bool_2 = Series([False, False, True])

        self.assertEqual((series_bool_1 & series_bool_2).values, [False, False, True])
        self.assertEqual((series_bool_1 | series_bool_2).values, [True, False, True])
        self.assertEqual((series_bool_1 ^ series_bool_2).values, [True, False, False])
        self.assertEqual((~series_bool_1).values, [False, True, False])


if __name__ == '__main__':
    unittest.main()
