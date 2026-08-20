import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset="cle_interop")
    df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
    df["long"] = pd.to_numeric(df["long"], errors="coerce")
    df = df.dropna(subset=["lat", "long"])

    return df

if __name__ == "__main__":
    from extract import extract

    df = extract("data/bal-75115.csv")
    print("Avant nettoyage :", df.shape)

    df_clean = transform(df)
    print("Après nettoyage :", df_clean.shape)
    print(df_clean.isna().sum())
