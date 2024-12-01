# Start
import pandas as pd
import numpy as np

data = pd.read_csv("./inputs/day1part1input.txt", sep="\s\s\s", index_col=False, engine="python")

df = pd.concat(
    [
        data.left.sort_values().reset_index(drop=True),
        data.right.sort_values().reset_index(drop=True),
    ],
    axis=1
)

print(np.sum(np.abs(df.left - df.right)))
