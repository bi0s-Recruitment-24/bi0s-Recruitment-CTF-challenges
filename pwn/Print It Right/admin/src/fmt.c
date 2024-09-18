#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
	char buf[50];

	char *inp;

	FILE *f = fopen("flag.txt","r");
	if (f == NULL) {
		printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
		exit(0);
	}
	fgets(buf,50,f);

	inp = &buf;

	char name[50];
	puts("Enter your name");
	fgets(name,50,stdin);
	puts("The name you entered is: ");
	printf(name);
}