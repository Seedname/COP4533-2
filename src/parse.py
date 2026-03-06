import pathlib


def read_input(file_name: str) -> tuple[int, int, list[int]]:
    parent_dir = pathlib.Path(__file__).parent
    input_directory = parent_dir.parent / "inputs"

    input_file = input_directory / f"{file_name}.in"

    if not input_file.exists():
        raise ValueError(f"Input file {file_name}.in does not exist")

    with open(input_file) as f:
        # read the lines of the input file
        lines: list[str] = f.readlines()

    # checks that the file is empty
    if len(lines) == 0:
        raise ValueError("Empty file")
    elif len(lines) < 2:
    # check that the file has at least two lines
        raise ValueError("File must contain at 2 rows")
    
    # check that the first line in the file contains a pair of numbers
    parameters = lines[0].strip().split(" ")

    if len(parameters) != 2 or not parameters[0].isdigit() or not parameters[1].isdigit():
        raise ValueError("Invalid input format")

    k, m = map(int, parameters)

    # make sure the second line contains m digits
    requests = lines[1].strip().split(" ")

    if len(requests) != m:
        raise ValueError(f"{len(requests)} requests instead of {m}")
    
    if not all(item.isdigit() for item in requests):
        raise ValueError("All requests must be integers")
    
    requests = list(map(int, requests))

    # return the valid data
    return k, m, requests


def read_output(file_name: str) -> list[int]:
    parent_dir = pathlib.Path(__file__).parent
    output_directory = parent_dir.parent / "outputs"

    output_file = output_directory / f"{file_name}.out"

    if not output_file.exists():
        raise ValueError(f"Output file {file_name}.output does not exist")

    with open(output_file, 'r') as f:
        lines = f.readlines()

    # make sure that theres 3 lines
    if len(lines) < 3:
        raise ValueError("Invalid output format")

    # split the lines by colon, and only look at lines with colons
    lines = [line.strip().split(":")[1].strip() for line in lines if ":" in line]

    # make sure that there are three valid lines
    if len(lines) != 3:
        raise ValueError("Must have three valid lines")
    
    # make sure they are all integers
    if not all(item.isdigit() for item in lines):
        raise ValueError("Values must be integers")
    
    # convert them to integers and return
    return list(map(int, lines))


def write_output(file_name: str, fifo_misses: int, lru_misses: int, optff_misses: int) -> str:
    parent_dir = pathlib.Path(__file__).parent
    output_directory = parent_dir.parent / "outputs"

    output_file = output_directory / f"{file_name}.out"

    output_string = f"FIFO  : {fifo_misses}\nLRU   : {lru_misses}\nOPTFF : {optff_misses}"

    with open(output_file, 'w') as f:
        f.write(output_string)

    return output_string


if __name__ == "__main__":
    # testing reading files
    file_name = "file1"

    k, m, requests = read_input(file_name)
    print(f"{k = }")
    print(f"{m = }")
    print(f"{requests = }")

    print()

    fifo_misses, lru_misses, optff_misses = read_output(file_name)
    print(f"{fifo_misses = }")
    print(f"{lru_misses = }")
    print(f"{optff_misses = }")