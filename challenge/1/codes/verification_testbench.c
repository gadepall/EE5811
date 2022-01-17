//Code written on January 16, 2022
// by Tadipatri Uday Kiran Reddy    

#include <stdio.h>
#include <time.h>

// Two input NAND
unsigned char NAND(unsigned char A, unsigned char B){
    return ~(A&B);
}

// NOT from NAND
unsigned char NOT(unsigned char A){
    return NAND(A, A);
}

// Two input AND using NAND
unsigned char AND(unsigned char A, unsigned char B){
    return NOT(NAND(A, B));
}

// Two input OR using NAND
unsigned char OR(unsigned char A, unsigned char B){
    return NAND(NOT(A), NOT(B));
}

// Two input XOR using NAND
unsigned char XOR(unsigned char A, unsigned char B){
    return NAND(NAND(NOT(A), B), NAND(A, NOT(B)));
}

// This function is a counter
void increment(unsigned char * input, unsigned char* output)
{
    unsigned char P, Q, R, S;

    P = input[0];
    Q = input[1];
    R = input[2];
    S = input[3];

    // output[0] = (~P&Q&R&S)|(P&~Q)|(P&~R)|(P&~S);
    // output[1] = (~Q&R&S)|(Q&~R)|(Q&~S);
    // output[2] = R^S;
    // output[3] = ~S;
    output[0] = XOR(P, AND(AND(Q, R), S));
    output[1] = XOR(Q, AND(R, S));
    output[2] = XOR(R, S);
    output[3] = NOT(S);

}

// This function implements logic
void LOGIC(unsigned char * input, unsigned char* stream)
{
    unsigned char P, Q, R, S;

    P = input[0];
    Q = input[1];
    R = input[2];
    S = input[3];

    // *stream = (P&Q&R)|(~Q&~R)|(~Q&~S)|(~P&S);
    *stream = OR(OR(AND(AND(P, Q), R), AND(NOT(Q), NAND(R, S))), AND(NOT(P), S));

}

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

    unsigned char  prev_state[4];
    unsigned char next_state[4];
    unsigned char stream;
    unsigned char one = 0x01;

    prev_state[0] = 0x00;
    prev_state[1] = 0x00;
    prev_state[2] = 0x00;
    prev_state[3] = 0x00;

    printf("P Q R S\t|\tH\n");
    printf("-------------\n");

    while(i < 16)
    {   
        LOGIC(prev_state, &stream);

        printf("%d %d %d %d\t|\t%d\n", 
            one&prev_state[0], one&prev_state[1], one&prev_state[2], one&prev_state[3],
            one&stream);

        increment(prev_state, next_state);

        // Delay for simulating clock
        delay(500);
        // Loop incrementor
        i = i+1;

        prev_state[0] = next_state[0]; 
        prev_state[1] = next_state[1]; 
        prev_state[2] = next_state[2]; 
        prev_state[3] = next_state[3];

    }

    return 0;
}