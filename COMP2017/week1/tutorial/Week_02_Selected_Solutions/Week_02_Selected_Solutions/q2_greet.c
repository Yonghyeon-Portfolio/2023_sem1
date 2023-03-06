#include <stdio.h>
#define MAX_LEN (256)

int main(int argc, char **argv)
{
	if (argc >= 2)
	{
		char name[MAX_LEN];
		fgets(name, MAX_LEN, stdin);
		printf("%s %s\n", argv[1], name);
	}
	return 0;
}
