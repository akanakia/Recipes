#include "stdafx.h"
#include "TriangularArray.h"


template <class T>
CustomDataStructures::TriangularArray<T>::TriangularArray(unsigned int n)
{
    this.n = n;
}

template <class T>
CustomDataStructures::TriangularArray<T>::~TriangularArray()
{
}

template<class T>
T at (unsigned int d1, unsigned int d2)
{
    if (d1 < d2) return ((d1 * n) - (d1 * (d1 + 1) / 2)) + (d2 - d1) - 1;
    if (d1 > d2) return ((d2 * n) - (d2 * (d2 + 1) / 2)) + (d1 - d2) - 1;

    return NULL;
}
