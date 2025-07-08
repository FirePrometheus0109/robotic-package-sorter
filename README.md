Overview

This project implements a package-sorting function for Thoughtful’s robotic automation factory. The function determines how to dispatch packages to the correct stack based on their size (volume and dimensions) and weight.

Sorting Rules

Bulky:
-Volume (Width × Height × Length) ≥ 1,000,000 cm³
-OR any dimension (Width, Height, Length) ≥ 150 cm

Heavy:
-Mass ≥ 20 kg

Stacks:

-STANDARD: Neither bulky nor heavy.

-SPECIAL: Bulky or heavy, but not both.

-REJECTED: Both bulky and heavy.

Usage

The main function is sort(width, height, length, mass):

-width, height, length: Dimensions in centimeters.

-mass: Weight in kilograms.

-Returns: stack name as a string: "STANDARD", "SPECIAL", or "REJECTED".


Example
```
from package_sorter import sort
print(sort(100, 100, 100, 10))    # Output: STANDARD
print(sort(151, 100, 100, 10))    # Output: SPECIAL
print(sort(100, 100, 100, 21))    # Output: SPECIAL
print(sort(151, 100, 100, 21))    # Output: REJECTED
```
