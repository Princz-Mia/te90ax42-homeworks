import numpy as np
import random
import sympy as sp
from sympy.abc import n

# Sorozat definíciója
def sequence(n):
    # Az órai példa sorozat
    return (n**2 - 3*n + 4) / (n**2 - 1)

# Határérték (analitikusan ismert)
L = sp.limit_seq(sequence(n), n)

def find_N(sequence, L, num_test=1000, max_n=10000, epsilon_range=(0.001, 0.1)):
    # Véletlenszerű, 1000db epsilon generálása
    epsilons = [random.uniform(epsilon_range[0], epsilon_range[1]) for _ in range(num_test)]

    for epsilon in epsilons:
        found_N = False

        for N in range(1, max_n):
            all_in_epsilon = True

            for n in range(N + 1, N + 101):
                if abs(sequence(n) - L) > epsilon:
                    all_in_epsilon = False
                    break

            if all_in_epsilon:
                found_N = True
                break

        if not found_N:
            print(f"Nem találtam N-t az epsilon={epsilon} esetén belül.")
            return None

    print(f"Sikeresen találtam N-t minden epsilon esetén a {num_test} próbából.")
    return N


N = find_N(sequence, L)
if (N is not None):
    print(f"Keresett N értéke: {N}")