# include <stdio.h>
# include <string.h>

int main() {
	char buf[10];
	char inv[10] = "GUNS";
	FILE * file;
	char flag[40];
	printf("Bat-Mite has swapped out all of Batman's batarangs with guns...\nDo you remember the spell to undo what you did\n");
	printf("[INVENTORY] : %s\n>> ",inv);
	fgets(buf,50,stdin);
	printf("\n[INVENTORY] : %s\n",inv);
	if (strstr(inv,"BATARANG")) {
		printf("Great Job!\n");
		file = fopen("flag.txt","r");
		if (file) {
			fread(flag, 40, 1, file);
		} else {
			perror("Read File Error");
		}
		printf("Here's the flag: %s",flag);
		return 0;
	};
	printf("That didn't work...You're gonna have some explaining to do...\n");
	return 0;
}
