//Code written on December 5, 2020
//Revised  December 8, 2020
// by G V V Sharma
//This program implements the incremental decoder using boolean logic in C

#include <stdio.h>

//The  main function
int main(void)
{

//2 bits = 1 baud
//4 bits = 1 nibble
//8 bits = 1 byte

//unsigned char takes input as 1 byte

unsigned char  Z=0x01,Y=0x00,X=0x00,W=0x01;//inputs in hex	
unsigned char one = 0x01;//used for displaying the output in bit
unsigned char A,B,C,D;//outputs

D = (W&X&Y&(~Z))|((~W)&(~X)&(~Y)&Z);//Boolean function for D
B=((~Z)&(~Y)&(~X)&W)|((~Z)&(~Y)&X&(~W))|((~Z)&Y&(~X)&W)|((~Z)&Y&X&(~W));
C=((~Z)&(~Y)&X&W)|((~Z)&Y&(~X)&(~W))|((~Z)&Y&(~Z)&W)|((~Z)&Y&X&(~W));
A = ((~W)&(~X)&(~Y)&(~Z))|((~W)&(X)&(~Y)&(~Z))|((~W)&(~X)&Y&(~Z))|((~W)&X&Y&(~Z))|((~W)&(~X)&(~Y)&(Z));
//Boolean function for A

printf("%x%x%x%x",one&Z,one&Y,one&X,one&W);//Iutput ZYXW
printf(" ");
printf("%x%x%x%x\n" ,one&D,one&C,one&B,one&A);//Output DCBA
return 0;
}
