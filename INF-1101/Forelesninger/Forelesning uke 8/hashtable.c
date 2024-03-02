#include <stdlib.h>
#include <stdio.h>

typedef struct data_t DataItem;
struct DataItem{
    int data;
    int key;
};

typedef struct table_t Table;
struct Table{
    data_t *DataItem;

}

int hashcode (table_t *table, int key){
    return key % table->size;
}
