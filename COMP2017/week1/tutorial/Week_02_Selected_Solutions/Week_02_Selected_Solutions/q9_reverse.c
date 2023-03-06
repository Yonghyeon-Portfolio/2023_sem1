#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_LEN (100)

void reverse(char *a, size_t length)
{

	for (int i = 0; i < length / 2; i++)
	{ // In-place reverse
		char temp = a[i];
		a[i] = a[length - i - 1];
		a[length - i - 1] = temp;
	}
}

int main()
{
	char word[MAX_LEN];

	while (fgets(word, MAX_LEN, stdin))
	{
		word[strlen(word) - 1] = '\0'; // Replaces \n with \0
		reverse(word, strlen(word));   // You can assume 100
		printf("%s\n", word);
	}
}
