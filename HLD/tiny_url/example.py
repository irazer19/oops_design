"""
# Requirements:
1. How short the url can be? AS short as we can.
2. Traffic: 10M urls per day = 365 * 10M urls per year = For 100 years: 365000M urls = 365Billion urls
3. Allowed chars: 0-9, a-z, A-Z = 10 + 26 + 26 = 62 chars in total, which means for a length of 7 we have 62^7 possibilities
   = 3.5 Trillion which satisfies our requirement.
4. We cannot use SHA256 or MD5 hash function because it will generate longer length string values which is greater than 7
   chars according to our need.
5. So the plan is to generate a unique counter from 0 to 3.5 Trillion for each url, and then we convert this decimal into
   a base 62 and take only the 7 characters to be the part of the shortened url.
6. We can use zookeeper to coordinate the counter value by assigning the range for each server's request.
   Ex: Server1 = 1-5 Million and Server2 = 6M - 10M range, etc. We can also use Snowflake to generate a unique id.
7. Rest of the architecture is easy. We can have a load balancer, and app servers and databases with cache.
   The database schema can have id, user_id, short_url, long_url
"""


# CODE

characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
base = len(characters)


def to_base62(num):
    if num == 0:
        return characters[0]
    result = []
    while num > 0:
        result.insert(0, characters[num % base])
        num //= base
    return "".join(result).rjust(
        7, characters[0]
    )  # Ensure the result is 7 characters long


counter = 123456  # This should be a unique incrementing counter
short_url = to_base62(counter)
