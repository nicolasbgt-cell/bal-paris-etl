import sqlite3
import pandas as pd


def load(df: pd.DataFrame, db_path: str = "adresses.db", table_name: str = "adresses") -> None:
    with sqlite3.connect(db_path) as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)


if __name__ == "__main__":
    from extract import extract
    from transform import transform

    df = extract("data/bal-75115.csv")
    df_clean = transform(df)

    load(df_clean, "adresses.db")
    print(f"{len(df_clean)} lignes chargées dans adresses.db")
