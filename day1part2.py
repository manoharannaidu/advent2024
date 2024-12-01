
# Start
import pandas as pd
import numpy as np

data = pd.read_csv("./inputs/day1part1input.txt", sep="\s\s\s", index_col=False, engine="python")

myset = data.left.unique()

print(data.right[data.right.isin(myset)].value_counts().reset_index().pipe(lambda df: df.right.mul(df["count"]).sum()))
