# COP 4533 Assignment 2

**Names:**  
Julian Dominguez (Seedname) - 80849534  
Alex Milanes (Alex42006) - 51506411  

## Usage

Running this program requires Python 3.14.

To run an input file, use the command
```sh
python src/run.py
```  

Change the input file by updating the `file_name` variable on line `9`. Do not include the path to the file, nor the `.in` extension. The resulting number of misses for the FIFO, LRU, and OPTFF algorithms can be found in `outputs/[file_name].out`

### Creating custom inputs

Define an input file in the `inputs/` directory. Input files must be in the format `[name].in`.  

Example input file `inputs/test.in`:
```
4
2 1 4 3
2 3 1 4
4 2 1 3 
4 3 2 1
2 3 4 1 
3 1 4 2
3 2 1 4 
2 3 4 1
```  

The first line contains the number of students/hospitals, n, which is 4 in this case. The next n lines are the preference lists for the hospitals in order from top to bottom, left to right. The next n lines are the students' preference lists, ordered the same way. 

Here is a mapping for clarity, with hospitals `a, b, c, d` and students `w, x, y, z`:  

```
Hospitals
a: x w z y
b: x y w z
c: z x w y
d: z y x w

Students
w: b c d a
x: c a d b
y: c b a d
z: b c d a
```

### Creating custom outputs

Define an output file in the `outputs/` directory. Output files must be in the format `[name].out`.  

Example output file `outputs/test.out`:
```
1 2
2 3
3 4
4 1
```

The file has n lines, where n is the number of students/hospitals (4 in this case). Each line contains a hospital-student match, with the hospital on the left and the student on the right.

Here is a mapping for clarity, with hospitals `a, b, c, d` and students `w, x, y, z`:  
```
Matches
a - x
b - y
c - z
d - w
```