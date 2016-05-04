def _fib2(N):
    if N == 0: return (0, 1)
    half_N, is_N_odd = divmod(N, 2)
    f_n, f_n_plus_1 = fib2(half_N)
    f_n_squared = f_n * f_n
    f_n_plus_1_squared = f_n_plus_1 * f_n_plus_1
    f_2n = 2 * f_n * f_n_plus_1 - f_n_squared
    f_2n_plus_1 = f_n_squared + f_n_plus_1_squared
    if is_N_odd:
        return (f_2n_plus_1, f_2n + f_2n_plus_1)
    return (f_2n, f_2n_plus_1)

def fib(n):
    return fib2(n)[0]
    
