from collections import defaultdict


class MooreMachine:
    def __init__(self):
        self.transitions = {
            'Y3/e3': {
                'throw': [{'next_state': 'Y0/e3', 'cond': None}],
            },
            'Y0/e3': {
                'warp': [{'next_state': 'Y5/e1', 'cond': None}]
            },
            'Y5/e1': {
                'add': [{'next_state': 'Y1/e4', 'cond': None}],
                'throw': [{'next_state': 'Y4/e0', 'cond': None}]
            },
            'Y1/e4': {
                'add': [{'next_state': 'Y6/e1', 'cond': None}]
            },
            'Y6/e1': {
                'throw': [
                    {'next_state': 'Y2/e2', 'cond':
                        {'var': 'weight', 'value': 0}},
                    {'next_state': 'Y4/e0', 'cond':
                        {'var': 'weight', 'value': 1}}
                ]
            },
            'Y4/e0': {
                'paint': [{'next_state': 'Y2/e2', 'cond': None}]
            },
            'Y2/e2': {
                'glare': [{'next_state': 'Y1/e4', 'cond': None}],
                'paint': [{'next_state': 'Y6/e1', 'cond': None}]
            }
        }
        self.current_state = 'Y3/e3'
        self.weight = 0
        self.in_edges_count = defaultdict(int)
        self._build_in_edges()

    def _build_in_edges(self):
        for from_state, methods in self.transitions.items():
            for method, transitions in methods.items():
                for trans in transitions:
                    self.in_edges_count[trans['next_state']] += 1

    def w(self, value):
        self.weight = value

    def get_output(self):
        return self.current_state.split('/')[1]

    def has_max_in_edges(self):
        if not self.in_edges_count:
            return False
        current_in = self.in_edges_count.get(self.current_state, 0)
        return current_in == max(self.in_edges_count.values())

    def has_max_out_edges(self):
        if not self.transitions:
            return False
        out_edges_counts = {}
        for state, methods in self.transitions.items():
            count = 0
            for transitions in methods.values():
                count += len(transitions)
            out_edges_counts[state] = count
        max_out = max(out_edges_counts.values())
        current_out = out_edges_counts.get(self.current_state, 0)
        return current_out == max_out

    def _handle_method(self, method):
        if not any(method in state for state in self.transitions.values()):
            return 'unknown'
        current_trans = self.transitions[self.current_state].get(method)
        if not current_trans:
            return 'unsupported'
        for trans in current_trans:
            cond = trans.get('cond')
            if cond is None or (self.weight == cond['value']):
                self.current_state = trans['next_state']
                return
        return 'unsupported'

    def __getattr__(self, name):
        def wrapper():
            return self._handle_method(name)

        return wrapper


def main():
    return MooreMachine()


def test_unknown_methods():
    obj = main()
    assert obj.rig() == 'unknown'
    assert obj.get_output() == 'e3'


def test_unsupported_transitions():
    obj = main()
    obj.current_state = 'Y6/e1'
    obj.w(2)
    assert obj.throw() == 'unsupported'

    obj = main()
    obj.current_state = 'Y3/e3'
    assert obj.warp() == 'unsupported'


def test_supported_transitions():
    obj = main()
    assert obj.throw() is None
    assert obj.get_output() == 'e3'


def test_conditional_transitions():
    obj = main()
    obj.current_state = 'Y6/e1'
    obj.w(0)
    assert obj.throw() is None
    assert obj.get_output() == 'e2'


def test_edge_cases():
    obj = main()
    obj.in_edges_count.clear()
    assert obj.has_max_in_edges() is False
    assert obj.has_max_out_edges() is False

    obj = main()
    obj.current_state = 'Y6/e1'
    assert obj.has_max_in_edges() is True
    assert obj.has_max_out_edges() is True


def test_empty_transitions():
    obj = main()
    original_transitions = obj.transitions
    obj.transitions = {}

    assert obj.has_max_out_edges() is False

    obj.transitions = original_transitions


def test_sequence_operations():
    obj = main()
    assert obj.w(0) is None
    assert obj.has_max_in_edges() is False
    assert obj.throw() is None
    assert obj.get_output() == 'e3'
    assert obj.has_max_out_edges() is False
    assert obj.warp() is None
    assert obj.has_max_out_edges() is True
    assert obj.get_output() == 'e1'
    assert obj.rig() == 'unknown'
    assert obj.has_max_out_edges() is True
    assert obj.stand() == 'unknown'
    assert obj.add() is None
    assert obj.melt() == 'unknown'
    assert obj.get_output() == 'e4'
    assert obj.add() is None
    assert obj.get_output() == 'e1'
    assert obj.has_max_out_edges() is True
    assert obj.throw() is None
    assert obj.has_max_in_edges() is True
    assert obj.w(1) is None
    assert obj.get_output() == 'e2'
    assert obj.paint() is None
    assert obj.group() == 'unknown'
    assert obj.get_output() == 'e1'
    assert obj.has_max_in_edges() is True
    assert obj.throw() is None
    assert obj.get_output() == 'e0'


def test():
    test_unknown_methods()
    test_unsupported_transitions()
    test_supported_transitions()
    test_conditional_transitions()
    test_edge_cases()
    test_empty_transitions()
    test_sequence_operations()
