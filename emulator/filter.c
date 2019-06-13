#include <stdio.h>
#include <stdlib.h>

int main() {
    char *line = malloc(1024);
    size_t size;

    while (getline(&line, &size, stdin) != -1) {
        if (line[0] != '[')
            printf("%s", line);
    }

    free(line);
}
