# Question link - https://www.hackerrank.com/challenges/apple-and-orange/problem
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0

    for d in apples:
        if s <= a + d <= t:
            apple_count += 1

    for d in oranges:
        if s <= b + d <= t:
            orange_count += 1

    print(apple_count)
    print(orange_count)
