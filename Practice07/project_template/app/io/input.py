import pandas as pd

def input_from_console():
    """
    Read text from console input.
    """
    text = input("Enter text here: ")
    return text

def read_file_builtin(path):
    """
    Read text from file using built-in Python functions.
    """
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def read_file_pandas(path):
    """
    Read file using pandas library.
    """
    df = pd.read_csv(path)
    return df.to_string()
