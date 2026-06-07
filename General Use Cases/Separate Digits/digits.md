How numbers are represented mathematically.

For 19:

19= 9×10^0 +1×10^1

But this expression constructs the number from its digits. 

but If we already have 19 and want to extract the digits, we need the reverse process.

---
Very Imporatant Logic - 

**How % and // works:**

19 % 10 = 9 → remainder after dividing by 10 **(last digit)**

19 // 10 = 1 → quotient after dividing by 10 **(remaining digits)**

---

### Method 1: Using % and // (best for 2-digit numbers)

``` python
n = 19

last_digit = n % 10      # 9
first_digit = n // 10    # 1

print(first_digit)
print(last_digit)
```

### General approach for any number
``` python
n = 1234

while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10
```
Output:
4
3
2
1

**Why does this work?**

Because if

1234 = 4×10^0 + 3×10^1 + 2×10^2 + 1×10^3

then:

- % 10 gives the coefficient of 10^0 → 4
- // 10 removes that term and leaves 123
- Repeat until the number becomes 0

- So your idea of 9×10⁰ + 1×10¹ is correct, but that's the forward representation of the number. 
- % and // are the tools used to go backwards and recover the digits.
