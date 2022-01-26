#include <iostream>
#include "PriorityNode.hpp"
#include "PriorityQueue.hpp"
using namespace std;

int main()
{
    PriorityQueue<string> task;

    task.enqueue("C",1);
    task.enqueue("F",3);
    task.enqueue("E",2);
    task.enqueue("A",0);
    task.enqueue("B",0);
    task.enqueue("D",1);

    PriorityQueue<string> task2 = PriorityQueue<string>(task);
    PriorityNode<string>* pos = task.getFrontPtr();
    for(int x = 1; x <= task.size(); x++)
    {
        cout << pos->getItem() << "\n";
        pos = pos->getNext();
    }
    cout << "\n\n";
    pos = task2.getFrontPtr();
    for(int x = 1; x <= task2.size(); x++)
    {
        cout << pos->getItem() << "\n";
        pos = pos->getNext();
    }

    return 0;
}