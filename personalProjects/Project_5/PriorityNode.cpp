/** 
Hans D Chaudry 
CSCI 23500 
Oyewole Oyekoya
Project 5
Completed on Dec 4, 2021
Implement PriorityNode.hpp
*/

#include "PriorityNode.hpp"
#include <iostream>
using namespace std;

/*DEFAULT CONSTRUCTOR*/
template<typename ItemType>
PriorityNode<ItemType>::PriorityNode()
{
    next_ = nullptr;
}

/*PARAMETERIZED CONSTRUCTORS*/
template<typename ItemType>
PriorityNode<ItemType>::PriorityNode(const ItemType& an_item)

{
    item_ = an_item;
    next_ = nullptr;
}

template<typename ItemType>
PriorityNode<ItemType>::PriorityNode(const ItemType& an_item, int priority)
{
    item_ = an_item;
    priority_ = priority;
    next_ = nullptr;
}

template<typename ItemType>
PriorityNode<ItemType>::PriorityNode(const ItemType& an_item, int priority, PriorityNode<ItemType>* next_node_ptr)
{
    item_ = an_item;
    priority_ = priority;
    next_ = next_node_ptr;
}

//SETTERS
/**
 * @brief set item_ equal to an_item
 * @param an_item is th new item that 
 */
template<typename ItemType>
void PriorityNode<ItemType>::setItem(const ItemType& an_item)
{
    item_ = an_item;
}

/**
 * @brief set priority_ equal to priority
 * @param priority is the priority level being assigned to the current node
 */
template<typename ItemType>
void PriorityNode<ItemType>::setPriority(const int priority)
{
    priority_ = priority;
}

/**
 * @brief set next_ euqal to next_node_ptr
 * @param next_node_ptr is the next pointer being assigned to this node
 */
template<typename ItemType>
void PriorityNode<ItemType>::setNext(PriorityNode<ItemType>* next_node_ptr)
{
    next_ = next_node_ptr;
}

//GETTERS
//return item_
template<typename ItemType>
ItemType PriorityNode<ItemType>::getItem() const
{
    return item_;
}

//return priority_
template<typename ItemType>
int PriorityNode<ItemType>::getPriority() const
{
    return priority_;
}

//return next_
template<typename ItemType>
PriorityNode<ItemType>* PriorityNode<ItemType>::getNext() const
{
    return next_;
}