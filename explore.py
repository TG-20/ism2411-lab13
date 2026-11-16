"""
ISM2411 Lab 13 — First DataFrame — Retail Sales Explorer
Author: Toghrul Guliyev
Run: python explore.py

SELF-ASSESSMENT
1. A boolean filter checks a condition on every row (True or False) and
   keeps only the rows where it is True, like an Excel AutoFilter.

2. df["revenue"] returns a Series (one column, 1-D). df[["revenue"]]
   returns a DataFrame (a table with one column, 2-D). It matters when a
   method needs a DataFrame (e.g. to_csv with a header, merging, or
   selecting more columns later) or when you want a Series method like
   .mean() to return a single number.

3. Reproducibility: the script gives the same result every run, records
   every step so it can be reviewed and reused, and scales to millions of
   rows. Excel can't promise any of that.
"""

import pandas as pd

# ── Exercise 1: Load it ───────────────────────────────────────
df = pd.read_csv("data/retail_sales.csv")
print("Exercise 1")
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.dtypes)

# ── Exercise 2: Filter by region ──────────────────────────────
print("\nExercise 2")
south = df[df["region"] == "South"]
print("South rows:", len(south))
print(south.head())

# ── Exercise 3: Top 5 by revenue ──────────────────────────────
print("\nExercise 3")
top5 = df.sort_values("revenue", ascending=False).head(5)
print(top5)

# ── Exercise 4: Two-condition filter ──────────────────────────
print("\nExercise 4")
big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]
print("Big South rows:", len(big_south))
print(big_south.head())

# ── Exercise 5: A new column ──────────────────────────────────
print("\nExercise 5")
df["per_unit"] = df["revenue"] / df["quantity"]
print(df.head())
print("Mean per-unit price:", df["per_unit"].mean())

# ── Exercise 6: Unique values ─────────────────────────────────
print("\nExercise 6")
print(df["region"].unique())
print(df["region"].value_counts(dropna=False))

# ── Exercise 7: Select columns ────────────────────────────────
print("\nExercise 7")
subset = df[["region", "product", "revenue"]]
print("Subset shape:", subset.shape)

# ── Exercise 8: Save ──────────────────────────────────────────
print("\nExercise 8")
df.to_csv("data/explored.csv", index=False)
print("Saved to data/explored.csv")