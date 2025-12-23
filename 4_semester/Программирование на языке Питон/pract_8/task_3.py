import numpy as np
import matplotlib.pyplot as plt


#3.1
print('#3.1')

def draw(vertices, edges):
    dot_str = "graph {\n"

    for vertex in vertices:
        dot_str += f'   "{vertex[0]}" [label="{vertex[1]}"];\n'

    for edge in edges:
        if len(edge) == 2:
            dot_str += f'   "{edge[0]}" -- "{edge[1]}";\n'
        elif len(edge) == 3:
            dot_str += f'   "{edge[0]}" -- "{edge[1]}" [label="{edge[2]}"];\n'

    dot_str += "}"
    return dot_str

print(draw([(1, 'v1'), (2, 'v2')], [(1, 2), (2, 3), (2, 2)]))


#3.2
print('\n#3.2')

class Chaos:
    def __init__(self, mu, state):
        self.mu = mu
        self.state = state
        self.stabilize()

    def stabilize(self):
        for _ in range(1000):
            self.next()

    def next(self):
        raise NotImplementedError("Subclasses must implement this method")

class LogisticMap(Chaos):
    def next(self):
        self.state = self.mu * self.state * (1 - self.state)
        return self.state

o = LogisticMap(2, 0.1)
print(o.next(), o.next(), o.next())

o = LogisticMap(3.2, 0.1)
print(o.next(), o.next(), o.next())

o = LogisticMap(3.5, 0.1)
print(o.next(), o.next(), o.next())

o = LogisticMap(3.55, 0.1)
print(o.next(), o.next(), o.next())


#3.3
print('\n#3.3')

def visualize(logmap):
    initial_state = logmap.state
    states = [initial_state]
    logmap.next()

    while logmap.state != initial_state:
        states.append(logmap.state)
        logmap.next()

    vertices = []
    edges = []

    for i, state in enumerate(states):
        vertices.append((i, f"{state}"))

    for i in range(len(states) - 1):
        edges.append((i, i + 1))

    edges.append((len(states) - 1, 0))

    return draw(vertices, edges)

print(visualize(LogisticMap(3.5, 0.1)))


#3.4
def bifurcation_diagram(mu_min, mu_max, state):
    n_mu = 40
    last = 10
    mu_values = np.linspace(mu_min, mu_max, n_mu)

    x_values = []
    mu_repeated = []

    for mu in mu_values:
        lm = LogisticMap(mu, state)

        for _ in range(last):
            x = lm.next()
            x_values.append(x)
            mu_repeated.append(mu)

    plt.figure(figsize=(12, 8))
    plt.scatter(mu_repeated, x_values)
    plt.title("Диаграмма бифуркаций логистического отображения")
    plt.xlabel("Параметр μ")
    plt.ylabel("Состояние системы")
    plt.grid(alpha=0.1)
    plt.show()

bifurcation_diagram(1, 4, 0.1)


#3.5
def analyze_distribution(mu, state):
    generator = LogisticMap(mu, state)
    n_samples = 100000

    samples = np.zeros(n_samples)
    for i in range(n_samples):
        samples[i] = generator.next()

    plt.figure(figsize=(12, 6))
    plt.hist(samples, bins=35)
    plt.title(f'Распределение значений LogisticMap')
    plt.xlabel('Значение состояния')
    plt.ylabel('Количество значений')
    plt.grid(alpha=0.3)
    plt.show()

    return samples

samples = analyze_distribution(4, 0.1)