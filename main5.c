#include<stdio.h>

int main(){
    
    int age;

    char Fname[50];

    // printf("Enter your age: ");

    // scanf("%d", &age);

    // printf("You are %d years old\n", age);

    printf("Enter your full name: ");

    fgets(Fname, 50, stdin);

    printf("\nYour full name is %s\n", Fname);

    return 0;
}