def read_csv(folder, filename):
    import pandas as pd

    filepath = f'{folder}/{filename}.csv'
    df = pd.read_csv(filepath)

    return df
