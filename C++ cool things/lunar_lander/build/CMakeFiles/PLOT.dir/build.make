# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/gic/Projects/lunar_lander

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/gic/Projects/lunar_lander/build

# Include any dependencies generated for this target.
include CMakeFiles/PLOT.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/PLOT.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/PLOT.dir/flags.make

CMakeFiles/PLOT.dir/src/pubsub.c.o: CMakeFiles/PLOT.dir/flags.make
CMakeFiles/PLOT.dir/src/pubsub.c.o: ../src/pubsub.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/gic/Projects/lunar_lander/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/PLOT.dir/src/pubsub.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/PLOT.dir/src/pubsub.c.o   -c /home/gic/Projects/lunar_lander/src/pubsub.c

CMakeFiles/PLOT.dir/src/pubsub.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/PLOT.dir/src/pubsub.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/gic/Projects/lunar_lander/src/pubsub.c > CMakeFiles/PLOT.dir/src/pubsub.c.i

CMakeFiles/PLOT.dir/src/pubsub.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/PLOT.dir/src/pubsub.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/gic/Projects/lunar_lander/src/pubsub.c -o CMakeFiles/PLOT.dir/src/pubsub.c.s

CMakeFiles/PLOT.dir/src/plotter.c.o: CMakeFiles/PLOT.dir/flags.make
CMakeFiles/PLOT.dir/src/plotter.c.o: ../src/plotter.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/gic/Projects/lunar_lander/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/PLOT.dir/src/plotter.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/PLOT.dir/src/plotter.c.o   -c /home/gic/Projects/lunar_lander/src/plotter.c

CMakeFiles/PLOT.dir/src/plotter.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/PLOT.dir/src/plotter.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/gic/Projects/lunar_lander/src/plotter.c > CMakeFiles/PLOT.dir/src/plotter.c.i

CMakeFiles/PLOT.dir/src/plotter.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/PLOT.dir/src/plotter.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/gic/Projects/lunar_lander/src/plotter.c -o CMakeFiles/PLOT.dir/src/plotter.c.s

# Object files for target PLOT
PLOT_OBJECTS = \
"CMakeFiles/PLOT.dir/src/pubsub.c.o" \
"CMakeFiles/PLOT.dir/src/plotter.c.o"

# External object files for target PLOT
PLOT_EXTERNAL_OBJECTS =

../bin/PLOT: CMakeFiles/PLOT.dir/src/pubsub.c.o
../bin/PLOT: CMakeFiles/PLOT.dir/src/plotter.c.o
../bin/PLOT: CMakeFiles/PLOT.dir/build.make
../bin/PLOT: CMakeFiles/PLOT.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/gic/Projects/lunar_lander/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking C executable ../bin/PLOT"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/PLOT.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/PLOT.dir/build: ../bin/PLOT

.PHONY : CMakeFiles/PLOT.dir/build

CMakeFiles/PLOT.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/PLOT.dir/cmake_clean.cmake
.PHONY : CMakeFiles/PLOT.dir/clean

CMakeFiles/PLOT.dir/depend:
	cd /home/gic/Projects/lunar_lander/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/gic/Projects/lunar_lander /home/gic/Projects/lunar_lander /home/gic/Projects/lunar_lander/build /home/gic/Projects/lunar_lander/build /home/gic/Projects/lunar_lander/build/CMakeFiles/PLOT.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/PLOT.dir/depend

