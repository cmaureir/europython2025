#include <stdio.h>
#include <stdint.h>

int main(int argc, char *argv[]) {
    uint32_t array[5] = {0, 0, 0, 0, 0};
    for (int idx = 0; idx < 7; idx++) {
        printf("%d: %d\n", idx, array[idx]);
    }
    return 0;
}
