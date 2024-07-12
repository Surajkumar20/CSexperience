#include <stdio.h>
#include "plotter.h"

void publishe(int* fifo_id, msg* message) {
    mkfifo(FIFO_NAME, 0666);
    *fifo_id = open(FIFO_NAME, O_WRONLY);

    if (*fifo_id == -1) {
        perror("open");
    }

    write(*fifo_id, message, sizeof(*message));
    //printf("Sent message");
    close(*fifo_id);
}

msg* subscribe(int* fifo_id, msg* message) {
    *fifo_id = open(FIFO_NAME, O_RDONLY);
    ssize_t bytes_read = read(*fifo_id, message, sizeof(msg));

    if (bytes_read == 0) {
        printf("Publisher pipe closed.\n\n");
    }

    else if (bytes_read == -1) {
        //perror("read");
    }

    return message;
}