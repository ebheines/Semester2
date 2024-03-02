#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"
#include "common.h"

typedef struct listnode listnode_t;

struct listnode{
    listnode_t *prev;
    listnode_t *next;
    void *item;
};

struct list{
    listnode_t *head;
    // listnode_t *tail;
    int numitems;
    cmpfunc_t comparefunc;
};

list_t *list_create(){
    list_t *list = malloc(sizeof(list_t));

    if(!list){
        fprintf(stderr, "Memory allocation failed!\n");
        exit(EXIT_FAILURE);
    }

    list->head = NULL;
    list->numitems = 0;

    return list;
}

void list_destroy(list_t *list){
    free(list);
}

int list_size(list_t *list){
    return list->numitems;
}

int list_addfirst(list_t *list, void *elem){

    listnode_t *node = malloc(sizeof(listnode_t));

    node->item = elem;
    node->next = list->head;
    node->prev = NULL;
    list->head = node;

    if(list->head->item == elem){
        list->numitems++;
        return 1;
    }
    else
        return 0;
}

int list_addlast(list_t *list, void *elem){
    listnode_t *current = malloc(sizeof(listnode_t));

    if(list->head == NULL){
        current->item = elem;
        current->next = NULL;
        current->prev = NULL;

        list->head = current;
        return 1;
    }

    current->item = elem;
    current->next = NULL;

    listnode_t *node;
    node = list->head;
    while((node->next != NULL)){
        node = node->next;
    }

    current->prev = node;
    node->next = current;

    node = list->head;
    while((node->next != NULL)){
        node = node->next;
    }

    if(node->item == elem){
        list->numitems++;
        return 1;
    }
    else{
        return 0;
    }
}

void *list_popfirst(list_t *list){
    listnode_t *current;

    current = list->head;

    list->head = list->head->next;
    list->head->prev = NULL;
    list->numitems--;

    return current->item;
}

void *list_poplast(list_t *list){
    listnode_t *current, *pop;

    current = list->head;

    while(current->next != NULL){
        current = current->next;
    }

    pop = current;
    free(current);
    list->numitems--;
    
    return pop->item;
}

int list_contains(list_t *list, void *elem){
    listnode_t *current;
    current = list->head;

    while(current->item != elem){
        if(current->item == elem)
        return 1;
        current = current->next;
    }
    
    return 0;
}

void printlist(list_t *list){
    listnode_t *node = list->head;

    while(node->next != NULL){
        printf("%s, ", (char*)node->item);
        node = node->next;
    }
}

void list_sort(list_t *list){
    listnode_t *current, *tmp;
    current = list->head;

    while(current->item != NULL){
        if(current->item >= current->next->item)
        continue;
        if(current->item < current->next->item)
        tmp->item = current->item;
        current->next->item = tmp->item;
        current->item = current->next->item;

        current = current->next;
    }
};




typedef struct list_iter list_iter_t;

struct list_iter{
    listnode_t *next;
    listnode_t *prev;
    list_t *list;
};  

list_iter_t *list_createiter(list_t *list){
    list_iter_t *iter = malloc(sizeof(list_iter_t));
    iter->next = list->head;
    iter->list = list;
    iter->prev = NULL;
    return iter;
};

void list_destroyiter(list_iter_t *iter){
    free(iter);
}

int list_hasnext(list_iter_t *iter){
    if(iter->next == NULL)
        return 0;
    else
        return 1;
}

void *list_next(list_iter_t *iter){
    if(iter->next != NULL)
        iter->next = iter->next->next;
}
