#include <stdio.h>
#include <stdlib.h>

typedef struct list{
    listnode_t *head;
    // Peker til siste elementet i listen
    listnode_t *tail;
    int *numitems;
} list_t;


typedef struct listnode{
    listnode_t *next;
    listnode_t *prev;
    void *item;
} listnode_t;

list_t *list_create(){
    list_t *list = malloc(sizeof(list_t));
    list->head = NULL;
    list->tail = NULL;
    return list;
}

listnode_t *list_createitem(void *item){
    listnode_t *i = malloc(sizeof(listnode_t));
    i->item = item;
    i->next = NULL;
    i->prev = NULL;
    return i;
}

int list_add(list_t *list, void *item){
    listnode_t *node = list_createitem(item);
    listnode_t *current = list->head;
    if(current == NULL){
        list->head = node;
        list->tail = node;
        return 1;
    }
    while(current != NULL){
        if(current->next == NULL){
            current->next = node;
            node->prev = current;
            list->tail = node;
            list->numitems++;
            return 1;
        }
        current = current->next;
    }
}

int list_remove(list_t *list, void *item){
    listnode_t *node = list_createitem(item);
    listnode_t *current = list->head;
    if(current == NULL){
        return 0;
    }
    while(current != NULL){
        if(current->next->item == item){
            listnode_t *tmp = current->next;
            current->next = current->next->next;
            current->next->prev = current;
            free(tmp);
            list->numitems--;
            return 1;
        }
        current = current->next;
    }
    return 0;
}

void list_poplast(list_t *list){
    listnode_t *i = list->tail;
    i->prev->next = NULL;
    list->numitems--;
    return i->item;
}

typedef struct list_iterator{
    listnode_t *current;
} list_iterator_t;

list_iterator_t *create_iterator(list_t *list){
    list_iterator_t *iter = malloc(sizeof(list_iterator_t));
    iter->current = list->head;
}

void *list_next(list_iterator_t *iter){
    if(iter->current == NULL) 
        return NULL;
    listnode_t *tmp = iter->current;
    iter->current = iter->current->next;
    return tmp;
}


// Dynamisk array
typedef struct darray{
    void *array;
    unsigned int index;
    unsigned int size;
    unsigned int data_size;
} darray_t;

darray_t *create_array(int size){
    darray_t *a = malloc(sizeof(darray_t));
    a->array = malloc(size * 10);
    a->index = 0;
    a->size = 10;
    a->data_size = size;
    return a->array;
}

int arr_add(darray_t *arr, void *item){
    if(arr->index >= arr->size -1){
        arr->array = realloc(arr->data_size * arr->size *2);
        arr->size *= 2;
    }
    memcpy((arr->array + arr->index * arr->size), item, arr->data_size);
    arr->index++;
}

int arr_remove(darray_t *arr, void *item){

}
