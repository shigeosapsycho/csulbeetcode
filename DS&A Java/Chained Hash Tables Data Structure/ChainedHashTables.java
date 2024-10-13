import java.util.*;

// This is an example of what happens if it was an integer instead of a string for the ChainedHashTable
public class ChainedHashTables {
    
    public static void main(String[] args) {
            
        Hashtable<Integer, String> table = new Hashtable<>(10); 
 
        table.put(100, "Spongebob");
        table.put(123, "Patrick");
        table.put(321, "Sandy");
        table.put(555, "Squidward");
        table.put(777, "Gary");

        // table.remove(777); // This will remove the key 777

        for(Integer key : table.keySet()){
            System.out.println((key.hashCode() % 10 + "\t" + key + "\t" + table.get(key)));
        }
    }
}
/*
Output:
7   777     Gary
5   555     Squidward
3   123     Patrick
1   321     Sandy
0   100     Spongebob
*/

// This is what happens when you change the key type to a String instead of an Integer
/*
public class ChainedHashTables {
    
    public static void main(String[] args) {
            
        Hashtable<String, String> table = new Hashtable<>(10); 
 
        table.put("100", "Spongebob");
        table.put("123", "Patrick");
        table.put("321", "Sandy");
        table.put("555", "Squidward");
        table.put("777", "Gary");

        // table.remove("777"); // This will remove the key "777"

        for(String key : table.keySet()){
            System.out.println((key.hashCode() % 10 + "\t" + key + "\t" + table.get(key)));
        }
    }
}

Output:
9   555     Squidward
5   777     Gary
5   100     Spongebob
0   321     Sandy
0   123     Patrick
*/

// Right now this causes a collission for Gary+Spongebob and Sandy+Patrick. To avoid this we can make the list bigger making the modulus operater take a bigger number:

/* This will NOT have any buckets with the same numbers
public class ChainedHashTables {
    
    public static void main(String[] args) {
            
        Hashtable<String, String> table = new Hashtable<>(21); 
 
        table.put("100", "Spongebob");
        table.put("123", "Patrick");
        table.put("321", "Sandy");
        table.put("555", "Squidward");
        table.put("777", "Gary");

        // table.remove(777); // This was before we changed the HashTable from Integer to String

        for(String key : table.keySet()){
            System.out.println((key.hashCode() % 21 + "\t" + key + "\t" + table.get(key)));
        }
    }
}
*/

// Different data types will have different hash code formulas
    // This is because the hashcode is determined by taking the ASCII value of the string and plugging it into a formula
    // The formula is s[0]*31^(n-1) + s[1]*31^(n-2) + ... + s[n-1]
// When a collision happens a LinkedList is created
// To avoid collisions is to increase the size of the hash table, the only downside of this is that it requires more memory