# Network Protocols:

# Application layer:
1. Client server protocol
    1. http - 1 connection
    2. ftp - 2 connections, data and control connections.
    3. smtp - to send the email
    4. web sockets
2. Peer to peer protocol
    1. webRTC: Uses UDP because its used in real time video conferencing.


Client server:
Client makes a request and the server responds back, its a one way communication.
Web socket is slightly different because its bidirectional but its still not a peer to peer.
In web socket, the client sends the data to server which sends to another client and vice-versa.

SMTP: To send the email
IMAP: To receive the email

Peer to Peer:
All the clients and servers can communicate with each other.

Transport / Network layer:
1. TCP/IP: We maintain a virtual connection through which data is sent, therefore ordering of the packets is
            maintained. If there is no acknowledgement from the receiver then it again sends the same packet.
2. UDP/IP: No connection is maintained here, the data is sent parallely without any order of the packets, the
            advantage is that its faster than TCP because we dont maintain connection or do acknowledgements.

##########################################################################

# CAP Theorem:
C = Consistency: All nodes should have the same value when requested.
A = Availability: The request should always be processed irrespective of the response code (HTTP 200/500, etc)
P = Partition Tolerent: If any nodes loose connection with each other then the system should not go down.

1. CA: We can achieve CA at the cost of P, meaning that if there is a connection loss between some node, then we
       will have to down the entire system until the connection is re-established.
2. CP: If there is a partition between nodes, then all the nodes cannot be available.
3. AP: If there is a partition between nodes, then even if all the nodes are available, the consistency between them
       will be lost until the connection is re-established.

##########################################################################

# Monolith service:
# Advantages:
1. Easier to manage since all code is in single codebase.
2. Faster performance without any latency issue for the API calls.
3. Easy deployment

# Disadvantages:
1. Hard to scale since all operations are in a single server.
2. High degree of code coupling, changing/updating code may break other parts of the app.
3. Legacy Technologies, If the application is written in an older technology, it can be time-consuming and difficult to
   migrate the whole monolith to a newer technology.

# Micro service:
# Advantages:
1. Easy to Scale
2. Easy to bug fix due to loose coupling.
3. Technology agnostic, any tech can be used in any microservice.
4. Quicker deployment since microservices can be deployed independently,

# Disadvantage:
1. Increased Complexity: Microservices introduce complexity as they transform applications into distributed systems.
   Communication between services, data consistency, and managing different services can be complex.
2. Data Management: Each microservice can have its own database, which can lead to challenges in data consistency and
   management across services
3. Network Congestion and Latency: Microservices communicate over the network, which can lead to network congestion
   and increased latency
4. Testing and debugging a microservices-based application can be more complex due to the distributed nature of the app.

# Micro Service Design Pattern:
# Here are the different phases or steps to create a micro service from scratch:
1. Decomposition: How do we break the components into smaller micro services?
2. Database: How many databases are needed? Do each micro service needs its own database?
3. Communication: What protocols do we use for the communication between the micro services?
4. Integration: How do we integrate the microservice with the existing architecture?
5. Observability: How do we debug or monitor the services?

# Decomposition pattern:
1. By business functionality.
2. By subdomain.

# Strangler design pattern:
- Whenever we want to migrate a monolithic to microservices, we can first deploy the microservice and start sending only
  10% of the traffic to it and 90% to the monolithic. Now slowly if the errors/bugs get fixed then we can increase the
  traffic to the microservice untill all 100% of the traffic moves to it and 0% traffic to the monolithic.

# Database Management in microservice:
1. DB for each individual service.
2. Shared database

# Disadvantage of shared database:
1. If one of the service requires more storage then we will have to vertically scale the database which is expensive.
2. If one of the service wants to delete a row, then it has to check all the dependencies of other services, if any then
   it cant delete it.

# Advantages of shared database:
1. Easy to do JOIN queries.
2. Easy to maintain ACID properties because only a single database exists.

# Disadvantage of Individual database for each microservice:
1. Hard to query join with distributed databases.
2. Hard to maintain Overall ACID property for distributed database.

