public class DynamicArrayImplentation {
    
    public static void main(String[] args) {
        
        DynamicArray dynamicArray = new DynamicArray(5);
        // The list starts with only 5
        dynamicArray.add("A");
        dynamicArray.add("B");
        dynamicArray.add("C");
        dynamicArray.add("D");
        dynamicArray.add("E"); // Right here the list will reach 5 the max elements
        dynamicArray.add("F"); // When adding another one it will resize by capacity * 2

        dynamicArray.delete("A");
        dynamicArray.delete("B");
        dynamicArray.delete("C"); // When removing elements that make the capacity a third of the lenght of the array, it will shrink down 
        
        // dynamicArray.insert(0, "X");
        // dynamicArray.delete("A");
        // System.out.println(dynamicArray.search("C"));

        System.out.println(dynamicArray);
        System.out.println("size: " + dynamicArray.size);
        System.out.println("capacity: " + dynamicArray.capacity);
        System.out.println("empty: " + dynamicArray.isEmpty());
    }
}

    // Advantages:
    // Random access of elemnets O(1)
    // Good locality of reference and data cache utilization
    // Easy to insery/delete at the end

    //Disadvantages:
    // Wastes more memory
    // Shifting elements is time consuming O(n)
    // Expaznding/shrinking the array is time consuming O(n)