cmake_minimum_required(VERSION 3.5)
project(LUNAR_LANDER LANGUAGES C)
project(LUNAR_LANDER VERSION 0.1)
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED True)

# Adding on some global variables
set(GLOBAL_VAR1 0.001) # This is the discrete time value

#add_executable(LUNAR_LANDER src/hey.c src/engine.c) # My code
add_executable(LUNAR_LANDER src/engine.c src/pubsub.c)
add_executable(PLOT src/pubsub.c src/plotter.c)
#add_executable(KOOLAID src/hey.c)

# Building external library
add_subdirectory(lib/)
target_link_libraries(LUNAR_LANDER PRIVATE Quaternion)
target_link_libraries(LUNAR_LANDER PUBLIC m)
target_include_directories(LUNAR_LANDER PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/lib/Quaternion)

# Solving the issue
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)