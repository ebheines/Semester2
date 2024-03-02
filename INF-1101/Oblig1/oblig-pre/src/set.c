#include <stdio.h>
#include <stdlib.h>

#include "set.h"
#include "list.h"

typedef struct set set_t;

struct set{
    int size;
    list_t *list;
    cmpfunc_t cmpfunc;
};


set_t *set_create(cmpfunc_t cmpfunc){
    set_t *set = malloc(sizeof(set_t));
    if(set == NULL)
        return NULL;
    set->list = list_create(cmpfunc);
    set->size = 0;
    set->cmpfunc = cmpfunc;
    
    return set;
}

void set_destroy(set_t *set){
    free(set->list);
    free(set);
}

int set_size(set_t *set){
    return set->size;
}

void set_add(set_t *set, void *elem){
    if(list_contains(set->list, elem))
        return NULL;
    else
        list_addfirst(set->list, elem);
        set->size++;
    list_sort(set->list);
}

int set_contains(set_t *set, void *elem){
    return list_contains(set->list, elem);
}

// Bruk iter for å komme dæ gjennom listen i stede for node
// Gjør koden mye ryddigere og bedre !!!!

set_t *set_union(set_t *a, set_t *b){
    list_iter_t *aiter = list_createiter(a->list);
    list_iter_t *wifebiter = list_createiter(b->list);

    set_t *new_set = set_create(a->cmpfunc);

    while(list_hasnext(aiter)){
        set_add(new_set, list_next(aiter));
    }

    while(list_hasnext(wifebiter)){
        set_add(new_set,list_next(wifebiter));
    }

    set_destroyiter(aiter);
    set_destroyiter(wifebiter);
    return new_set;
}

set_t *set_intersection(set_t *a, set_t *b){
    list_iter_t *aiter = list_createiter(a->list);

    set_t *new_set = set_create(a->cmpfunc);
    void *elem;

    while(list_hasnext(aiter)){
        elem = list_next(aiter);
        if(set_contains(b, elem))
            set_add(new_set, elem);
    }

    set_destroyiter(aiter);
    return new_set;
}

set_t *set_difference(set_t *a, set_t *b){
    list_iter_t *aiter = list_createiter(a->list);

    set_t *new_set = set_create(a->cmpfunc);
    void *elem;

    while(list_hasnext(aiter)){
        elem = list_next(aiter);
        if(!set_contains(b, elem))
            set_add(new_set, elem);
    }
    
    set_destroyiter(aiter);
    return new_set;
}

set_t *set_copy(set_t *set){
    listnode_t *node = set->list->head;
    set_t *new_set = set_create(set->cmpfunc);

    while(node != NULL){
        set_add(new_set, node->elem);
        node = node->next;
    }
    return new_set;
}

typedef struct set_iter set_iter_t;
struct set_iter{
    list_iter_t *listiter;
};

set_iter_t *set_createiter(set_t *set){
    set_iter_t *iter = malloc(sizeof(set_iter_t));
    if(iter == NULL)
        return NULL;
    
    iter->listiter = list_createiter(set->list);
    return iter;
}

void set_destroyiter(set_iter_t *iter){
    free(iter);
}

int set_hasnext(set_iter_t *iter){
    return list_hasnext(iter->listiter);
}

void *set_next(set_iter_t *iter){
    return list_next(iter->listiter);

}

