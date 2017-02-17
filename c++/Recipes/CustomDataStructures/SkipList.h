#pragma once

#include <list>

#define SAFE_DELETE(x) (if ((x) != NULL) { delete((x)); (x) = NULL; })

namespace CustomDataStructures
{
    template <class T>
    class SkipList
    {
    public:
        SkipList();
        ~SkipList();

        void add(T value);
        T pop();
        void remove(T value);
        unsigned int index_of(T value);
        unsigned int get_size();

    private:
        class SkipNode
        {
        public:
            inline SkipNode()
            {
                this->value = NULL;
                this->links = new std::list<SkipNode *>();
                this->size = 0;
            }

            inline SkipNode(T value, unsigned int size)
            {
                this->value = value;
                this->links = new std::list<SkipNode *>(size);
                this->size  = size;
            }
            inline ~SkipNode()
            {
                SAFE_DELETE(this->links);
            }

            std::list<SkipNode *> links;
            T value;
            unsigned int size;
        };

        SkipNode *find(T value);

        SkipNode *head, *tail;
        unsigned int size;
    };
}