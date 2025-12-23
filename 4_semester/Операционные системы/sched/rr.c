#include <time.h>
#include <stdlib.h>
#include <stdio.h>

#include "sched.h"

#define MAX_PROCESSES 100

static int process_count;
static int process_ids[MAX_PROCESSES];
static int current_index;

int sched_init(void)
{
  process_count = 0;
  current_index = 0;
  return 0;
}

void sched_clean(void)
{
  process_count = 0;
  current_index = 0;
}

int add_proc(void)
{
  if (process_count >= MAX_PROCESSES) {
    return -1;
  }
  process_ids[process_count] = process_count;
  return process_ids[process_count++];
}

int sched(int time, int cont)
{
  if (cont == 0 && time != 0) {
    for (int i = current_index; i < process_count - 1; i++) {
      process_ids[i] = process_ids[i + 1];
    }
    process_count--;

    if (current_index >= process_count) {
      current_index = 0;
    }
  } else {
    current_index = (current_index + 1) % process_count;
  }

  if (process_count == 0) {
    return -1;
  }

  return process_ids[current_index];
}

int sched_fin(void)
{
  return 0;
}
