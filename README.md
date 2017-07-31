Python performance tips and evaluation
===

This project intends to publish simple performance tests using different optimization techniques and libraries for 
python and publish the difference in performance obtained.

Numba
==

Numba is a library that at first seems to be pretty simple to be used, however a simple usage of it can hurt 
performance instead of making it better.


| Function name                   | Mean Time | Total Time | Number of Calls |
| ------------------------------- | --------- | ---------- | --------------- |
| simple_function                 | 0.0071    | 0.0071     | 1               | 
| simple_function_numba           | 0.0635    | 0.0635     | 1               |
| simple_function_numba_optimized | 0.0014    | 0.0014     | 1               |
