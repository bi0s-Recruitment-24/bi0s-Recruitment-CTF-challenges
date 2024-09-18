#include <stdio.h>
#include <string.h>

void print_flag() {
    FILE *file = fopen("flag.txt", "r");
    if (file == NULL) {
        printf("Error opening flag.txt\n");
        return;
    }

    char flag[256];
    if (fgets(flag, sizeof(flag), file) != NULL) {
        printf("Congratulations! You overflowed me.\n");
        printf("FLAG: %s", flag);
    } else {
        printf("Error reading flag.txt\n");
    }

    fclose(file);
}

void vulnerable_function() {
    char buffer[126];
    int val = 0xdeadbeef;
    printf("Enter input: ");
    gets(buffer);
    if(val != 0xdeadbeef){
        print_flag();
    }
    else{
        printf("Input received: %s\n", buffer);
        printf("Good job, bye\n");
    }
}

int main() {
    vulnerable_function();
    return 0;
}
