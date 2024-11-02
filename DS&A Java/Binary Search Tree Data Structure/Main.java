public class Main {
    
    public static void main(String[] args) {

        BinarySearchTree tree = new BinarySearchTree();

        tree.insert(new Node(5));
        tree.insert(new Node(1));
        tree.insert(new Node(9));
        tree.insert(new Node(2));
        tree.insert(new Node(7));
        tree.insert(new Node(3));
        tree.insert(new Node(6));
        tree.insert(new Node(4));
        tree.insert(new Node(8));

        tree.remove(1);
        tree.display();

        System.out.println(tree.search(1));

    }
}

// Binary Search Tree = A tree data structure, where each node is greater than it's left child but less than its right.

//                                              Benefit: easy to locate a node when tey are in this order

//                                              Time complexity: Best case O(log n)
//                                                               Worst case O(n)

//                                              Space complexity: O(n)