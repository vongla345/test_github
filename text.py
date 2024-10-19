import pandas as pd

def read_text_file(file_path):
    return pd.read_csv(file_path, sep="\t")

if __name__ == "__main__":
    print(read_text_file("data.txt"))