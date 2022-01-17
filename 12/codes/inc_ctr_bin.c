//Code written on December 9, 2020
// by G V V Sharma
//This program implements the incrementing counter in binary

#include <stdio.h>
#include <time.h>

void delay(unsigned int);
unsigned int increment(unsigned char D, unsigned char C, unsigned char B, unsigned char A);



unsigned int * increment(unsigned char * input)
{
unsigned char W, X, Y, Z;
unsigned char output[4];

W = input[0];
X = input[1];
Y = input[2];
Z = input[3];

output[0] = (W&X&Y&(~Z))|((~W)&(~X)&(~Y)&Z);//Boolean function for D
output[1]=((~Z)&(~Y)&(~X)&W)|((~Z)&(~Y)&X&(~W))|((~Z)&Y&(~X)&W)|((~Z)&Y&X&(~W));
output[2]=((~Z)&(~Y)&X&W)|((~Z)&Y&(~X)&(~W))|((~Z)&Y&(~Z)&W)|((~Z)&Y&X&(~W));
output[3] = ((~W)&(~X)&(~Y)&(~Z))|((~W)&(X)&(~Y)&(~Z))|((~W)&(~X)&Y&(~Z))|((~W)&X&Y&(~Z))|((~W)&(~X)&(~Y)&(Z));
//Boolean function for A
}

//The  main function
int main(void)
{

unsigned char i=0;
unsigned char input[4];

while(i < 9) //begin while 
{
printf("%d %d\n",i,i+1);//i th row of the table
delay(1000000);
i = i+1;
}//end while loop
printf("%d %d\n",i,i-9);//i th row of the table

return 0;
}
//end main function






printf("%x\n",one&D);//Output D
printf("%x\n",one&A);//Output D
return 0;
}

//delay function
void delay(unsigned int mseconds)
{
    clock_t goal = mseconds + clock();
    while (goal > clock());
}
