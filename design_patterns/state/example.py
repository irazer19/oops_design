"""
The State design pattern:
We define multiple different state's for a given class, and we can also change the state of that class based on the
need.
Ex: We have two states, StateA and StateB. Now we have the class Context which requires to maintain a state.
This class has a default stateA, and once stateA handle() method is called, then it changes the Context's state to StateB.
And StateB does the same thing whhen its handle() method is called.

"""


class State:
    def handle(self, context):
        pass


class StateA(State):
    def handle(self, context):
        print("Handling in State A")
        context.state = StateB()


class StateB(State):
    def handle(self, context):
        print("Handling in State B")
        context.state = StateA()


class Context:
    def __init__(self, state: State):
        self.state = state

    def request(self):
        self.state.handle(self)


# Example usage
context = Context(StateA())
context.request()  # Output: "Handling in State A"
context.request()  # Output: "Handling in State B"
