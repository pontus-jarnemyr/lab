cmake_minimum_required(VERSION 3.15)
project(logger CXX)

add_library(logger src/logger.cpp)
target_include_directories(logger PUBLIC include)

set_target_properties(logger PROPERTIES PUBLIC_HEADER "include/logger.h")
install(TARGETS logger)
