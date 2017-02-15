#pragma once

namespace CustomDataStructures
{
    template <class T>
    class TriangularArray
    {
    public:
        TriangularArray(unsigned int n);

        ~TriangularArray();

        T& operator[] (unsigned int d1, unsigned int d2);

    private:
        unsigned int n;
    };
}
