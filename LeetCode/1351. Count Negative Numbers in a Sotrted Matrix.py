class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total_non_negative = 0  # Total count of non-negative numbers in the grid
        row_count = len(grid)   # Number of rows in the grid
        column_count = len(grid[0]) # Number of columns in the grid
        current_column = column_count - 1  # Start from the last column (rightmost column) by taking the indices and subtracting 1 to get the last column index

        for row in range(row_count): # Checks through row_count iterations
            while current_column >= 0 and grid[row][current_column] < 0: # Check if the current number is negative
                current_column -= 1  # Move left if the current number is negative
            total_non_negative += current_column + 1  # Add the count of non-negative numbers in this row

        """ 
        This section explains what row 18 does in variables that gives the reader clarity
        # total_elements = row_count * column_count
        # negative_count = total_elements - total_non_negative  # Total negative numbers in the grid
        """
        negative_count = row_count * column_count - total_non_negative  # Total negative numbers in the grid
        return negative_count
    
# Time complexity: O(m+n) where m is the number of rows and n is the number of columns in the grid
# O(m+n) is caused by us performing a single pass over the rows and columns in a diagonal fashion rather than scanning all elements in the grid

        """
        Example of how the code works:
        grid = [[4,3,2,-1],
                [3,2,1,-1],
                [1,1,-1,-2],
                [-1,-1,-2,-3]]
        
        First Row: 4,3,2,-1
        3 non-negative numbers positions: [0][0], [0][1], [0][2]
        
        Second Row: 3,2,1,-1
        3 non-negative numbers positions: [1][0], [1][1], [1][2]
        
        Third Row: 1,1,-1,-2
        2 non-negative numbers positions: [2][0], [2][1]
        
        Fourth Row: -1,-1,-2,-3
        0 non-negative numbers positions: [] (All elements are negative)
        
        Total Negative Numbers = 4*4 (rows*columns) = 16 - 8 (position otherwise known as non-negative numbers) = 8
        """