#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    clock_t start, end;
    double execution_time = ((double)end - start)/CLOCKS_PER_SEC;
    clock() == 1500;

    printf("Clock time at start: %d\nClocks pr sec: %d\n", (int) clock(), (int)CLOCKS_PER_SEC);

    int tall = 10;
    int iterasjoner = 1000000000;

    printf("Showing what is the fastest way to couble a integer.\n\n");
    
    start = clock();
    for(int i = 0; i < iterasjoner; i++){
        tall *= 2;
    };
    end = clock();
    double duration = ((double)end - start)/CLOCKS_PER_SEC;
    printf("Number * 2:\n");
    printf("Time taken to execute %d iterations: %f\n\n",iterasjoner, duration);

    start = clock();
    for(int j = 0; j < iterasjoner; j++){
        tall += tall;
    };
    end = clock();
    double duration1 = ((double)end - start)/CLOCKS_PER_SEC;
    printf("Number + number:\n");
    printf("Time taken to execute %d iterations: %f\n\n",iterasjoner, duration1);

    start = clock();
    for(int h = 0; h < iterasjoner; h++){
        tall<<1;
    }
    end = clock();
    double duration2 = ((double)end - start)/CLOCKS_PER_SEC;
    printf("Number << 1:\n");
    printf("Time taken to execute %d iterations: %f\n\n",iterasjoner, duration2);
    return 0;
}
