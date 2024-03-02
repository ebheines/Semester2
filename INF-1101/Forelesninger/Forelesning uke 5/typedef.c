#include <stdio.h>

typedef int tall;
typedef int (*funksjon)(int, int);

int legg_sammen(int a, int b){
    return a + b;
}

int main(){
    tall a = 10;

    // En funksjonspeker med variabel "int", setter parantes runt "*funksjon" for å vise at det er funksjonen vi peker til  
    //int (*funksjon)(int, int) = &legg_sammen;


    // En lettere måte å bruke en funksjonspeker ved hjelp av typedef
    funksjon fn = legg_sammen;
    
    while(a < 15){
        printf("Tallet er %d\n", a);
        a++;
    }
}