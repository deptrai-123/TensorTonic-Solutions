
def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    for i in range(0,steps,1):
        x0 = x0 - lr*(2*a*x0 + b)
    return x0
    pass