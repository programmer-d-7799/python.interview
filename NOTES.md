Rate limiter
one customer doesn't overload system, per customer rate limit,  
each customer can make x requests in y seconds

customer id, based on thresholds, if serve request or won't. 

serve or don't serve.  bool for now. 

global thresholds for now. 


storing data about past requests, (the type or attribvutes of the requests matter)
counting, requests in last 10/s in last 1000 ms, was there 10 requests, if 10 or more, reject. 


customer id, 

class RateLimiter:

    def __init__(self):
        self.customer____: Dict[]
        #queue? ---
        # every time customer makes a non rate limited request, then add to queue, maybe jsut add the timestamp itself to the queue, 
        #  remove all items at front of queue that have a timestamp, older than  last second

        0ms -> 1
        10ms -> 2

        1000 ms -> 9

        100, 200, 300 - 1, 2,3,
        400 ms, 
        

        Timestamp could just be 0ms


        #   
        #int, , current reequest in last second
        # every time there is a attempted request (not rejected due to rate limiting), 
        # custoemr request count + 1, 
        #   every 1000 ms, remove count by 10, min (0, count)

        # if customer has 0, and we're 'removing count' then we could remove the customer, 
        # if customer has no activity in say last minute, 
        # -----

    

    def exceeds_rates_threshold(customer_id: str) -> bool
        count requests in last 1000 ms, 
        if >= 10:
            return True

        return False

# customer sends 9 requests, at 0 s, 
# int for customer is 9,
# at 1 s , int -> 0 
# futher requests not excieding limit , all good

#customer sends 10 requests at 0s
int goes to 10
customer sends 1 request 0.5 s

look up, customer int >= 10 -> don't process
and then at 1s, customer down to 0

0.4 s receive 10
1s count down to 0
1.1 s receive 10 , 
this blows our 10/second. 


kotlin, aws, react
alerts is terraform,
Dynamodb

Atlassian’s abstraction for infrastructure

company mainly uses the same

2.5 years. as good as it gets

based on impact.


very laid back. 