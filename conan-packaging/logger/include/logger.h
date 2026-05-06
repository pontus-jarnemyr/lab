#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

enum LogLevel { 
    DEBUG = 10, 
    INFO = 20, 
    WARNING = 30, 
    ERROR = 40, 
    CRITICAL = 50
};


class Logger {
public:
    Logger() {}
    Logger(const string& filename) {
        this->logFile.open(filename);
        if(!this->logFile.is_open()) {
            cerr << "Failed to open file " << filename << endl;
        }
    }

    ~Logger() {
        this->logFile.close();
    }

    void log(LogLevel level, const string& message);
    void setLevel(LogLevel level) {
        this->level = level;
    }
    void debug(const string& message);
    void info(const string& message);
    void warning(const string& message);
    void error(const string& message);
    void critical(const string& message);

private:
    ofstream logFile;
    LogLevel level = INFO;

    string levelToString(LogLevel level) {
        switch(level) {
            case DEBUG:
                return "DEBUG";
            case INFO:
                return "INFO";
            case WARNING:
                return "WARNING";
            case ERROR:
                return "ERROR";
            case CRITICAL:
                return "CRITICAL";
            default:
                return "UNKNOWN";
        }
    }
};
