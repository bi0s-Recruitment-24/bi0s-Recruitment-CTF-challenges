#include <stdio.h>
#include <string.h>


int main() {
	char buf[10];
	printf("Bat-Mite has to help Batman find Robin!\nDo you know the spell to summon him?\n>>");
	fgets(buf,100,stdin);
	printf("That wasn't quite right...\n");
	return 0;
}

int call_robin(int a, int b) {
	FILE* file;
	char flag[23];
	if ((a == 0xdeadbeef) && (b == 0xcafebabe)) {
		printf("\nGreat Job!\n");
		file = fopen("flag.txt","r");
		if (file) {
			fread(flag, 23, 1, file);
		} else {
			perror("Read File Error");
		}
		printf("Here's the flag: %s",flag);
		return 0;
	}
	printf("That wasn't quite right...\n");
}
