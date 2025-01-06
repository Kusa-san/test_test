#include<stdio.h>

int x=5;
int y=5;
int l=2;
int *k=&l;

int n1=1;
int n2=2;

int sub(int x, int y){

    if (x>y)
        return x-y;

    if (y>x)
        return y-x;

    if (x==y)
        return 0;
    
    }

void msg(char msg){

        if (msg =='n')
            printf("no\n");
            
        else if (msg == 'y')
            printf("yes\n");
           
        else
            printf("not found\nnot found\nnot found\n");
           
    }

int div( int n1, int n2){

        if (n1>n2)
            return n1/n2;

        else
            return n2/n1;
    }

void mult(int *no1){

    (*k)=(*k)*2;
}

int main(){

    printf("%d - %d = %d\n",x , y, sub(x,y));

    printf("%d / %d = %d \n",n1,n2,div(n1,n2));

    msg('y');
    msg('n');
    msg('d');

    mult(k);
    printf("%d\n",l);

    return 0;
}