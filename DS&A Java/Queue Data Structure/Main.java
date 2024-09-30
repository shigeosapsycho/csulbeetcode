import java.util.Queue;
import java.util.LinkedList;

public class Main{

    public static void main(String[] args){
        // Queue = FIFO data structure. First-in First-Out (like a line of people)
        //              A collection designed for holding elements prior to processing
        //              Linear data structure

        //              add = enque, offer()
        //              remove = dequeue, poll()

        Queue<String> queue = new LinkedList<String>();

        queue.offer("Karen");
        queue.offer("Chad");
        queue.offer("Steve");
        queue.offer("Harold");

        System.out.println(queue);
    }
}