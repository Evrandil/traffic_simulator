cmake_minimum_required(VERSION 4.2)
project(traffic_simulator)

set(CMAKE_CXX_FLAGS "-Wall -Wextra -std=c++23")

add_executable(simulator src/main.cpp src/vehicle/vehicle.cpp src/lane/lane.cpp src/intersection/intersection.cpp)
