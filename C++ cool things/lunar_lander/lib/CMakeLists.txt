cmake_minimum_required(VERSION 3.0)

project(Quaternion)

set(library_sources
    Quaternion/Quaternion.c
)

add_library(Quaternion SHARED ${library_sources})