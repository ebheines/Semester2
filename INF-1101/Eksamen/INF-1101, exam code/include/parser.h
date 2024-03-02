#ifndef PARSEBNF_H
#define PARSEBNF_H

#include "list.h"
#include "map.h"
#include "set.h"

typedef struct parse_node parse_node;

parse_node *new_node(int type, char *value);

parse_node *pares_query(list_t *query, list_iter_t *iter);

parse_node *andterm(list_t *query, list_iter_t *iter);

parse_node *orterm(list_t *query, list_iter_t *iter);

parse_node *term(list_t *query, list_iter_t *iter);

parse_node *create_tree(list_t *query, list_iter_t *iter);

set_t *evaluate_tree(map_t *map, parse_node *node);

#endif