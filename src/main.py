from src.dataframe import DataFrame, from_csv
from src.series import Series

# From data dictionary
data_dict = {
    "Stock": Series(["Google", "Apple", "Microsoft", "Tesla"]),
    "price": Series([35.2, 234.3, 34.0, 50.92]),
    "taxed": Series([False, True, True, False, ]),
}
df = DataFrame(data_dict)

# Print Series
print("Stock names:", df["Stock"])
print("Stock price > 50:", df[df["price"] > 50]["Stock"])
print("Stock price > 40.5 and Taxed:", df[(df["price"] > 40.5) & (df["taxed"])])
df["price"] = df["price"] * 1.1
print("Index goes up:", df)

# From CSV - De Niro's movies
df_deniro = from_csv("../data/deniro.csv", header=True)
print(df_deniro.get_column_types())
result = df_deniro[(df_deniro["Year"] > 1985.0) & (df_deniro["Year"] <= 1995.0) & (df_deniro["Score"] > 90.0)]
result_inverted = df_deniro[
    ~((df_deniro["Year"] > 1985.0) & (df_deniro["Year"] <= 1995.0) & (df_deniro["Score"] > 90.0))]
print("Movie between 1985 to 1995 and score > 90:", result)
print("Inverted and score > 90 (only names):", result_inverted[result_inverted["Score"] > 90]["Title"])