# SAGA design pattern (Sequence of local transaction):
- Need: Lets say we have 3 databases d1, d2, d3. Now if a transaction fails in d3, then we should also rollback the
        transactions done in d1 and d2, but how do we do it? since the database is distributed in nature!
- Answer: Each database will produce an event after doing a transaction. Now lets say d1 does a transaction and publishes
          an event (failed transaction), now d2 will read this event and see that it has been failed and so it will not
          perform the transcation at all.
          In another scenario, if d1 does a success transaction and publish an event, then d2 will read that and also
          do its transaction and so on.

# CQRS (Command query request segregation):
- We separate the database based on the type of request.
- Since join is hard on distributed database, we will do create, update, delete request on the individual
  distributed database, and read request can be forwarded to the common database where JOIN can be easy.
  Now whenever there is a create, update and delete operation, an event will be published which will save the data
  in the common database enabling access to all the latest data for read query.

# How to scale a database?
- By using more replicas and Master-Slave concept. If the master goes down then one of the slave is promoted as a master.
- Vertical scaling: Increase the system resources and server capacity.
- Horizontal scaling: Sharding of the data such that the data is stored in multiple distributed database.
Types of Sharding:
1. Horizontal sharding: Dividing the data by rows into mmultiple tables, Ex: Storing row-1 to row-100 in db1 and row-101
                        to row-500 in db2.
2. Vertical sharding: Diving the data by column wise and storing in different db.

We can also do nested sharding if needed.

# Consisten Hashing:
- Hashing: Given a key it generates a fixed length character.
- Mod hashing: Given a key, it generates a fixed length character and then mods(%) with the total number of available
             hashes.
- Need for Consisten hashing: [For equal distribution of load!] Lets say we have 3 servers where for a given key we do 
  f(key) % 3 and get the server which needs to store this data. Now if we add a new server then for the same key 
  f(key) % 4 will return a different server but our data will not be found here and we will have to rebalance all the 
  previous data into the correct server which is hard.
- Consisten hashing solves this problem: It ensures that minimum number of rebalance happens when a server is added/removed.
  We place the servers on a virtual ring, and then for a given key we find its hash on the ring and move in clockwise
  direction, now the first server that we find will be serving this key request. To make the request distribution even
  we use virtual server/nodes and place it on the ring such that all the keys are uniformaly handled by all the servers.
  Virtual servers: Say we have a server A, now we use this same server and call it ServerA1, ServerA2, etc on the ring,
  which ultimately points to the same Server A.
- What about replication? If the replication factor n = 3, then we need to replicate the data in n-1 servers = 2 servers.
  We move in the clockwise direction in the ring ignoring all the virtual nodes, and save the data in the node which are
  in a differenet data-center.
- Preference list: It is the list of all nodes where the replica data is stored. The first preference is given to the first
  node where the data is stored. Every node has a preference list, and every other node is aware of every nodes preference list.

# Twitter Snowflake:
One popular example of a distributed unique ID generator is Twitter's Snowflake system. In Snowflake, a 64-bit ID is 
generated by combining a timestamp, a worker number, and a sequence number. The timestamp ensures general chronological 
ordering, the worker number ensures uniqueness across different machines, and the sequence number ensures uniqueness 
for IDs generated by the same worker at the same timestamp


# Back of envelope estimation
Need: Drives our decision for system design.
Considerations:
1. Rough estimation
2. Do not spend too much time on it.
3. Keep the assumption value simple, such as 10 million.

Cheat Sheet:
1. 000 = thousand traffic and storage is in KB
2. 000,000 = Million traffic and storage is in MB
3. 9 zeros = Billion traffic and storage is in GB
4. 12 zeros = Trillion traffic and storage is in TB
5. 15 zeros = Quadtrillion and storage is in PB

Chars = 2 bytes
Long/double = 8 byte
image size = 300kb

Example:
x million(6 zeros) users * y MB(6 zeros) = xy TB (12 zeros)

Things to estimate:
1. Number of servers
2. RAM
3. Storage capacity
4. Tradeoff (CAP theorem)

