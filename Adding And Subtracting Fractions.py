from fractions import Fraction

Fract1n = int(input("First Fraction's Numerator:"))
Fract1d = int(input("First Fraction's Denominator:"))
Fract2n = int(input("Second Fraction's Numerator:"))
Fract2d = int(input("Second Fraction's Denominator:"))
denom = Fract1d * Fract2d
numer1 = Fract1n * Fract2d
numer2 = Fract2n * Fract1d

AddorSubtract = input("Add or Subtract?")
if AddorSubtract == "Subtract":
  numer = (numer1 - numer2)
  fraction = Fraction(numer,denom)
  print(fraction)
if AddorSubtract == "Add":
  numer = (numer1 + numer2)
  fraction = Fraction(numer,denom)
  print(fraction)
if AddorSubtract == "Add" and denom % numer:
  numer = (numer1 + numer2)
  numerr = (numer % denom)
  mixed = int(numer / denom)
  fraction = Fraction(numerr, denom)
  print(mixed, fraction)
if AddorSubtract == "Subtract" and denom % numer:
  numer = (numer1 - numer2)
  numerr = (numer % denom)
  mixed = int(numer / denom)
  fraction = Fraction(numerr, denom)
  print(mixed, fraction)
