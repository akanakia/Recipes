// Console.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "CSVFileParser.h"

void TestCSVFileReader(const std::string& filePath)
{
    CSVFileParser::ReadCSVFile(filePath);
}

int main(int argc, char *argv[])
{
    std::string filePath = std::string(argv[1]);
    TestCSVFileReader(filePath);
}