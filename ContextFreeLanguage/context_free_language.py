from ContextFreeLanguage.state import State
from ContextFreeLanguage.transition import Transition
from collections import defaultdict

LAMBDA = "λ"
EPSILON = "ε"
DELTA = "𝛿"


class ContextFreeLanguage:

    def __init__(self):
        init_state = State("q_s", True, False)
        mid_state = State("q_m", False, False)
        final_state = State("q_f", False, True)
        self.states = (init_state, mid_state, final_state)
        self.transitions = []

    def is_in_language(self, candidate_string):
        stack = [EPSILON]
        finish_process, state = self.pars_candidate(candidate_string, self.states[0], stack)
        return state.isFinal and finish_process

    def print_as_pda(self):
        transition_function = defaultdict(lambda: [])
        for transition in self.transitions:
            key = (transition.current_state, transition.input, transition.string_to_be_popped)
            transition_function[key].append((transition.next_state, transition.strings_to_be_pushed))

        for (key, value) in transition_function.items():

            targets = []
            for val in value:
                targets.append(
                    '(' + str(val[0]) + ',' + ''.join(val[1]) + ')'
                )

            transition_line = f"{DELTA}({key[0]}, {key[1]}, {key[2]})= {', '.join(targets)}"
            print(transition_line)

    def pars_candidate(self, candidate_string, current_state, stack):
        top = stack[len(stack) - 1]
        finish_process = False

        if len(candidate_string) > 0:
            current_char = candidate_string[0]
        else:
            current_char = LAMBDA  # Try edges with lambda

        state = current_state
        passed_an_edge = False

        for transition in self.transitions:
            """
                Conditions to be checked
            """
            is_in_current_state = transition.current_state is current_state
            can_cross_the_edge = (transition.input == current_char or transition.input == LAMBDA)
            can_pop_from_stack = transition.string_to_be_popped == top

            if is_in_current_state and can_cross_the_edge and can_pop_from_stack:

                popped_stack = stack[:-1]  # Pop from the stack

                push_symbols = transition.strings_to_be_pushed[:]
                push_symbols.reverse()  # Because it must be pushed in a reversed order

                for sym in push_symbols:
                    if sym == LAMBDA:
                        continue
                    popped_stack.append(sym)

                # Recursive calls
                if transition.input == LAMBDA:
                    finish_process, state = self.pars_candidate(candidate_string[:], transition.next_state,
                                                                popped_stack)
                else:
                    finish_process, state = self.pars_candidate(candidate_string[1:], transition.next_state,
                                                                popped_stack)

                passed_an_edge = True  # mark path traversed
                if state.isFinal and finish_process: break

        if not passed_an_edge:
            finish_process = len(candidate_string) == 0

        return finish_process, state

    def import_grammar(self, grammar_rules):
        start_variable_name = grammar_rules[0][0]
        [self.add_rule(item) for item in grammar_rules]

        start_transitions = Transition(LAMBDA, self.states[0], self.states[1], EPSILON,
                                       [start_variable_name, EPSILON])
        final_transitions = Transition(LAMBDA, self.states[1], self.states[2], EPSILON,
                                       [EPSILON])

        self.transitions.append(start_transitions)
        self.transitions.append(final_transitions)

    def add_rule(self, rule):
        rule = rule.strip().replace(" ", "")
        left_side = rule[:rule.find('-')]
        right_side = rule[rule.find('>') + 1:]
        right_side = right_side.split('|')

        for semi_terminal in right_side:
            variables = list(semi_terminal[1:])
            self.transitions.append(
                Transition(
                    semi_terminal[:1],
                    self.states[1],
                    self.states[1],
                    left_side,
                    variables if len(variables) > 0 else [LAMBDA]
                )
            )
