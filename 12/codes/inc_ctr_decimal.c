//Code written on December 9, 2020
// by G V V Sharma
//This program implements the incrementing counter in decimal

#include <stdio.h>
#include <time.h>

//delay function
void delay(unsigned int mseconds)
{
    clock_t goal = mseconds + clock();
    while (goal > clock());
}

//The  main function
int main(void)
{

unsigned char i=0;


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
