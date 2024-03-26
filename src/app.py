from typing import Dict
from datetime import datetime
from pydantic import BaseModel
from collections import deque

class RateLimiter:

    def __init__(self):
        #describe data struct
        self.customer_request_queues: Dict[str,deque] = {}

    def add_nonrejected_request(self,customer_id:str, timestamp: int) ->bool :
        if customer_id in self.customer_request_queues:
            queue = self.customer_request_queues[customer_id]
        else:
            queue = deque()
            self.customer_request_queues[customer_id] = queue

        queue.append(timestamp)
        return True


    def exceeds_rates_threshold(self,customer_id: str) -> bool
        now_time = datetime.now()
        now_time_int = magic_function(now_time)
        queue = self.customer_request_queues[customer_id]
        
        
        #go through items in loop, if too old remove, 
        # peeking, then removing, because if item is not too old don't remove.
        #if queue gets to less than 10, the return True

        # if queue is 10 or more and oldest item is in time range,
        # return False. 
        

        while len(queue) >= 10 :
            leftmost_item = queue.popleft()
            if self.is_old(leftmost_item):
                continue
            else:
                queue.appendleft(leftmost_item)
                return True

        self.add_nonrejected_request(customer_id,now_time_int)
        return False
if __name__ == "__main__":
    print("Hello world")
    example_method()


10/1s


x/y

O(x)

m customers, then memory, m * x 


