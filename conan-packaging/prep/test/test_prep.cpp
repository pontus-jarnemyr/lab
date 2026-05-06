#include <catch2/catch_test_macros.hpp>
#include <argparse/argparse.hpp>

TEST_CASE("Basic sanity check") {
    REQUIRE(2 + 2 == 4);
}

TEST_CASE("Argparse works") {
    argparse::ArgumentParser program("prep");

    // Explicitly declare that --foo expects one value
    program.add_argument("--foo").nargs(1);

    // Either of these forms works:
    program.parse_args({"prep", "--foo", "bar"});
    // program.parse_args({"--foo=bar"});

    REQUIRE(program.get<std::string>("--foo") == "bar");
}

