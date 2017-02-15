#pragma once

#include <list>

template <class T>
class SkipList
{
public:
    SkipList();
    ~SkipList();

    void push(T value);
    T pop();

private:
    template <class T>
    class SkipNode
    {
    private:
        std::list<SkipNode> links;
        T value;

    public:
        SkipNode();
        ~SkipNode();
    };
};

