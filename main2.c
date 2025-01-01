#include <stdio.h>

char charecter = 'C';

int main() {
//         if (charecter == 'X') {
//             printf("charecter is X\n");
//             // return 0;
//         } else {
//             printf("charecter is %C\n", charecter);
//             // return 1;
//         }

//     switch (charecter) {
//         case 'A':
//             printf("A\n");
//             break;
//         case 'B':
//             printf("B\n");
//             break;
//         case 'C':
//             printf("C\n");
//             break;
//         default:
//             printf("default\n");
//     }

//     int x = 5;
//     printf("%d\n", ++x);
//     printf("%d\n", x++);
//     printf("%d\n", x);
    
//     for  (int i =0; i<5;i++){
//         printf("for loop is = %d\n",i);
//     }
// int i=0;
//     while ( i<5){
//         printf("while loop is = %d\n",i);
//         i++;
//     }
// i=0;
//     do{
//         printf("do while value is = %d\n",i);
//         i++;
//     }
//     while(i<5);

    // for (int i=1;i<7;i++){
    //     if (i==3)
    //         printf("this is the forth loop\n");
    //     else{printf("message\n");}

        for (int i=1 ;i<101;i++)
        {
            if ((i%3==0 && i%5==0)==1)
            printf("fuzz buzz\n");
        else if(i%3==0)
            printf("fuzz\n");
        else if(i%5==0 )
            printf("buzz\n");
        else
            printf("%d\n",i);
        }
    return 0;
    }