#include <stdio.h>
#include <sys/mman.h>
#include <unistd.h>
#include <limits.h>
#include <stdlib.h>

void __attribute__((section(".upx"))) hello_world()
{
  printf("Hello, world\n");
}

extern char upx_end;
extern char upx_start;

void apply_mask(char *start, char *end, const char mask, size_t mask_len) {
  for (size_t i = 0; start + i < end; i++) {
      start[i] ^= mask;
  }
}

int main(int argc, char *argv[])
{
  int page_size = sysconf(_SC_PAGE_SIZE);
  printf("page size: %d\n", page_size);
  printf("start = %p , end = %p\n", &upx_start, &upx_end); 
  void *ptr;
  ptr = &upx_start;

  void *page_start = (void *)((size_t)&upx_start & ~(page_size - 1));
  size_t protect_size = (&upx_end - (char *)page_start + page_size - 1) & ~(page_size - 1);
  
  if (mprotect(page_start, protect_size, PROT_READ | PROT_WRITE | PROT_EXEC) == -1) {
      perror("mprotect");
      return 1;
  }
  
  const char mask = 0xAA;
  apply_mask(&upx_start, &upx_end, mask, sizeof(mask));
  
  hello_world();
  
  return 0;
}