# Example: Estimation of facebook
## Traffic estimation:
Total user: 1 Billion
DAU (Daily active users): 25% of total users = 250M
Read per user = 5
Write per user = 2
Total request per user = 7

Total traffic per day = 250M * 7 query
Total traffic per second = (250M * 7) / 86400 = 18k query per second

## Storage estimation
- Every user makes 2 posts, where each post is of 250 chars
- 10% of the users upload an image, where image size is 300KB

1 Post of 250 chars = 250 chars * 2 bytes = 500 bytes
So 2 post will require = 500 * 2 = 1000 bytes = 1 KB
Therefore, 250M(6 zeros) users * 1 KB(3 zeros) = 250 GB per day for the post

Now 10% of the DAU users upload 1 image = 25M(6 zeros) users * 300KB(3 zeros) = 7500GB =~ 8TB per day (roundoff)

## RAM estimation
- Each users last 5 post is put in a cache.
So 1 post requires 500 bytes, and 5 post will require 5 * 500 = 2500 bytes ~ 3KB
DAU = 250M, so 250M(6 zeros) * 3 KB(3 zeros) = 750 GB memory 

If one machine can hold 75Gb of data then we will need 750/75 = 10 machines will be needed.

Latency: 95% of the time we will have 500ms of latency
1 server has 50 threads
Tradeoff: Also we would want Availability and Partition tolerance for facebook. Consistency is not so important here.


# Data Versioning
It uses Vector clock.
In vector clock, lets say we have 3 servers s1, s2, s3. Every server will maintain a VALUE(server, counter), here
the server=the server which handled the request and counter=the version of this data.
Now if CAR is written in s1 then it will have CAR(s1, 1), and lets say it replicated the data to s2, s3.
So s2 = Car(s1, 1) and s3 = Car(s1, 1).
Now a request value CART came in but s1 is down, so from the preference list we select s2 to handle this request, so
s2 = CAR(s1, 1), CART(s2, 1), and s2 was not able to replicate this data to s3.
Now again lets say a request value CARM came in, and both s1 and s2 were down, so s3 handled it so:
s3 = CAR(s1, 1), CARM(s3, 1)
Next, all servers went healthy, and a GET request came in for it so s1 checks in:
s1 = CAR(s1, 1)
s2 = CAR(s1, 1), CART(s2, 1)
s3 = CAR(s1, 1), CARM(s3, 1)

s1 will know that CAR(s1, 1) cannot be the latest value because s2, s3 have new data version so it has to decide
between CART(s2, 1) and CARM(s3, 1) but thats a conflict, and so it sends both the data to the client to resolve it.
Client resolves the conflict and updates the nodes with the correct value.

# Gossip protocol:
Need? How will the servers know which of the servers are healthy and which ones are down?
Each server maintains a list of all the servers health status, and sends the heartbeats periodically to let other 
servers know that its alive.
Lets say server2 stopped sending heartbeat, now if majority of the servers identify that server2's heartbeat was not
received in last x seconds, then it server2 will be conculded as dead and will be replaced.

# Merkel Tree
Used to compare data for data corruption check.
Lets say we have 4 chunks for a given data, now we will create a binary tree like structure where these 4 chunks are 
the leaf nodes and compute the hash at every node until we reach the root node. 
To compare whether data1 ==  data2, we only have to compare the root nodes of the these two data recursively.

# NOSQL types:
1. Key-value pair: Simplest nosql db where the value can be anything.
2. Document db: It has key and the value is another document in json format on which we can run queries.
3. Column wise db: Here for every key we store a value which is a {col1: val1, col2: val2, col3: val3, etc}
4. Graph db: Data is stored in a node and its related to another node via an edge(relation).

# ACID property:
1. Atomicity: This property ensures that a transaction is treated as a single, indivisible unit of work. Either all the 
   changes made in a transaction are committed to the database, or if the transaction fails at any point, all changes 
   are rolled back. There is no scenario where a transaction is partially completed

2. Consistency: Consistency ensures that a transaction brings the database from one valid state to another. The 
   database should satisfy a set of predefined rules, known as integrity constraints. If a transaction would violate 
   these constraints, it is rolled back and the database remains unchanged

