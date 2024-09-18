#include <stdio.h>
#include <seccomp.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

void init_seccomp() {
    scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_KILL);
    
    if (ctx == NULL) {
        perror("seccomp_init");
        exit(EXIT_FAILURE);
    }

    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(read), 0); 
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(open), 0);  

    if (seccomp_load(ctx) < 0) {
        perror("seccomp_load");
        seccomp_release(ctx);
        exit(EXIT_FAILURE);
    }

    seccomp_release(ctx);
}

int main() {
    
    unsigned char shellcode[512]; 
    printf("Only 'open', 'read' and 'write syscalls are allowed'\n\n");
    printf("Enter your shellcode here: \n");
    
    init_seccomp();
    read(STDIN_FILENO, shellcode, sizeof(shellcode));

    shellcode[strcspn(shellcode, "\n")] = 0;

    printf("Executing your shellcode...\n");

    void (*execute_shellcode)() = (void(*)())shellcode;

    execute_shellcode();

    return 0;
}
