class State:

    def __init__(self, name, is_initial, is_final, transitions=None):
        if transitions is None:
            transitions = []
        self.name = name
        self.isInitial = is_initial
        self.isFinal = is_final
        self.transitions = transitions

    def add_transition(self, transition):
        self.transitions.append(transition)

    def __str__(self):
        return self.name
