"""
The proxy object acts as an intermediate between the client and the server.
In the below example, we have a RealObject which is suppose to call request() function without proxy, and now if we
use proxy then we pass this RealObject to the Proxy constructor, and then call the Proxy's request method.
Doing this, we can control the request access, if the request is valid then the proxy will now internally call the
RealObject's request method else throw an exception.

"""


class RealObject:
    def request(self):
        print("RealObject: Handling request.")


class Proxy:
    def __init__(self, real_object):
        self._real_object = real_object

    def request(self):
        print("Proxy: Checking access prior to firing a request.")
        self._real_object.request()
        print("Proxy: Post-request processing.")


def client_code(subject):
    subject.request()


real_subject = RealObject()
print("Client: Executing the client code with a real subject:")
# Without Proxy
client_code(real_subject)

# With Proxy!
proxy = Proxy(real_subject)
print("Client: Executing the same client code with a proxy:")
client_code(proxy)
