import java.util.*;

public class LinkedListDataStructure {
    public static void main(String[] args) {
        LinkedList<String> linkedList = new LinkedList<String>();
        
        // linkedList.push("A");
        // linkedList.push("B");
        // linkedList.push("C");
        // linkedList.push("D");
        // linkedList.push("F");
        // linkedList.pop(); // pops the top of the list since the list reads [F, D, C, B, A]

        // Using a LinkedList to mimic a stack/queue
        linkedList.offer("A");
        linkedList.offer("B");
        linkedList.offer("C");
        linkedList.offer("D");
        linkedList.offer("F");
        // linkedList.poll();

        linkedList.add(4, "E");
        linkedList.remove("E");

        // System.out.println(linkedList.indexOf("F"));

        System.out.println(linkedList.peekFirst()); // Prints first element in the list
        System.out.println(linkedList.peekLast()); // Prints last element in the list
        linkedList.addFirst("0"); // Adds an element at index 0 of the list and shifts all of the other elements by 1
        linkedList.addLast("G"); // Adds an element at the last index

        String first = linkedList.removeFirst();
        String last = linkedList.removeLast();

        System.out.println(linkedList);
    }
}

/*
LinkedLists = stores Nodes in 2 parts (data + address)
                    Nodes are in non-consecutive memory locations
                    Elements are linked using pointers


Singly Linked List
                    Node                Node              Node
            (data | address) -> (data | address) -> (data | address)
Doubly Linked List
                    Node                                Node                        Node
            (address | data | address) <-> (address | data | address) <-> (address | data | address)

Advantages?
1. Dynamic Data Structure (allocates needed memory while running)
2. Insertion and Deletion of Nodes is easy. O(1)
3. No/Low memory waste

Disadvantages?
1. Greater memory usage (additional pointer)
2. No random access of elements (no index [i])
3. Accessing/searching elements is more time consuming. O(n)

Uses?
1. Implement Stacks/Queues
2. GPS navigation
3. Music playlist

small data set: LinkedList = BAD
large data ste + lots of searching: LinkedList = BAD
large data set + lost of inserting/dleeting: LinkedList = GOOD
*/