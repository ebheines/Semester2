#include <stdio.h>
#include <stdlib.h>

#include "set.h"

typedef struct set set_t;

struct set{
    int size;
    void **array;
    cmpfunc_t cmpfunc;
};

// Merging two subarrays from the given array
// A left array from the start to middle
// and a right array from the middle to end

static void merge(set_t *set, int left, int mid, int right){
// Making variables for for/while loops and index for the new arrays
    int i, j, k;
    int index1 = mid - left + 1;
    int index2 = right - mid;

// Allocating memory for the new arrays
    void **Leftarr = malloc(index1 * sizeof(void*));
    void **Rightarr = malloc(index2 * sizeof(void*));

// Filling the Left array
    for(i = 0; i < index1; i++){
        Leftarr[i] = set->array[left + i];
    }

// Filling the Right array
    for(j = 0; j < index2; j++){
        Rightarr[j] = set->array[mid + 1 + j];
    }   

// Merging the Left and Right array into the original array
    i = 0;
    j = 0;
    k = left;
    while(i < index1 && j < index2){
        if(Leftarr[i] < Rightarr[j]){
            set->array[k] = Leftarr[i];
            i++;
        }
        else{
            set->array[k] = Rightarr[j];
            j++;
        }
        k++;
    }

// Merging the remaining elements from Left and Right array, if there are any
    while(i < index1){
        set->array[k] = Leftarr[i];
        i++;
        k++;
    }

    while(j < index2){
        set->array[k] = Rightarr[j];
        j++;
        k++;
    }
    free(Leftarr);
    free(Rightarr);
}

// Recursive function for sorting the subarrays we've made
static void mergeSort(set_t *set, int left, int right){
    if(left < right){
        int mid = left + (right - left) / 2;

        mergeSort(set, left, mid);
        mergeSort(set, mid + 1, right);

        merge(set, left, mid, right);
    }
}

// Calling the mergeSort-function and implements the right arguments
static void set_sort(set_t *set){
    mergeSort(set, 0, set->size - 1);
}


// Bubblesort for the set, only here to test
// static void bubble_sort(set_t *set){
//    void **tmp;
//    for(int i = 0; i < set->size; i++){
    //    for(int j = 0; j < set->size; j++){
        //    if(set->array[i] < set->array[j]){
            //    tmp = set->array[j]; 
            //    set->array[j] = set->array[i];
            //    set->array[i] = tmp;
        //    }
    //    }
//    }
// }

// Creates a new arrayset
set_t *set_create(cmpfunc_t cmpfunc){
    // Allocates memory for the set
    set_t *new_set = malloc(sizeof(set_t));
    // Allocates memory for the array of the set
    new_set->array = malloc(sizeof(void *));    
    new_set->size = 0;
    new_set->cmpfunc = cmpfunc;

    return new_set;
}

// Destroys the given set
void set_destroy(set_t *set){
    free(set->array);
    free(set);
}

// Return the size of the given set
int set_size(set_t *set){
    return set->size;
}

// Adds the given element to the given set
void set_add(set_t *set, void *elem){
    // Checks if the element is already in the set
    if(!set_contains(set, elem)){
        // If the element is not in the set, its added to the set
        // and the array is reallocted to make space for the element
        set->array = realloc(set->array, sizeof(void *) * (set->size + 1));
        set->array[set->size] = elem;
        set->size++;
        bubble_sort(set);
    }
}

// Checks if a given element is in the given set
int set_contains(set_t *set, void *elem){
    // Loops through the given set
    for(int i = 0; i < set->size; i++){
        // Checks if any of the elements in the set is equal to the 
        // given element, if so returns 1
        if(set->cmpfunc(elem, set->array[i]) == 0)
            return 1;
    }
    return 0;
}

// Return a union set of the two given sets containing all the elements
// containing in either a or b
set_t *set_union(set_t *a, set_t *b){
    set_t *new_set = set_create(a->cmpfunc);

    for(int i = 0; i < a->size; i++){
        set_add(new_set, a->array[i]);
    }

    for(int i = 0; i < b->size; i++){
        set_add(new_set, b->array[i]);
    }
    return new_set;
}

// Returns a new set containing all the elements that are 
// both in a and b
set_t *set_intersection(set_t *a, set_t *b){
    set_t *new_set = set_create(a->cmpfunc);

    for(int i = 0; i < a->size; i++){
        if(set_contains(b, a->array[i]))
            set_add(new_set, a->array[i]);
    }
    return new_set;
}

// Return a new set containing the elements thats in a
// and not in b
set_t *set_difference(set_t *a, set_t *b){
    set_t *new_set = set_create(a->cmpfunc);

    for(int i = 0; i < a->size; i++){
        if(!set_contains(b, a->array[i]))
            set_add(new_set, a->array[i]);
    }
    return new_set;
}

// Returns a new set thats a copy of the given set
set_t *set_copy(set_t *set){
    set_t *new_set = set_create(set->cmpfunc);

    for(int i = 0; i < set->size; i++){
        set_add(new_set, set->array[i]);
    }
    return new_set;
}


typedef struct set_iter set_iter_t;
struct set_iter{
    void **array;
    int index;
    int size;
};

// Creates a iterator to iterate trought the given set
set_iter_t *set_createiter(set_t *set){
    set_iter_t *iter = malloc(sizeof(set_iter_t));

    if(iter == NULL)
        return NULL;

    iter->array = set->array;
    iter->index = 0;
    iter->size = set->size;
    return iter;
}

// Destroys the given iterator
void set_destroyiter(set_iter_t *iter){
    free(iter);
}

// Returns 0 if the iterator has reached the end,
// and returns 1 if not
int set_hasnext(set_iter_t *iter){
    if(iter->index >= iter->size)
        return 0;
    else
        return 1;
    if(set_hasnext(iter))
    {
        elem = iter->array[iter->index++];
    }
    else
    {
        return NULL;
    }
    return elem;
}