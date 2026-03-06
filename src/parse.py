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
    

if __name__ == "__main__":
    # testing reading input "file1.in"
    k, m, requests = read_input("file1")
    print(k, m, requests)