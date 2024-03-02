#include "set.h"
#include "map.h"
#include "list.h"
#include "parser.h"
#include <printing.h>
#include <stdio.h>
#include <stdlib.h>

/* Easier way to identify the Boolean operators */
enum Search{
    ANDNOT,
    AND,
    OR,
    WORD
};

/* Struct for the node in the parser */
struct parse_node{
    parse_node *left;
    parse_node *right;
    char *value;
    int type;
};

/* Creating a new node with a value and a type */
parse_node *new_node(int type, char *value){
    parse_node *node = malloc(sizeof(parse_node));
    node->left = NULL;
    node->right = NULL;
    node->value = value;
    node->type = type;

    return node;
}

/* Start of the recursive parsing, identifing the ANDNOT operator */
parse_node *parse_query(list_t *query, list_iter_t *iter){

    /* Creating two nodes, a root for the parsetree and one going to
    the next function */
    parse_node *root = NULL;
    parse_node *left_child = andterm(query, iter);

    /* Checking if the query is empty or the next word is an operator */
    if(!list_hasnext(iter) || compare_strings(list_peeknext(iter), "ANDNOT") != 0){
        // continue to next rule
        return left_child;
    }

    /* If not, going to the next word and create a new node with the ANDNOT operator */
    else{
        list_next(iter);
        root = new_node(ANDNOT, NULL);
        root->left = left_child;
        root->right = parse_query(query, iter);
    }
    return root;
}

/* Checking for the AND operator */
parse_node *andterm(list_t *query, list_iter_t *iter){

    /* Creating two nodes, one as a root and one for the next
    function */
    parse_node *root = NULL;
    parse_node *left_child = orterm(query, iter);

    /* Checking if the query is empty or the next word is a operator */
    if(!list_hasnext(iter) || compare_strings(list_peeknext(iter), "AND") != 0){
        return left_child;
    }

    /* If not, going to the next word and create a new node with the AND operator */
    else{
        list_next(iter);
        root = new_node(AND, NULL);
        root->left = left_child;
        root->right = andterm(query, iter);
    }
    return root;
}

/* Checking for the OR operator */
parse_node *orterm(list_t *query, list_iter_t *iter){

    /* Creating two nodes, one as a root and one for the next
    function */
    parse_node *root = NULL;
    parse_node *left_child = term(query, iter);

    /* Checking if the query is empty or the next word is a operator */
    if(!list_hasnext(iter) || compare_strings(list_peeknext(iter), "OR") != 0){
        return left_child;
    }

    /* If not, going to the next word and create a new node with the OR operator */
    else{
        list_next(iter);
        root = new_node(OR, NULL);
        root->left = left_child;
        root->right = orterm(query, iter);
    }
    return root;
}

/* Checking for "(" or ")", and identifying the current word as a WORD */
parse_node *term(list_t *query, list_iter_t *iter){

    /* Creating two nodes, one as a root and one for
    the result of the function as well as a current
    being the current word in the query */
    parse_node *root;
    parse_node *result;
    char *current = list_next(iter);

    /* Checkinf ro potential () */
    if(compare_strings(current, "(") == 0){
        root = parse_query(query, iter);
        current = list_next(iter);
        if(compare_strings(current, ")") == 1){
            DEBUG_PRINT("Error in function: term\n");
        }
        return root;
    }

    /* Creating a new node as a WORD operator */
    result = new_node(WORD, current);
    return result;
}

/* Creating a new parse tree */
parse_node *create_tree(list_t *query, list_iter_t *iter){
    parse_node *root = parse_query(query, iter);
    return root;
}

/* Function for evaluating the identified operators */
set_t *evaluate_tree(map_t *map, parse_node *node) {

    /* Creates sets to be returned to the search engine */
    set_t *left_child, *right_child;
    set_t *set = set_create(compare_strings);

    /* Checks for the node type, being the Boolean operators */
    switch (node->type) {

        /* If the node type is WORD, return the set in the index map */
        case WORD:
            left_child = set_copy((set_t *) map_get(map, node->value));
            if (left_child != NULL) {
                return left_child;
            } else {
                return set;
            }

        /* If the node type is AND, return the intersection of the returned sets */    
        case AND:
            left_child = evaluate_tree(map, node->left);
            right_child = evaluate_tree(map, node->right);
            return set_intersection(left_child, right_child);

        /* If the node type is AND, return the union of the returned sets */  
        case OR:
            left_child = evaluate_tree(map, node->left);
            right_child = evaluate_tree(map, node->right);
            return set_union(left_child, right_child);

        /* If the node type is AND, return the difference of the returned sets */  
        case ANDNOT:
            left_child = evaluate_tree(map, node->left);
            right_child = evaluate_tree(map, node->right);
            return set_difference(left_child, right_child);

        /* Returning a Error if something goes wrong */
        default:
            printf("Error in evaluate tree\n");
            return NULL;
    }
    return set;

}




