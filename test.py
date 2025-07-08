def sort(width, height, length, mass):
    """
    Sorts package into proper stack based on dimensions and mass.
    Returns: "STANDARD", "SPECIAL", or "REJECTED"
    """
    # Calculate volume
    volume = width * height * length

    # Bulky check: volume >= 1,000,000 or any dimension >= 150
    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150

    # Heavy check: mass >= 20 kg
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# ---------------- TEST CASES ----------------

def test():
    # Standard
    assert sort(100, 50, 100, 10) == "STANDARD"
    # Bulky (volume)
    assert sort(100, 100, 100, 5) == "SPECIAL"
    # Bulky (dimension)
    assert sort(151, 10, 10, 5) == "SPECIAL"
    # Heavy
    assert sort(50, 50, 50, 25) == "SPECIAL"
    # Both (rejected)
    assert sort(200, 200, 10, 25) == "REJECTED"
    # Edge: exactly at thresholds
    assert sort(100, 100, 100, 20) == "SPECIAL"  # mass just at heavy
    assert sort(100, 100, 100, 19.9999) == "SPECIAL"  # just under heavy, but volume bulky
    assert sort(150, 100, 10, 19.99) == "SPECIAL"  # just at dimension threshold
    assert sort(149.999, 100, 10, 19.99) == "STANDARD"  # under all thresholds
    assert sort(150, 150, 150, 20) == "REJECTED"  # all at or above

    print("All test cases passed.")

if __name__ == "__main__":
    test()
