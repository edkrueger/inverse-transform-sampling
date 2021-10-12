import math
import collections

def normal_pdf(x, mu=0, sigma=1):

    numerator = math.exp(-(1 / 2) * ((x - mu) / sigma) ** 2)
    denominator = sigma * math.sqrt(2 * math.pi)

    return numerator / denominator

def make_integral_table(f, a, b, n_steps):

    dx = (b - a) / n_steps

    table = collections.OrderedDict()
    cum_area = 0

    x = a
    table[x] = cum_area

    while x < b:
        next_x = x + dx
        midpoint = (x + next_x) / 2
        height = f(midpoint)
        area = height * dx
        cum_area += area
        table[next_x] = cum_area
        x = next_x

    return table

def integrate(f, a, b, n_steps):

    table = make_integral_table(f, a, b, n_steps)

    def f_integrated(x):

        last_k = None
        for current_k in table.keys():

            if current_k > x:
                break
            last_k = current_k

        return table.get(last_k, 0)

    return f_integrated