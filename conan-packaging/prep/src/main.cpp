#include <iostream>
#include <argparse/argparse.hpp>
#include "logger.h"


int main(int argc, char* argv[]) {
    argparse::ArgumentParser program("prep");
    program.add_argument("-v", "--verbose")
        .help("increase logging verbosity")
        .default_value(false)
        .implicit_value(true);

    try {
        program.parse_args(argc, argv);
    } catch(const std::exception& err) {
        std::cerr << err.what() << std::endl;
        std::cerr << program;
        std::exit(1);
    }

    Logger logger = Logger();
    if(program.get<bool>("verbose") == true) {
        logger.setLevel(DEBUG);
        logger.debug("Verbosity enabled!");
        
    } else {
        std::cout << "Verbosity not enabled :/" << std::endl;
    }
}

