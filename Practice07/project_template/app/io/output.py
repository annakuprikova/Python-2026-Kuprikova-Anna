def print_to_console(text):
    """
    Print text to console.
    """
    print(text)


def write_to_file(path, text):
    """
    Write text to file using built-in Python functions.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)