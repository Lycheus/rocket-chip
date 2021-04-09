#include <stdint.h>

void bon();
void boff();
void store8(uint64_t *ptr, uint64_t value);
void store4(uint32_t *ptr, uint32_t value);
void store2(uint16_t *ptr, uint16_t value);
void store1( uint8_t *ptr,  uint8_t value);
uint64_t load8(uint64_t *ptr);
uint32_t load4(uint32_t *ptr);
uint16_t load2(uint16_t *ptr);
 uint8_t load1( uint8_t *ptr);
void *set_bound(void *ptr, void *base, void *bound);
void *set_bound_4(void *ptr, void *base);
