import pandas as pd
INPUT_FILE = "messy.csv"
OUTPUT_FILE = "cleaned.csv"
REMOVE_DUPLICATES = True
df = pd.read_csv(INPUT_FILE)
df.columns = (
    df.columns
      .str.strip()   
      .str.lower()  
      .str.replace(" ", "_")
)
df = df.apply(
    lambda col: col.str.strip() if col.dtype == "object" else col
)
df = df.replace("", pd.NA)
df = df.dropna(how="all")        
df = df.dropna(axis=1, how="all")
if REMOVE_DUPLICATES:
    df = df.drop_duplicates()
df.to_csv(OUTPUT_FILE, index=False)
print("CSV cleaning complete.")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")