from interpreter import Interpreter
from sys import exit


def valid_file(filepath: str) -> None:
    """If file extension is not 'bf' or 'b' stop the process."""
    file_extension = filepath.split(".")[1]
    if file_extension not in ["bf", "b"]:
        exit(f"Invalid file extension '{file_extension}'")


def get_file_text(filepath: str) -> str:
    with open(filepath, "r") as f:
        lines = f.readlines()
        s = ""
        for line in lines:
            s += line
        return s


if __name__ == '__main__':
    filepath = "test.bf"
    valid_file(filepath)

    file_text = get_file_text(filepath)
    interpreter = Interpreter(file_text)
    interpreter.execute()
