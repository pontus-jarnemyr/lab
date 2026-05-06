#include "logger.h"


void Logger::log(LogLevel level, const std::string &message) {
    if(level < this->level) {
        return;
    }
    std::ostringstream logEntry;
    logEntry << "[" << this->levelToString(level) << "]: " << message << std::endl; 
    std::cout << logEntry.str();
    if(this->logFile.is_open()) {
        this->logFile << logEntry.str();
        this->logFile.flush();
    }
}


void Logger::debug(const std::string &message) {
    this->log(DEBUG, message);
}

void Logger::info(const std::string &message) {
    this->log(INFO, message);
}

void Logger::warning(const std::string &message) {
    this->log(WARNING, message);
}

void Logger::error(const std::string &message) {
    this->log(ERROR, message);
}

void Logger::critical(const std::string &message) {
    this->log(CRITICAL, message);
}
