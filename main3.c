#include <stdio.h>

int main() {

int i=2;

while(i<1000){

    i=i*2;
}

printf("the value of i is %d\n",i);

    char  c='a';

    for (c='a'; c<='d'; c++) {
        printf("%c\n", c);
    }

    printf("%d\n",i);
i=1024;
    do {
        i*=2;
    }
    while(i<1000);

printf("the value of i is %d\n",i);

for (int i=1;i<=20;i++){
    for (int j=1;j<=20;j++){
        printf("%d ",j);
        if(j==20){
            printf("\n");
        }

    }
}
    return 0;
}