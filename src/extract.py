import pandas as pd

def extract(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, sep=";")
    return df

if __name__ == "__main__":
    df = extract("data/bal-75115.csv")
    print(df.shape)
    print(df.head())
