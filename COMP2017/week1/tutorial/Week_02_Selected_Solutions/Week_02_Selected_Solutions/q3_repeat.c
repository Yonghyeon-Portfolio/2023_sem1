#include <stdio.h>
#define MAX_LEN (100)

int main()
{
  char word[MAX_LEN];
  while (fgets(word, MAX_LEN, stdin))
  {
    printf("%s\n", word);
  }
  return 0;
}
