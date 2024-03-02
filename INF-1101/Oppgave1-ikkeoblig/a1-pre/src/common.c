/* Author: Steffen Viken Valvaag <steffenv@cs.uit.no> */
#include <stdio.h>
#include <printing.h>
#include <string.h>
#include "list.h"

void tokenize_file(FILE *file, list_t *list, int rev)
{
    char *word;
    char buf[101];
    buf[100] = 0;

    while (!feof(file)) {
        /* Skip non-letters */
        fscanf(file, "%*[^a-zA-Z0-9'_]");
        /* Scan up to 100 letters */
        if (fscanf(file, "%100[a-zA-Z0-9'_]", buf) == 1) {
            word = strdup(buf);
            if (word == NULL)
                ERROR_PRINT("out of memory");
            if(rev == 1)
                list_addlast(list, word);
            if(rev == 0)
                list_addfirst(list, word);
        }
    }
}
