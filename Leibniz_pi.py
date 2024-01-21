from timer import timer


@timer
def calculate_pi(n):
    # Initialize denominator
    k = 1

    # Initialize sum
    s = 0

    for i in range(n):

        # even index elements are positive
        if i % 2 == 0:
            s += 4 / k
        else:
            # odd index elements are negative
            s -= 4 / k

        # denominator is odd
        k += 2

    return s

