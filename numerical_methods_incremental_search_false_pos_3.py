# As described in NUMERICAL METHODS FOR ENGINEERS  8th Edition
# Incremental search for sign changes of function
# adapted from pseudocode on page 142
# combined with
# mofified false position root finding method
# adapted from pseudocode on page 141

from math import *
import sys

def incremental(f, interval, n_steps):
    """incremental search for sign c-changes
    f: function of one argument to search
    n_steps: number of points to evaluate f on"""
    xl, xu = interval
    x_old = xl
    sign_old = copysign(1, eval_fun(f, x_old))
    intervals = []
    for step in range(n_steps):
        x = xl + (xu - xl) * step / (n_steps - 1)
        sign = copysign(1, eval_fun(f, x))
        if sign != sign_old:
            intervals.append([x_old, x])
        x_old = x
        sign_old = sign
    return intervals

def modfalsepos(f, interval, imax, es):
    """Modified false position method
    f: function of one argument to find root of
    interval: iterable with lowel and upper guess (xl,xu)
    imax: max allowed number of iterations
    es: maximum relative error allowed in %
    """
    xl, xu = interval # lower and upper guesses
    iter_ = 0
    fl = eval_fun(f, xl)
    fu = eval_fun(f, xu)
    xr = xu
    iu = 0; il = 0
    msg = "succes"
    while True:
        xr_old = xr # save previous root estimation
        xr = xu - fu * (xl - xu) / (fl - fu) # new estimate for root
        try:
            fr = eval_fun(f, xr) # function value at new root estimate
        except Exception as e:
            ea = None
            msg = str(e)
            break
        iter_ += 1
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100 # relative error estimate in %
        test = fl * fr
        if test < 0: # values of function at xr and xl have different signs
            xu = xr # root must be in lower half of interval
            fu = eval_fun(f, xu)
            iu = 0 # start counting if lower half more then 2 times reduce function value lower limit fl
            il += 1
            if il >= 2:
                fl /= 2
        elif test > 0: # values of function at xr and xl have same signs
            xl = xr # root must be in upper half of interval
            fl = eval_fun(f, xl)
            il = 0 # start counting if upper half more then 2 times reduce function value upper limit fu
            iu += 1
            if iu >=2:
                fu /= 2
        else:
            ea = 0 # fr must be zero, then xr is root
        if ea < es: # rel error small enough
            break
        elif iter_ >= imax: # max iter reached
            msg = "MaxIterReached"
            break
    return xr, iter_, ea, msg


def eval_fun(fun, x):
    """Calculate function value for given x
    x: float value to evaluate function with"""
    global_dict = { "x": x, "__builtins__": {}}
    global_dict.update(math_fun_dict)
    try:
        f = eval(fun, global_dict)
    except NameError:
        print(f"ERROR: {fun} contains unknown variables other then x")
        sys. exit() 
    except ValueError:
        print(f"ERROR: {fun} is not a valid real function over given interval")
        sys. exit() 
    except SyntaxError:
        print(f"ERROR: invalid syntax detected in {fun}")
        sys. exit() 
    return f


def input_value(prompt, default, value_type):
    """Get user input providing prompt and default choice
       prompt: text to display when asking for input
       default: returned result when user just presses return
       value_type: type user input is converted to, float or int"""
    valid = False
    while not valid:
        answer = input(prompt + "\nHit enter for " + str(default) + ": ")
        if answer == "":
            return default
        try:
            if value_type == int:
                value = int(answer)
            elif value_type == float:
                value = float(answer)
        except:
            valid = False
        else:
            valid = True
    return value
            

def get_input():
    """Get user input for function, bounds, max. interations and rel. error"""
    valid = False
    while not valid:
        print("Function of x to find roots of")
        print("Key words which can be used:", *math_fun_dict.keys())
        fun = input("f(x) = ").lower()
        if fun != "":
            valid = True 
    xl = input_value("Lower boundary of interval on x axis", -1.0, float)
    xu = input_value("Upper boundary of interval on x axis", 1.0, float)
    if xl > xu:
        xl, xu = xu, xl
    es = input_value("Maximum allowed percentage error", 0.1, float)
    N = input_value("Maximum number of iterations", 300, int)
    return fun, xl, xu, es, N


def main_loop():
    terminate = False
    while not terminate:
        print("Incremental search for sign changes of function")
        print("As described in NUMERICAL METHODS FOR ENGINEERS  8th Edition")
        print("------------------------------------------------------------")
        fun, xl, xu, es, N = get_input() # get user input
        results = incremental(fun, (xl, xu), N) # search for zero crossings, results is list of lists [xl, xu]
        if len(results)>0:
            print(f"\nFinding root at each zero crossing using Mofified False Position method")
            print(f"Function {fun}=0\nwith x in interval {xl} to {xu}")
            print(f"{"Interval with zero crossing":25}\t|{"Solution":30}")
            print(f"{"xl":8}\t{"xu":8}\t|{"xr (root)":8}\t{"ea (% error)":8}\t{"residual":8}\tn")
            for xl, xu in results:
                root, steps, rel_error, msg = modfalsepos(fun, (xl, xu), N, es)
                if msg == "ZeroDivisionError":
                    print(f"{xl:.8f}\t{xu:.8f}\t|Division by zero at x = {root}")
                elif msg == "MaxIterReached":
                    print(f"{xl:.8f}\t{xu:.8f}\t|No solution after {N} iterations")
                elif msg == "succes":
                    print(f"{xl:.8f}\t{xu:.8f}\t|{root:.8f}\t{rel_error:.8f}%\t{eval_fun(fun, root):.2e}\t{steps}")
                else:
                    print(f"{xl:.8f}\t{xu:.8f}\t|{msg}")
        else:
            print(f"No zero crossings found in given interval ({xl},{xu})")
        answer = input("Another search? (y/n)").lower()
        if answer != "y":
            terminate = True



# functions which can be used in eval()
math_fun_dict = {   
  "pi": pi, "e": e, "sqrt": sqrt,
  "log": log, "exp": exp, "log10": log10,
  "sin": sin, "cos": cos, "tan": tan,
  "asin": asin, "acos": acos, "atan": atan,
  "atan2": atan2, "abs": abs}

file_name = "roots.txt"

main_loop()        

