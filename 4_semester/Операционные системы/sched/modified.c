#include <time.h>
#include <stdlib.h>
#include <stdio.h>

#include "sched.h"

static int process_count;
static int last_process;
static int *process_time = NULL;
static int *number_processes = NULL;
static int f = 0;
static int ind = 0;

int sched_init(void)
{
    return 0;
}

void sched_clean(void)
{
    if (process_time != NULL) {
        int i, j;
        for (i = 0; i < process_count - 1; i++) {
            for (j = i + 1; j < process_count; j++) {
                if (process_time[i] < process_time[j]) {
                    int x = process_time[i];
                    process_time[i] = process_time[j];
                    process_time[j] = x;
                    
                    x = number_processes[i];
                    number_processes[i] = number_processes[j];
                    number_processes[j] = x;
                }
                f = 1;
            }
            FILE* fl = fopen("quants.txt", "w");
            for (int i = 0; i < process_count; i++) {
                fprintf(fl, "%d %d\n", number_processes[i], process_time[i]);
            }
            fclose(fl);
        }
    }
    process_count = 0;
}

int add_proc(void)
{
    int *new_time = realloc(process_time, (process_count + 1) * sizeof(int));
    if (f == 0) {
        int *new_number = realloc(number_processes, (process_count + 1) * sizeof(int));
        if (new_number == NULL) {
            perror("realloc failed for number_processes");
            exit(1);
        }
        number_processes = new_number;
        number_processes[process_count] = process_count;
        if (new_time == NULL) {
            perror("realloc failed for process_time");
            exit(1);
        }
        process_time = new_time;
        process_time[process_count] = 0;
        last_process = process_count + 1;
    } else {
        ind = process_count + 1;
        last_process = number_processes[ind];
    }
    return (process_count++);
}

int sched(int time, int cont)
{
    if (f == 0) {
        process_time[last_process] += time;
    }
    if (cont == 0) {
        if (f == 0) {
            last_process--; 
        } else {
            ind = ind - 1;
            if (ind < 0) {
                last_process = -1;
            } else {
                last_process = number_processes[ind];
            }
        }
    }
    return last_process;
}

int sched_fin(void)
{
    return 0;
}