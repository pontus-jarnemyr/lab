# Advent of code 2025

TODO

## Building projects

I use CMake to build all "projects" (or all days). I've also opted to use a
few external packages/libraries for handling e.g. CLI arguments and testing,
and a few packages for e.g. logging. To manage these, I use
[Conan](https://docs.conan.io/2/index.html).

### Installing Conan

To install Conan, run the following:

```sh
# create and activate virtual environment
python3 -m venv venv
source venv/bin/activate
# install conan
pip install conan
# let conan set up your computer's profile
conan profile detect --exist-ok
```

All projects use the same external dependencies, which are defined in
[conanfile.txt](./conanfile.txt).

### Installing CMake

TODO

### Creating the logger

The [logger](./logger/README.md) package is created specifically for this
project and not uploaded to any Conan repository. To build it, follow these
steps:

```sh
cd logger/
conan create .
```

This builds the logger library and adds it to your Conan cache, which then
makes it possible to add it as a dependency for our other projects. Easy!

### Example

Let's build the [prep](./prep/) project! Do the following:

```sh
# switch to prep directory
cd prep/
# install dependencies
conan install .. --output-folder=build --build=missing
# build the project
cd build/
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build .
```

You should now have an executable called `prep` in your build directory! To
run the tests, simply run `ctest` in the build directory.