3. Isolation: This property ensures that concurrent execution of transactions leaves the database in the same state as 
   if the transactions were executed sequentially. This means that the intermediate state of a transaction is invisible to other transactions

4. Durability: Durability guarantees that once a transaction has been committed, it will remain committed even in the 
   case of a system failure (such as a power outage or crash). This is typically achieved by storing transaction logs 
   that can be used to recreate the system state right before the failure

# Bloom Filter:
Bloom Filter: A Bloom filter is a probabilistic data structure that is used to test whether an element is a member of a 
set. It's space-efficient and can quickly check if an item is in a set

False Positives: The price we pay for efficiency is that Bloom filters are probabilistic in nature, meaning there might
be some false positive results. A false positive means the filter might indicate that a given item is in the set when 
it is not. However, Bloom filters never generate false negative results

Bitmap: Under the hood, a Bloom filter is just a bitmap. Initially, all the bits are set to 0. To add an item, the item
is hashed, the result is modded by the length of the bitmap, and that bit is set to 1. To check if an item is in the 
set, the same process is followed. If the bit is 0, then the item is definitely not in the set. If the bit is 1, then 
the item might be in the set, but it could be a false positive.
A common use case is checking the availability of usernames. A Bloom filter can quickly check if a username is taken 
without needing to store the actual username

# Proxy Server:
Its a server which sits between the client and the app server.
There are two types:
1. Forward proxy
2. Reverse proxy

## Forward proxy
No server can talk to a client directly.
It hides the client from the app servers. When a client sends a request, the proxy receives it and sends its own ip
as the request maker to the app server, and the server thinks that the request is coming from the proxy.
The server only talks to the proxy. 

Advantages:
1. This gives anonymity to the client.
2. Group requests, ex: if two or more client asks for google.com, then it will just send a single request to the internet
   and returns the result to both the clients.
3. Access restricted data/content. If your country has blocked certain websites, then the proxy will block it if you try
   to access it.
4. Proxy servers can cache frequently accessed content

## Reverse Proxy:
No traffic coming from the internet can directly talk to the app servers.
Advantages:
1. Security: outside world is not aware of the internal server ip address but only of the reverse proxy. Attackers can
   only attack reverse proxy server and not the internal servers. CDN is a kind-of a reverse proxy.
2. Reverse Proxy can also act as a firewall.

## Reverse Proxy vs Load balancer:
1. Reverse proxy can act like a load balacner but load balancer cannot replace a proxy.
2. For a single server we dont need a load balancer, but we need a reverse proxy.


# Load balancer:
Two types:
1. Application LB: Can read headers, session, etc. It is much more advanced.
2. Network LB: This is much faster than the App LB.

Round Robin:
The load is distributed in sequence and in fixed order. It is easy to implement and load is equally distributed.
Disadvantage: If a server is 10x faster than other servers, its capacity will never be fully utilized.

Weight Round robin:
We can give higher weight to a server and weight represents the capacity of the server. If a server has a weight of 3,
then first 3 requests will go that server and so on.
Disadvantage: If a low capacity server receives a long processing request and high capacity server gets fast requests,
then the low capacity server will be over-burdened because it will get a request before it has finished previous request.

IP Hash algorithm: Every client ip will be hashed and assigned a server, this will ensure that the same server processess
the same client everytime (Sticky).
Disadvantage: If lots of client are going through a forward proxy, then the LB will hash the proxy's IP address which
will over burnden a single server with all of those requests.

Least connections:
The LB will forward the request to server having the least number of active connections.
Disadvantage: Sometimes tcp connections are active without any data transfer, this will make the LB take wrong decisions.

Weighted Least Connection:
Same as Least connection except that we assign weight to every server based on its capcity. LB will compute the
ratio of (number of active connection) / weight for every request.


# Caching
Caching is the mechanism of storing data in a temporary storage location, either in memory or on disk, to serve data 
requests faster. It improves performance by decreasing page load times and reduces the load on servers and databases

