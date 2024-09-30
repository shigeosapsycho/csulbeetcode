import java.util.Queue;
import java.util.LinkedList;

public class Main1{

    public static void main(String[] args){
        // Queue = FIFO data structure. First-in First-Out (like a line of people)
        //              A collection designed for holding elements prior to processing
        //              Linear data structure

        //              add = enque, offer()
        //              remove = dequeue, poll()

        Queue<String> queue = new LinkedList<String>();

        // System.out.println(queue.isEmpty()); // Will print True

        queue.offer("Karen");
        queue.offer("Chad");
        queue.offer("Steve");
        queue.offer("Harold");

        // System.out.println(queue.isEmpty()); // Will print False
        // System.out.println(queue.size()); // Will print 4
        // System.out.println(queue.contains("Harold")); // Prints true but does not give the index

        // System.out.println(queue.peek());
        // queue.poll(); // Pulls Karen
        // queue.poll(); // Pulls Chad
        // queue.poll(); // Pulls Steve
        // queue.poll(); // Pulls Harold
        // queue.poll(); // Pulls nothing but will not cause an exception error
        // queue.elemnent(); // will cause an exception error though

        System.out.println(queue);

        // When are queues useful?
    
        // 1. Keyboard Buffer (letters should appear on the screen in the order they're pressed)
        // 2. Printer queue (print jobs should be completed in order)
        // 3. Used in LinkedLists, PriorityQueues, breadth-first search
    }
}