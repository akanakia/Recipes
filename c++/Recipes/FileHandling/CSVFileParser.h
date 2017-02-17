#pragma once

#include <string>

class CSVFileParser
{
public:
    static void ReadCSVFile(const std::string& filePath, const char& del = ',');
    static void WriteCSVFile(const std::string& filePath);
};

class CSVData
{
public:

};