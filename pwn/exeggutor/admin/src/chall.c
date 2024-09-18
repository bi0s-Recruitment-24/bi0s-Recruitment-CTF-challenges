#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>


int main() {
    
    unsigned char shellcode[512]; 
    printf("All syscalls are allowed!'\n\n");
    printf("Enter your shellcode here: \n");
    
    read(STDIN_FILENO, shellcode, sizeof(shellcode));

    shellcode[strcspn(shellcode, "\n")] = 0;

    printf("Executing your shellcode...\n");

    void (*execute_shellcode)() = (void(*)())shellcode;

    execute_shellcode();

    return 0;
}
