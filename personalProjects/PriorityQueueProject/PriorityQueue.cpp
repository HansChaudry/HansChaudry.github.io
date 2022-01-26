/** 
Hans D Chaudry 
CSCI 23500 
Oyewole Oyekoya
Project 5
Completed on Dec 4, 2021
Implement PriorityQueue.hpp with the help of PriorityNode.hpp
*/

#include "PriorityQueue.hpp"
#include "PriorityNode.hpp"
#include <iostream>
using namespace std;

/*Default Constructor*/
template<typename ItemType>
PriorityQueue<ItemType>::PriorityQueue()
{
    item_count = 0;
    front_ = nullptr;
    back_ = nullptr;
}

/*Copy Constructor*/
/**
 * @brief Construct a new Priority Queue object that is a deep copy of a_priority_queue
 * @param a_priority_queue the queue that is being copied
 */
template<typename ItemType>
PriorityQueue<ItemType>::PriorityQueue(const PriorityQueue<ItemType>& a_priority_queue)
{   
    item_count = 0;
    PriorityNode<ItemType>* next = a_priority_queue.getFrontPtr();
    while(item_count <= a_priority_queue.size()-1)
    {
        enqueue(next->getItem(), next->getPriority());
        next = next->getNext();
    }
}

/*Destructor*/
template<typename ItemType>
PriorityQueue<ItemType>:: ~PriorityQueue()
{
    while (!isEmpty())
    {
        dequeue();
    }
    
}

/**
 * @brief add an item to the queue. items must be arranged by priority.
 * case 1: Add item with the queue is empty
 * case 2: Add to the front when the queue is not empty
 * case 3: Add beteen two nodes
 * case 4: add to the back
 * @param new_entry the item being added to the queue
 * @param priority the priority of the new_entry
 */
template<typename ItemType>
void PriorityQueue<ItemType>::enqueue(const ItemType& new_entry, int priority)
{   
    PriorityNode<ItemType>* newNode = new PriorityNode<ItemType>(new_entry, priority);

    if(item_count == 0)//case 1
    {
        front_ = newNode;
        back_ = newNode; 
    }
    else if (item_count > 0 and front_->getPriority() > priority)//case 2 
    {
        newNode->setNext(front_);
        front_ = newNode;
    }
    else 
    {
        PriorityNode<ItemType>* curr = front_;
        //keeo navigating trough the linked list to find the node that comes before the new node 
        while(curr->getNext() != nullptr and curr->getNext()->getPriority() <= priority)
        {
            curr = curr->getNext();
        }
        if(curr != back_)//case 3
        {
            newNode->setNext(curr->getNext());
            curr->setNext(newNode);
        }
        else//case 4
        {
            curr->setNext(newNode);
            back_ = newNode;
        }
    }   
    item_count++;
}

/**
 * @brief remove the first item in the queue. stops if queue is empty
 * sets front_ and back_ to nullptr if queue is empty after removal of an item
 */
template<typename ItemType>
void PriorityQueue<ItemType>::dequeue()
{
    if (isEmpty()){
        return;
    }
    PriorityNode<ItemType>* temp = front_;
    front_ = front_->getNext();//front_ nowpoints to the item after the first item
    delete temp;
    temp = nullptr;
    item_count--;
    if(item_count == 0)
        back_ = nullptr;
}

//return the the first item in the queue
template<typename ItemType>
ItemType PriorityQueue<ItemType>::front() const
{
    return front_->getItem();
}

//return the pointer to the first item in the queue(front_)
template<typename ItemType>
PriorityNode<ItemType>* PriorityQueue<ItemType>::getFrontPtr() const
{
    return front_;
}

//return item_count
template<typename ItemType>
int PriorityQueue<ItemType>::size() const
{
    return item_count;
}

//returns true is list empty, and false if it's not
template<typename ItemType>
bool PriorityQueue<ItemType>::isEmpty() const

{
    return item_count == 0;
}