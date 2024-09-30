class RecentCounter:
    
    def __init__(self):
        self.request_map = {} # create a dictionary to store the ping calls
        
    def ping(self, t: int) -> int:
        self.request_map[t] = self.request_map.get(t, 0) + 1 # If the time of the ping call is already in the dictionary, increment the count by 1. Otherwise, add the time of the ping call to the dictionary with a count of 1

        for time in list(self.request_map.keys()): # Iterate through the keys of the dictionary
            if time < t - 3000: # If the time of the ping call is less than t - 3000, then remove it from the dictionary
                del self.request_map[time]
        return len(self.request_map) # Return the length of the dictionary to get the number of ping calls within the last 3000 ms
    
# O(n) time complexity
# Space complexity is O(n) because we are storing the ping calls in a dictionary