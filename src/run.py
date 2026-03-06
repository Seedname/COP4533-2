from fifo import fifo
from lru import lru
from optff import optff
from parse import read_input, write_output


if __name__ == "__main__":
    # specify file name here
    file_name = "file2"

    # read the input
    k, m, requests = read_input(file_name)

    # pass through each function
    fifo_misses = fifo(k, m, requests)
    lru_misses = lru(k, m, requests)
    optff_misses = optff(k, m, requests)

    # write the output
    output = write_output(file_name, fifo_misses, lru_misses, optff_misses)

    print(output)
