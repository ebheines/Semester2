#include "set.h"
#include <stdlib.h>
#include <time.h>

#include "printing.h"

static int compare_ints(void *a, void *b){
    int *ia = a;
    int *ib = b;

    return (*ia)-(*ib);
}

static void *newint(int i){
    int *p = malloc(sizeof(int));
    *p = i;
    return p;
}

static void printset(char *prefix, set_t *set)
{
    set_iter_t *it;

    INFO_PRINT("%s", prefix);
    it = set_createiter(set);
    while (set_hasnext(it)) {
	    int *p = set_next(it);
	    printf(" %d", *p);
    }
    printf("\n");
    set_destroyiter(it);
}

static void dumpset(char *prefix, set_t *set)
{
    printset(prefix, set);
    set_destroy(set);
}

int main(int argc, char **argv){
    set_t *tnumbers, *all, *evens, *odds, *nonprimes, *primes;
    int i, j, n = 100000;
    int **numbers;

    clock_t start, end;
    double time_used;

    /* Create sets */
    all = set_create(compare_ints);
    evens = set_create(compare_ints);
    odds = set_create(compare_ints);
    nonprimes = set_create(compare_ints);
    primes = set_create(compare_ints);
    tnumbers = set_create(compare_ints);

    /* Allocate numbers from 0 to n */
    numbers = (int **) malloc(sizeof(int*) * (n+1));
    for (i = 0; i <= n; i++) {
	    numbers[i] = newint(i);
    }

    start = clock();
    for(i = 0; i <= n; i++){
        set_add(tnumbers, numbers[i]);
    }
    end = clock();
    time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Times used to add %d elements to a set:   %f\n", n, time_used);    


    /* Initialize sets */
    for (i = 0; i <= n; i++) {
		set_add(all, numbers[i]);
	    if (i % 2 == 0) {
	        set_add(evens, numbers[i]);
	    }
	    else {
	        set_add(odds, numbers[i]);
	    }
        // if (i < 2) {
            // set_add(nonprimes, numbers[i]);
        // }
        // else {
	        // for (j = i+i; j <= n; j += i) {
	            // set_add(nonprimes, numbers[j]);
	        // }
        // }
	    // if (!set_contains(nonprimes, numbers[i])) {
	        // set_add(primes, numbers[i]);
	    // }
    }

    printf("Union, intersection and difference with %d elements: \n\n", n);

    start = clock();
    set_union(evens, odds);
    end = clock();
    time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Time used for set_union: %f\n", time_used);

    start = clock();
    set_intersection(evens, odds);
    end = clock();
    time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Time used for set_intersection: %f\n", time_used);
 
    start = clock();
    set_difference(evens, odds);
    end = clock();
    time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Time used for set_difference: %f\n", time_used);

    for (i = 0; i <= n; i++) {
	    free(numbers[i]);
    }
    free(numbers);
}