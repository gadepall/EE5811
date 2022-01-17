from function import *


Expression = ['0000', '0001', '0010', '0011', '0101', '0111', '1000', '1001', '1010', '1110', '1111']

Minimised_Prime_Implecants,Prime_Implecants,Inputs,No_of_variables,time_taken = main_without_txt(Expression)

print("\nOptimal Expression is ",expr(Minimised_Prime_Implecants).upper())