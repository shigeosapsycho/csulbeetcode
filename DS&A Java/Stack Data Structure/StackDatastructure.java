import java.util.Stack;

public class StackDatastructure{

    public static void main(String[] args) {
        
        // Stack = LIFO data structure. Last in first out
        //  Stores objects into a sort of "Vertical Tower"
        //  push() = add an item to the top of the stack
        //  pop() = remove an item from the top of the stack

        Stack<String> stack = new Stack<String>();
        
        // System.out.println(stack.empty());
        
        stack.push("Minecraft");
        stack.push("Skyrim");
        stack.push("Doom");
        stack.push("Borderlands");
        stack.push("FFVII");

        // stack.pop(); // Removes FFVII
        // stack.pop(); // Removes Borderlands
        // stack.pop(); // Removes Doom
        // stack.pop(); // Removes Skyrim
        // stack.pop(); // Removes Minecraft
        // // stack.pop(); Causes an EmptyStackException error

        // String myFavGame = stack.pop();

        // System.out.println(stack);
        // System.out.println(myFavGame);

        // System.out.println(stack.peek());

        // System.out.println(stack.search("Borderlands"));
        // System.out.println(stack.search("Valorant")); // Will return -1 if serach does not find the object within the stack

        // for(int i = 0; i < 10000000; i++){ // An OutOfMemoryError is supposed to happen here but my processor can handle this
            
        //     stack.push("Skyrim");
        // }

        // Uses of stacks?
        // 1. undo/redo features in text editors
        // 2. moving back/forward through browser history
        // 3. backtracking algorithms (maze, file directories)
        // 4. calling functions (call stack)

        System.out.println(stack);
    }
}