#include "test.h"
#include <stdint.h>
#include <stdio.h>

int main() {
    void *sp;
    asm("add %0, sp, zero" : "=r"(sp));

    // might not work
    bon(sp+0x1000);

    uint64_t array[4] = {0};
    uint64_t *array_ptr = set_bound(array, array, array+4);

    printf("test begin...\n");
    /*
    store8((uint64_t *)((*array_dptr) + 0), 1);
    store4((uint32_t *)((*array_dptr) + 1), 2);
    store2((uint16_t *)((*array_dptr) + 2), 3);
    store1((uint8_t  *)((*array_dptr) + 3), 4);

    uint64_t a = load8((uint64_t *)(array_ptr + 0));
    uint32_t b = load4((uint32_t *)(array_ptr + 1));
    uint16_t c = load2((uint16_t *)(array_ptr + 2));
    uint8_t  d = load1((uint8_t  *)(array_ptr + 3));
    */
    kenny1(array_ptr, &array_ptr);

    printf("test finished\n");

    //boff();    
    return 0;
}