Layers of caching:
1. Client side caching(Browser)
2. CDN(Used to store static data)
3. Load balancer
4. Server side caching (Redis)**

Ususally the server side cache such as redis sits between the app server and the database.

## Distributed Caching
This is a cache that spans multiple servers so that it can grow and shrink in size and throughput as needed.
Each client has a "cache client" which help it connect to one of the cache servers. It uses consistent hashing
to select one of the servers from the cluster.

## Caching Strategies:
Cache-Aside: This is the most commonly used caching approach. When an application needs data, it first checks the cache.
If the data is in the cache (a cache hit), it is returned immediately. If the data is not in the cache (a cache miss), 
the application retrieves the data from the main storage, stores it in the cache for future use, and then returns it. 
This strategy is particularly useful for applications with read-heavy workloads.

Read-Through: In this strategy, the cache sits between the application and the main storage. When a read request comes 
in, the cache checks if it has the data. If it does, it returns it (cache hit). If it doesn't, it retrieves the data 
from the main storage, stores it, and then returns it. This strategy ensures that the cache always has the most recent 
copy of the data.

Write-Through: This strategy is similar to read-through, but it applies to write operations. When a write request comes
in, the cache updates itself and also forwards the write to the main storage. This ensures that the cache and the main 
storage are always in sync.

Write-Back (or Write-Behind): In this strategy, when a write request comes in, the cache immediately updates itself and 
acknowledges the write to the application, but it delays updating the main storage. This can improve performance by 
reducing the number of write operations to the main storage, but there's a risk of data loss if the cache fails before
it has a chance to update the main storage.

Write-Around: In this strategy, write requests are sent directly to the main storage, bypassing the cache. This prevents
the cache from being filled up with write-intensive data that may not be read again soon. However, if the data is read 
soon after being written, this strategy could result in more cache misses.

Refresh-Ahead: This strategy predicts which data items are likely to be requested in the near future and preloads them 
into the cache. This can reduce cache misses, but it requires a good prediction algorithm to be effective.

## Cache Replacement Policies: 
These are strategies that determine which item to discard when the cache is full. 
Common policies include Least Recently Used (LRU), First In First Out (FIFO), and Least Frequently Used (LFU)


# How to handle distributed transaction?
A distributed transaction is a set of operations on data that is performed across two or more databases. 
These operations are coordinated across separate nodes connected by a network, and they ensure ACID properties and data integrity

Three ways to handle it:
1. 2-Phase commit
2. 3-Phase commit
3. SAGA pattern (already discussed above)

## 2-Phase commit:
There is a transaction coordinator which does the following:
1. Sends the query to the two databases d1, d2.
2. PHASE 1: Then asks d1 and d2 "Are you prepared for commit?".
3. PHASE 2: If both reply "OK", then it sends a commit request to both of them.
4. If any one of them reply "NO" then it aborts all the requests.

Problems that can arise:
1. Transcation coordinator failure:
   - Prepare message can be lost
   - Commit message is lost
2. Database failure during response.
   - Database response message is lost

Solution:
- Transaction coordinator will maintain a lock file and writes all the actions.
- If the prepare message is lost, and db has applied the lock, then the db will wait for sometime and then abort.
- If OK message is lost, then the transaction coordinator will wait for sometime and then abort.
- If the commit message is lost then the db will contact the transaction coordinator and ask for either commit or abort.
  The transcation coordinator will look into its lock file and reply to the db. Here the db is not able to take its
  own decision.

## 3-Phase commit:
The only difference is that it has an intermediate phase which sends the decision of the transcation coordinator:
1. Sends the query to the two databases d1, d2.
2. PHASE 1: Then asks d1 and d2 "Are you prepared for commit?".
3. PHASE 2: If both reply "OK", then it sends a precommit message telling its final decision "Commit/abort"
4. PHASE 3: If both reply "ACK", then it sends a commit request to both of them.
5. If any one of them reply "NO" then it aborts all the requests.

Now if the pre-commit message fails, then the databases will coordinate with each other and check about the latest
decision of the transcation coordinator from their lock file, and if any database has recevied "commit" or "abort", 
then all other databases will follow it.


