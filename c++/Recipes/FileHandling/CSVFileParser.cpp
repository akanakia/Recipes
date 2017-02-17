#include "CSVFileParser.h"

#include <iostream>
#include <fstream>
#include <vector>

#define SAFE_DELETE(x) if ((x) != NULL) { delete (x); (x) = NULL; }

std::vector<std::string> *tokenize(const std::string& str, const char& del)
{
    std::vector<std::string> *tokenList = new std::vector<std::string>();
    size_t start_loc = 0;
    size_t end_loc = str.find(del);

    // If no delimiters are found in the string, just return the whole string.
    if (end_loc == std::string::npos)
    {
        tokenList->push_back(std::string(str));
        return tokenList;
    }

    while (end_loc != std::string::npos)
    {
        std::string token = std::string(str, start_loc, end_loc - start_loc);
        tokenList->push_back(token);
        start_loc = end_loc + 1;
        end_loc = str.find(del, start_loc);
    }

    if (start_loc < str.length() - 1)
    {
        std::string token = std::string(str, start_loc, str.length() - 1);
        tokenList->push_back(token);
    }

    return tokenList;
}

void CSVFileParser::ReadCSVFile(const std::string& filePath, const char& del)
{
    std::ifstream freader;
    freader.open(filePath, std::ios::in);

    while (freader.good())
    {
        std::string line;
        std::getline(freader, line);
        std::vector<std::string> *tokens = tokenize(line, del);
        for (std::string tok : *tokens)
        {
            std::cout << tok << ' ';
        }

        SAFE_DELETE(tokens);
        std::cout << std::endl;
    }
}

void CSVFileParser::WriteCSVFile(const std::string& filePath)
{

}
