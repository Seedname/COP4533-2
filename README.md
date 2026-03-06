# COP 4533 Assignment 2

**Names:**  
Julian Dominguez (Seedname) - 80849534  
Alex Milanes (Alex42006) - 51506411  

## Usage

Running this program requires Python 3.14.

To run an input file, use the command
```sh
python3 src/run.py
```  

Change the input file by updating the `file_name` variable on line `9`. Do not include the path to the file, nor the `.in` extension. The resulting number of misses for the FIFO, LRU, and OPTFF algorithms can be found in `outputs/[file_name].out`

### Input/Output

Define an input file in the `inputs/` directory. Input files must be in the format `[name].in`.  

Example input file `inputs/file1.in`:
```
5 55
0 1 1 2 2 2 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9
```  

The first line contains the cache size and the number of requests. The next line contains the requests in chronological order. 

Output files return how many times each algorithm finds a cache miss (FIFO, LRU, and OPTFF). Running `run.py` on this example input file returns the following output:
```
FIFO  : 10
LRU   : 10
OPTFF : 10
```

### Written Component

The written component for this assignment can be found in COP4533-2.pdf.