from fractions import Fraction

Fract1n = int(input("First Fraction's Numerator:"))
Fract1d = int(input("First Fraction's Denominator:"))
Fract2n = int(input("Second Fraction's Numerator:"))
Fract2d = int(input("Second Fraction's Denominator:"))
denom = Fract1d * Fract2d
numer1 = Fract1n * Fract2d
numer2 = Fract2n * Fract1d

AddorSubtract = input("Add or Subtract?")
ImproperorMixed = input("Improper or Mixed?")
if AddorSubtract == "Subtract" and ImproperorMixed == "Improper":
  numer = (numer1 - numer2)
  fraction = Fraction(numer, denom)
  print("Fraction is:", fraction)
if AddorSubtract == "Add" and ImproperorMixed == "Improper":
  numer = (numer1 + numer2)
  fraction = Fraction(numer, denom)
  print("Fraction is:", fraction)
if AddorSubtract == "Add" and ImproperorMixed == "Mixed":
  numer = (numer1 + numer2)
  numerr = (numer % denom)
  mixed = int(numer / denom)
  fraction = Fraction(numerr, denom)
  print("Mixed fraction is:", mixed, fraction)
if AddorSubtract == "Subtract" and ImproperorMixed == "Mixed":
  numer = (numer1 - numer2)
  numerr = (numer % denom)
  mixed = int(numer / denom)
  fraction = Fraction(numerr, denom)
  print("Mixed fraction is:", mixed, fraction)
