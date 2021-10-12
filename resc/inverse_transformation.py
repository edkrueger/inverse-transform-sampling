import random
import collections

def make_psuedo_inverse_table(f, a, b, n_steps):

    dx = (b - a) / n_steps

    table = collections.OrderedDict()

    x = a
    table[f(x)] = x

    while x < b:
        next_x = x + dx
        table[f(next_x)] = next_x
        x = next_x

    return table

def psuedo_invert(f, a, b, n_steps):

    table = make_psuedo_inverse_table(f, a, b, n_steps)

    def f_inverted(x):
        last_k = None
        for current_k in table.keys():

            if current_k > x:
                break
            last_k = current_k

        return table[last_k] if table[last_k] < b else b

    return f_inverted

def create_random_variable(cdf, a, b, n_steps):

    inverse_cdf = psuedo_invert(cdf, a, b, n_steps)

    def random_variable():

        return inverse_cdf(random.random())

    return random_variable