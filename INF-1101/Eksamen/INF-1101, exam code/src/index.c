#include "index.h"
#include "map.h"
#include "parser.h"
#include "set.h"
#include "common.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <printing.h>


struct index{
    map_t *map;
    double document_count;
};

/* For compare query paths */
int compare_query_path(void *a, void *b){
    query_result_t *query_a = (query_result_t *)a;
    query_result_t *query_b = (query_result_t *)b;

    return compare_strings(query_a->path, query_b->path);
}

/* For comparing query scores */
int compare_query_score(void *a, void *b){
    query_result_t *query_a = (query_result_t *)a;
    query_result_t *query_b = (query_result_t *)b;

    return ((query_b->score) - (query_a->score)) * 100;
}

/*
 * Creates a new, empty index.
 */
index_t *index_create(){
    index_t *index = malloc(sizeof(index_t));
    index->map = map_create(compare_strings, hash_string);
    index->document_count = 0;

    return index;
}

/*
 * Destroys the given index.  Subsequently accessing the index will
 * lead to undefined behavior.
 */
void index_destroy(index_t *index){
    map_destroy(index->map, free, (void *) set_destroy);
    free(index);
}

/*
 * Takes in a list of words and returns a map with the words as keys
 * and the value being the amount of times the word is in the 
 * document
*/
map_t *word_counter(list_t *words) {

    /* Creating a map and iterator for the list */
    map_t *wordfreq = map_create(compare_strings, hash_string);
    list_iter_t *iter = list_createiter(words);
    char *current;

    /* Iterating through the list */
    while(list_hasnext(iter)) {
        current = list_next(iter);

        /* Adding the word if the word is not in the map already */
        if(!map_haskey(wordfreq, current)) {
            double *value = malloc(sizeof(double));
            *value = 1;
            map_put(wordfreq, current, value);
        }

        /* Increasing the score if the word is already in the map */
        else {
            double *value = map_get(wordfreq, current);
            (*value)++;
            map_put(wordfreq, current, value);
        }
    }
    list_destroyiter(iter);
    return wordfreq;
}

/*
 * Adds the given path to the given index, and index the given
 * list of words under that path.
 * NOTE: It is the responsibility of index_addpath() to deallocate (free)
 *       'path' and the contents of the 'words' list.
 */
void index_addpath(index_t *index, char *path, list_t *words){

    /* Create a map of all the words in the words list */
    char *current;
    map_t *wordfreq = word_counter(words);

    /* Iterates through the list given */
    while(list_size(words) != 0) {
        current = list_popfirst(words);

        /* 
         * Checking if the word is already in the map, and if it is
         * then adding the current path to the set with the right score
         */
        if(map_haskey(index->map, current) != 0){
            set_t *set = map_get(index->map, current);

            query_result_t *result = malloc(sizeof(query_result_t));
            if(result == NULL){
                printf("Error creating query_result in function index_addpath");
            }
            result->path = strdup(path);
            result->score = (*(double*)map_get(wordfreq, current) / list_size(words));

            /* Adding the result to the set of documents */
            if(set_contains(set, result) == 0){
                set_add(set, result);
            }
        }

        /*
         * If the word is not already in the map, its added
         * with a set as the value and the word as the key
        */
        else{
            set_t *set = set_create(compare_query_path);

            query_result_t *result = malloc(sizeof(query_result_t));
            result->path = strdup(path);
            result->score = (*(double*)map_get(wordfreq, current) / list_size(words));

            set_add(set, result);
            map_put(index->map, current, set);
            }
    }

    index->document_count++;
    free(path);
}


/*
 * Performs the given query on the given index.  If the query
 * succeeds, the return value will be a list of paths (query_result_t). 
 * If there is an error (e.g. a syntax error in the query), an error 
 * message is assigned to the given errmsg pointer and the return value
 * will be NULL.
 */
list_t *index_query(index_t *index, list_t *query, char **errmsg){
    
    /* All the iterators and data structures required */
    list_iter_t *parsefuckingsiter = list_createiter(query);
    parse_node *tree = create_tree(query, parsefuckingsiter);
    set_t *path = evaluate_tree(index->map, tree);
    list_t *result_list = list_create(compare_query_score);
    set_iter_t *iter = set_createiter(path);

    if(tree == NULL){
        DEBUG_PRINT("Error creating tree in fucntion index query\n");
        return NULL;
    }

    /*
     * Iterating through the parse tree created by the parser
     * and returning all the paths connected to the word
     * being searched for
    */
    while(set_hasnext(iter)){
        query_result_t *qtips = (query_result_t*)set_next(iter);
        query_result_t *result = malloc(sizeof(query_result_t));
        if(qtips == NULL){
            DEBUG_PRINT("Error making query result qtips in funciton index_query");
            return NULL;
        }
        result->path = qtips->path;
        result->score = qtips->score * log(index->document_count / set_size(path)) * 10;
        list_addlast(result_list, result);
    }

    set_destroy(path);
    set_destroyiter(iter);
    list_sort(result_list);
    list_destroyiter(parsefuckingsiter);
    return result_list;
}