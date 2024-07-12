#ifndef PLOTTER_H
#define PLOTTER_H

#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

#define FIFO_NAME "data_pipe"

typedef struct {
    float posX;
    float posY;
} msg;

void publishe(int* fifo_id, msg* message);
msg* subscribe(int*, msg*);

#endif