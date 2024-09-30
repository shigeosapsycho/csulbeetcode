import collections

class RecentCounter:

    def __init__(self):
        self.queue = collections.deque() # This is to keep track of the ping calls within the last 3000 ms

    def ping(self, t: int) -> int: # t is the time of the ping call
        self.queue.append(t) # Append the time of the ping call to the queue, appending is basically adding the ping call to the end of the queue
        while self.queue[0] < t - 3000: # If the time of the first ping call in the queue is less than t - 3000, then pop it out of the queue
            self.queue.popleft() # If the time of the first ping call in the queue is less than t - 3000, then pop it out of the queue
        return len(self.queue) # Returning the length of the queue will give us the number of ping calls within the last 3000 ms
    
# O(n) time complexity
# Space complexity is O(n) because we are storing the ping calls in a queue