---
title: Bit Manipulation
author: Ren Zhang
date: May-11-2020
---

# Bit Manipulation
## Reference 
### 4 bit signed integer decimal to binary table
| decimal | binary | decimal | binary |
| ------: | :----- | ------: | :----- |
|      -8 | 1000   |       7 | 0111   |
|      -7 | 1001   |       6 | 0110   |
|      -6 | 1010   |       5 | 0101   |
|      -5 | 1011   |       4 | 0100   |
|      -4 | 1100   |       3 | 0011   |
|      -3 | 1101   |       2 | 0010   |
|      -2 | 1110   |       1 | 0001   |
|      -1 | 1111   |       0 | 0000   |

## Operators 
| operator | name               | what it does                       |             example |                                                    sample property / usage |
| :------- | :----------------- | :--------------------------------- | ------------------: | -------------------------------------------------------------------------: |
| ~        | complement         | switch each 0 to 1 and each 1 to 0 |        ~0101 = 1010 |                                         `~x = -x - 1` and  `~(x - 1) = -x` |
| &        | and                | 1 iff both bits are 1 else 0       |  0110 & 0101 = 0100 |             `x & - x` to extract last bit, `x & (x - 1)` to clear last bit |
| \|       | or                 | 0 iff both bits are 0 else 1       | 0110 \| 0101 = 0111 |                                               `flags |= x` to set the flag |
| ^        | xor (eXclusive OR) | 1 iff only one bit is 1 else 0     |  0110 ^ 0101 = 0011 | `0 ^ x = x`, `x ^ x = 0` simple checksum `reduce(operator.xor, words, 0)` |
| <<       | left shift         | shift bits to left                 |    0011 << 2 = 1100 |                                                 `x << y` is $x \times 2^y$ |
| >>       | right shift        | shift bits to right                |    0110 >> 2 = 0001 |                                   `x >> y` is $\lfloor{x \div 2^y}\rfloor$ |

## Usages
1. Set a bit at a position
```python
def set_bit(x, pos):
    mask = 1 << pos
    return x | mask
```

2. Clear a bit at a position
```python
def clear_bit(x, pos):
    mask = ~(1 << pos)
    return x & mask
```

3. Clear leading bits from position
```python
def clear_leading_bits(x, pos):
    mask = (1 << pos) - 1
    return x & mask
```

4. Clear trailing bits after position
```python
def clear_trailing_bits(x, pos):
    mask = (1 << 31) - 1 << pos
    return x & mask
```

5. Flip a bit at position
```python
def flip_bit(x, pos):
    mask = 1 << pos
    return x ^ mask
```

6. Check a bit at position
```python
def check_bit(x, pos):
    return x >> pos & 1
```

7. Check number is even
```python
def check_even(x):
    return (x & 1) == 0
```

8. Check number is power of 2
```python
def check_pow_2(x):
    return x & (x - 1) == 0
```

9. Check two numbers are of opposite sign
```python
def check_opposite_sign(x, y):
    return x ^ y < 0
```

10. Swap integers the bit manipulation way
```python
def swap(x, y):
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y
```
