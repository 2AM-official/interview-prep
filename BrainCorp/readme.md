# Matrix Transpose and Mutiply Implementation

This project implements a C++ program to transpose and multiply two matrices.

## Task: Write a high-performance, portable linear algebra libray supporting transpose and multiplication.

- To achieve portable goal, I wrote a Matrix class including Matrix.h and Matrix.cpp for better access the implementation.
- To achieve high-performance, based on the multiply implementation, I add cache blocking to improve the performance. Cache blocking is a technique for optimizing matrix multiplication performance by reducing the number of cache misses. A cache miss occurs when the processor needs to fetch data from main memory because it is not present in the cache. This can be a time-consuming operation, since accessing main memory is much slower than accessing the cache. By reducing the number of cache misses, cache blocking can improve the performance of matrix multiplication by a factor of 2-3 on modern CPUs, particularly for large matrices that do not fit entirely in the cache.



## Compiling and Running
You can compile this code using the provided `Makefile` via the `make` command:
```
$ make
g++ -Wall -Wextra -pedantic -std=c++11 -c Matrix.cpp -o Matrix.o
g++ -Wall -Wextra -pedantic -std=c++11 -c MatrixTest.cpp -o MatrixTest.o
g++ -Wall -Wextra -pedantic -std=c++11 Matrix.o MatrixTest.o -o MatrixTest
```
If you want to clean up your environment by deleting all the compiled executables, you can simply run `make clean`:
```
$ make clean 
rm -f Matrix.o MatrixTest.o MatrixTest
```
Here's an example of how the file should look like when running from the command line:
```
$./MatrixTest
Test Matrix Construction andn Access Success!
Test Matrix Transpose Success!
Test Matrix Multiply Success!
Time with cache blocking: 2.37188 seconds
Time without cache blocking: 2.69574 seconds
```
You can change the function in MatrixTest.cpp to test different functions of the implementation.

## Result
I tested the multiply implementation when the size $N$ of two random matrix is 500, 1000 and 1500, and the blocking size is 64. Here is the result:
|Size $N$ |Time with cache blocking(seconds) | Time without cache blocking(seconds)|
|---      |---                      |---                         |
|500      |2.37188                  |2.69574                     |
|1000     |19.0837                  |27.0872                     |
|1500     |68.2097                  |159.814                     |

From the result we can find that the cache blocking improve the performance greatly when the data size getting larger.
