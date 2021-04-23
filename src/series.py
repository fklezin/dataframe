class Series:
    SUPPORTED_DTYPES = [str, bool, int, float]
    SUPPORTED_NUMERIC_TYPES = [int, float]

    def __init__(self, values):
        self._set_data_type(values)
        for value in values:
            if isinstance(value, self.data_type):
                pass
            elif self.data_type in self.SUPPORTED_NUMERIC_TYPES and type(value) in self.SUPPORTED_NUMERIC_TYPES:
                pass
            elif value is None:
                pass
            else:
                raise TypeError("Types don't match!")
        self.values = values

    def __getitem__(self, query):
        if isinstance(query, int):
            return self.values[query]
        if isinstance(query, Series):
            return self._filter(query)
        raise TypeError("Wrong type!")

    def __str__(self):
        string = str(self.values) + "\n"
        return string

    # Comparisons
    def __eq__(self, other):
        if type(other) in self.SUPPORTED_DTYPES:
            result = [value == other for value in self.values]
        else:
            self._is_comparable(other)
            result = [self.values[i] == other.values[i] for i in range(len(self.values))]
        return Series(result)

    def __ne__(self, other):
        if type(other) in self.SUPPORTED_DTYPES:
            result = [value != other for value in self.values]
        else:
            self._is_comparable(other)
            result = [self.values[i] != other.values[i] for i in range(len(self.values))]
        return Series(result)

    def __gt__(self, other):
        if type(other) in self.SUPPORTED_DTYPES:
            result = [value > other for value in self.values]
        else:
            self._is_comparable(other)
            result = [self.values[i] > other.values[i] for i in range(len(self.values))]
        return Series(result)

    def __ge__(self, other):
        if type(other) in self.SUPPORTED_DTYPES:
            result = [value >= other for value in self.values]
        else:
            self._is_comparable(other)
            result = [self.values[i] >= other.values[i] for i in range(len(self.values))]
        return Series(result)

    def __lt__(self, other):
        if type(other) in self.SUPPORTED_DTYPES:
            result = [value < other for value in self.values]
        else:
            self._is_comparable(other)
            result = [self.values[i] < other.values[i] for i in range(len(self.values))]
        return Series(result)

    def __le__(self, other):
        if type(other) in self.SUPPORTED_DTYPES:
            result = [value <= other for value in self.values]
        else:
            self._is_comparable(other)
            result = [self.values[i] <= other.values[i] for i in range(len(self.values))]
        return Series(result)

    # Expressions
    def __add__(self, other):
        if type(other) in self.SUPPORTED_DTYPES:
            result = [value + other for value in self.values]
        else:
            self._is_comparable(other)
            result = [self.values[i] + other.values[i] for i in range(len(self.values))]
        return Series(result)

    def __sub__(self, other):
        if type(other) in self.SUPPORTED_DTYPES:
            result = [value - other for value in self.values]
        else:
            self._is_comparable(other)
            result = [self.values[i] - other.values[i] for i in range(len(self.values))]
        return Series(result)

    def __mul__(self, other):
        if type(other) in self.SUPPORTED_DTYPES:
            result = [value * other for value in self.values]
        else:
            self._is_comparable(other)
            result = [self.values[i] * other.values[i] for i in range(len(self.values))]
        return Series(result)

    def __truediv__(self, other):
        if type(other) in self.SUPPORTED_DTYPES:
            result = [value / other for value in self.values]
        else:
            self._is_comparable(other)
            result = [self.values[i] / other.values[i] for i in range(len(self.values))]
        return Series(result)

    def __floordiv__(self, other):
        if type(other) in self.SUPPORTED_DTYPES:
            result = [value // other for value in self.values]
        else:
            self._is_comparable(other)
            result = [self.values[i] // other.values[i] for i in range(len(self.values))]
        return Series(result)

    def __and__(self, other):
        self._is_comparable(other)
        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] and other.values[i])
        return Series(result)

    def __or__(self, other):
        self._is_comparable(other)
        result = [self.values[i] or other.values[i] for i in range(len(self.values))]
        return Series(result)

    def __xor__(self, other):
        self._is_comparable(other)
        result = [self.values[i] != other.values[i] for i in range(len(self.values))]
        return Series(result)

    def __invert__(self):
        result = [not self.values[i] for i in range(len(self.values))]
        return Series(result)

    # Private functions
    def _is_comparable(self, other):
        if not isinstance(other, Series):
            raise Exception("Not instance Series!")
        if len(self.values) != len(other.values):
            raise Exception("Not same lengths!")
        if self.data_type != other.data_type:
            raise Exception("Not same data type!")
        return True

    def _set_data_type(self, values):
        data_type = None
        for value in values:
            if value is not None:
                data_type = type(value)
                break
        if data_type not in self.SUPPORTED_DTYPES:
            raise Exception("Not supported data type!")

        self.data_type = data_type

    def _filter(self, query):
        if query.data_type != bool:
            raise Exception("Query series records should be bool!")
        if len(query.values) != len(self.values):
            raise Exception("Lengths are not the same!")
        result = []
        for i in range(len(query.values)):
            if query.values[i]:
                result.append(self.values[i])
        return Series(result)
