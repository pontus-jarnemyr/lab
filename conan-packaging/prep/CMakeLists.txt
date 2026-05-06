cmake_minimum_required(VERSION 3.12)
project(AoC_Prep)

# Tell CMake to look in Conan's generated files
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})
find_package(argparse REQUIRED)
find_package(Catch2 REQUIRED)
find_package(logger REQUIRED)

add_executable(prep src/main.cpp)
target_link_libraries(prep argparse::argparse logger::logger)

# Add test executable
add_executable(tests test/test_prep.cpp)
target_link_libraries(tests PRIVATE Catch2::Catch2WithMain argparse::argparse)

include(CTest)
include(Catch)
catch_discover_tests(tests)
