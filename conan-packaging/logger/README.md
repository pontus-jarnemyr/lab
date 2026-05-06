# Logger

This simple logger is inspired by Python's logging module. There are five logger
levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.

Here's how you can use the logger:

```cpp
#include "logger.h"

int main() {
    Logger logger = Logger();
    // By default, messages of level INFO and higher are enabled
    logger.info("Hello!");
    // This won't be logged since we use the default INFO level
    logger.debug("Greetings");
    // change logger threshold
    logger.setLevel(WARNING);
    // This won't be logged since we changed the threshold
    logger.info("Hello :)");
    // You can also use logger.log() and pass the log level explicitly
    logger.log(ERROR, "This is an error message");
    // The above is equivalent to
    logger.error("This is an error message");
}
```
