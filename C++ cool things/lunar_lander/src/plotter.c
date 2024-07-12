#include <stdio.h>
#include "plotter.h"

int main(void) {
    msg message;
    msg* rcvd_msg;
    int fifo_id = open(FIFO_NAME, O_RDONLY);

    while (1) {
        rcvd_msg = subscribe(&fifo_id, &message);
        printf("Received the information. PosX: %f, PosY: %f\n\n", rcvd_msg->posX, rcvd_msg->posY);
    }

    close(fifo_id);
    return 0;
}