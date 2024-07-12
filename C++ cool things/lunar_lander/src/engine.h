#ifndef ENGINE_H
#define ENGINE_H

// Basic Game State
struct landerState {
	float posX;
	float posY;
	float theta;

	float velX;
	float velY;
	float w;

	float accX;
	float accY;
	float alpha;

	float Izz;
};

#ifndef M_PI
    #define M_PI (3.14159265358979323846)
#endif

// Initializing Beginning Game State
// Using normal physics S.I. units
// X-direction
float x_0 = 3;
float x_dot_0 = 0.5;
float x_dotdot_0 = 0.3;

// Y-direction
float y_0 = 2;
float y_dot_0 = 0.2;
float y_dotdot_0 = 3;

float theta_0 = 90.0 * M_PI / 180.0; // in radians son
float g = 2;
float m = 4.5;
float dT = 0.1; // 1 ms physics tick
float FTHST = 20;  // in newtons

#endif