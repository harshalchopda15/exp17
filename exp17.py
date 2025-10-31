# Quantum Algorithm and Computational Methods
# Program: Shor’s Algorithm to factor a composite number using period finding (simplified)

from math import gcd
import random

def shors_algorithm(N):
    print("🔹 Shor’s Algorithm Simulation (Simplified) 🔹")
    print(f"Composite number (N): {N}")

    # Step 1: Choose a random a < N that is coprime with N
    a = random.randint(2, N - 1)
    while gcd(a, N) != 1:
        a = random.randint(2, N - 1)

    print(f"Chosen random base (a): {a}")

    # Step 2: Find period 'r' such that a^r ≡ 1 (mod N)
    r = 1
    while pow(a, r, N) != 1 and r < N:
        r += 1

    # If no period found, exit
    if r == N:
        print("No valid period found. Try another 'a'.")
        return

    print(f"Calculated period (r): {r}")

    # Step 3: Classical post-processing to find factors
    factor1 = gcd(pow(a, r // 2) - 1, N)
    factor2 = gcd(pow(a, r // 2) + 1, N)

    # Step 4: Display results
    if 1 < factor1 < N:
        print(f"Possible factors: {factor1}, {factor2}")
    else:
        print("Failed to find non-trivial factors. Try another 'a'.")

# Example: Run for N = 15
shors_algorithm(15)
