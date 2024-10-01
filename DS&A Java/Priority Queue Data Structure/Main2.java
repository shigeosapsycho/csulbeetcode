import java.util.*;

public class Main2{

    public static void main(String[] args) {
            // Priority Queue = A FIFO data structure that serves elements
            // With the highest priorities first
            // Before elements with lower priority
            
        // Queue<Double> queue = new PriorityQueue<>(); // Organizes it in ascending order, smallest to biggest
        // Queue<Double> queue = new PriorityQueue<>(Collections.reverseOrder()); // Organizes it in descending order, biggest to smallest
        // Queue<String> queue = new PriorityQueue<>(); // For alphabetical order
        Queue<String> queue = new PriorityQueue<>(Collections.reverseOrder()); // For reverse alphabetical order

        // For lines 10 and 11 only
        // queue.offer(3.0);
        // queue.offer(2.5);
        // queue.offer(4.0);
        // queue.offer(1.5);
        // queue.offer(2.0);

        // For line 12 and 13 only
        queue.offer("B");
        queue.offer("C");
        queue.offer("A");
        queue.offer("F");
        queue.offer("D");

        while(!queue.isEmpty()){
            System.out.println(queue.poll());
        }
    }
}