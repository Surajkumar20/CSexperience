#include <stdio.h>
#include <Quaternion.h>
#include "engine.h"
#include "plotter.h"

void cool_test(void);
void logger(struct landerState* input);

int main(void) {
	struct landerState hello;
	int count = 0;
	hello.w = 0; hello.theta = theta_0;
	hello.Izz = 0.023; hello.alpha = 0;

	while (1) {
		if (count == 0) {
			hello.accX = x_dotdot_0;
			hello.velX = x_dot_0;
			hello.posX = x_0;
			hello.accY = y_dotdot_0;
			hello.velY = y_dot_0;
			hello.posY = y_0;
			count = 1;
		}

		else if (count == 1) {
			hello.accX = (1 / m) * FTHST * sin(hello.theta) + hello.accX;
			hello.velX = dT * (hello.accX) + hello.velX;
			hello.posX = dT * (hello.velX) + hello.posX;
			hello.accY = -g - (1 / m) * FTHST * cos(hello.theta) + hello.accY;
			hello.velY = dT * (hello.accY) + hello.accY;
			hello.posY = dT * (hello.velY) + hello.posY;
		}
		//logger(&hello);
		int fifo_id;
		msg message;
		message.posX = hello.posX;
		message.posY = hello.posY;
		publishe(&fifo_id, &message);
		sleep(1);
	}
	return 0;
}

void cool_test(void) {
	double position[3] = {0,0,0};
	Quaternion orientation;
	Quaternion_setIdentity(&orientation);

	// Rotate character to left
	Quaternion rotateLeft;
	double angle = 90.0 / 180.0 * M_PI;
	Quaternion_fromZRotation(angle, &rotateLeft);

	Quaternion_multiply(&rotateLeft, &orientation, &orientation);
	printf("\n\nQuaternions work dude!\n\n");
}

void logger(struct landerState* input) {
	printf("\nPos X: %f & Pos Y: %f\n",input->posX, input->posY);
}