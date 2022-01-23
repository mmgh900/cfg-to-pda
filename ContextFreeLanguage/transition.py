class Transition:

    def __init__(self, input_symbol, currState, nextState, string_to_be_popped, strings_to_be_pushed):
        self.input = input_symbol
        self.current_state = currState
        self.next_state = nextState
        self.string_to_be_popped = string_to_be_popped
        self.strings_to_be_pushed = strings_to_be_pushed

    def __str__(self):
        return f"{self.input}, {self.string_to_be_popped}, {''.join(self.strings_to_be_pushed)}"
