Write a Python function that generates a matrix with n rows (where n is an input parameter), each row containing: a) a
permutation of size 6 where the value 1 does not appear in the first half; b) a value representing the quality of the
permutation. The quality of an individual permutation P (of size 6) is determined by the sum of positions where even
values appear (for example, the individual P=[2,5,4,3,0,1] is feasible because 1 appears in the last position; the
quality of P is 0+2+4=6). Evaluate the n generated individuals and display the maximum quality.