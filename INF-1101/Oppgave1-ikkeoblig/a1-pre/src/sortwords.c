#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "list.h"
#include "common.h"

// int compare_func(void *e1, void *e2){
    // char *word1 = (char*)(e1);
    // char *word2 = (char*)(e2);
    // return strcmp(word1, word2);
// };
void tokenize_file(FILE *file, list_t *list, int rev);

int main(int argc, char **argv)
{
    printf("Starting...\n");
    list_t *result_list = list_create();
    FILE *fp;

    fp = fopen("/home/eskil/Desktop/Eskil/2. semester/INF-1101/Oppgave 1 (ikke oblig)/a1-pre/data/hamlet.txt", "r");
    tokenize_file(fp, result_list, 1);
    fclose(fp);
    printlist(result_list);
    printf("\n\n");
    printf("End on process. Have a great day :)");
 
    return 0;
}
