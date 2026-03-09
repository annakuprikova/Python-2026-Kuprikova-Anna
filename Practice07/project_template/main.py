from app.io.input import input_from_console, read_file_builtin, read_file_pandas
from app.io.output import print_to_console, write_to_file

def main():
    console_text = input_from_console()
    file_text = read_file_builtin("data/input.txt")
    pandas_text = read_file_pandas("data/data.csv")

    print_to_console(console_text)
    print_to_console(file_text)
    print_to_console(pandas_text)

    write_to_file("data/output.txt", console_text + "\n" + file_text)

if __name__ == '__main__':
    main()