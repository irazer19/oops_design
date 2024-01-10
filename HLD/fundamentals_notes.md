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
- Need for Consisten hashing: Lets say we have 3 servers where for a given key we do f(key) % 3 and get the server 
  which needs to store this data. Now if we add a new server then for the same key f(key) % 4 will return a different
  server but our data will not be found here and we will have to rebalance all the previous data into the correct server
  which is hard.
- Consisten hashing solves this problem: It ensures that minimum number of rebalance happens when a server is added/removed.
  We place the servers on a virtual ring, and then for a given key we find its hash on the ring and move in clockwise
  direction, now the first server that we find will be serving this key request. To make the request distribution even
  we use virtual server/nodes and place it on the ring such that all the keys are uniformaly handled by all the servers.
  Virtual servers: Say we have a server A, now we use this same server and call it ServerA1, ServerA2, etc on the ring,
  which ultimately points to the same Server A.

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