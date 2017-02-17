#include "stdafx.h"
#include "SkipList.h"

template <class T>
CustomDataStructures::SkipList<T>::SkipList()
{
    this->head = new SkipNode();
    this->tail = new SkipNode();
    this->size = 0;
}

template <class T>
CustomDataStructures::SkipList<T>::~SkipList()
{
    SAFE_DELETE(this->head);
    SAFE_DELETE(this->tail);
}

template<class T>
void CustomDataStructures::SkipList<T>::add(T value)
{
    SkipNode *new_node = new SkipNode(value);
    
}

template<class T>
T CustomDataStructures::SkipList<T>::pop()
{
    return T();
}

template<class T>
void CustomDataStructures::SkipList<T>::remove(T value)
{
}

template<class T>
unsigned int CustomDataStructures::SkipList<T>::index_of(T value)
{
    return 0;
}

template<class T>
unsigned int CustomDataStructures::SkipList<T>::get_size()
{
    return this->size;
}

template<class T>
typename CustomDataStructures::SkipList<T>::SkipNode *CustomDataStructures::SkipList<T>::find(T value)
{
    std::list<SkipNode *> head_list = this->head->links;
    return NULL;
}
