"""
The Fibonacci Scroll -- A Spell of Ancient Numerical Magic
Inscribed by Kiro the Grey Hat
"""

def cast_fibonacci_spell(n=10):
    print("=" * 50)
    print("  Kiro's Fibonacci Scroll -- Awakens!")
    print("=" * 50)

    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    print(f"\nThe first {n} numbers of the sacred Fibonacci sequence:\n")
    for i, num in enumerate(sequence, 1):
        print(f"   Position {i:>2}: {num}")

    print("\n" + "=" * 50)
    print("  The spell is complete. The scroll is sealed.")
    print("=" * 50)

if __name__ == "__main__":
    cast_fibonacci_spell(10)
