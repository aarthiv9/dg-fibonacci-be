# The following is based on a article for fast Fib number calculation:
# http://blog.richardkiss.com/?p=398

def _fib2(n):
    if n == 0: return (0, 1)
    half_n, is_n_odd = divmod(n, 2)
    f_n, f_n_plus_1 = fib2(half_n)
    f_n_squared = f_n * f_n
    f_n_plus_1_squared = f_n_plus_1 * f_n_plus_1
    f_2n = 2 * f_n * f_n_plus_1 - f_n_squared
    f_2n_plus_1 = f_n_squared + f_n_plus_1_squared
    if is_n_odd:
        return (f_2n_plus_1, f_2n + f_2n_plus_1)
    return (f_2n, f_2n_plus_1)

def fib(n):
    return fib2(n)[0]
