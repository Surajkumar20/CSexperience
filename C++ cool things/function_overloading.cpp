#include <iostream>

class Pop {
    public:
        int ft(int a) {
            return(3*a);
        }

        int ft(int a, int b) {
            return(3*a*b);
        }

        int ft(int a, int b, int c) {
            return(3*a*b*c);
        }};

int main(void) {
    Pop first_class;
    std::cout << "One arg version: " << first_class.ft(3) << std::endl;
    std::cout << "Two arg version: " << first_class.ft(3,3) << std::endl;
    std::cout << "Three arg version: " << first_class.ft(1,2,3) << std::endl;

    return(0);
}

