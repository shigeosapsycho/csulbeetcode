import java.util.Arrays;

public class BinarySearchMain {
    
    public static void main(String[] args) {
        
        int array[] = new int[100000];
        int target = 77777;

        for(int i = 0; i < array.length; i++ ) {
            array[i] = i;
        }

        // int index = Arrays.binarySearch(array, target);

        int index = binarySearch(array, target);
        
                if (index == -1) {
                    System.out.println(target + " not found");
                }
                else {
                    System.out.println("Element found at: " + index);
                }
            }
        
            private static int binarySearch(int[] array, int target) {

                int low = 0;
                int high = array.length - 1;

                while(low <= high){
                    int middle = low + (high - low) / 2;
                    int value = array[middle];

                    System.out.println("Middle: " + value);

                    if(value < target)
                        low = middle + 1;
                    else if(value > target) high = middle - 1;
                    else return middle; // Target is found
                }

                return -1; // Target is not found
            }
}

// Binary search = search algorithm that finds the position
//                 of a target value within a sorted array.
//                 Half othe array is eliminted during each step