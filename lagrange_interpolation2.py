# Polynomial interpolation using Lagrange polynomial
# try from wikipedia using info from:
# https://en.wikipedia.org/wiki/Lagrange_polynomial
# https://en.wikipedia.org/wiki/Polynomial_interpolation

# Lagrange polynomial
#
# xi, yi : data points
#
#          n  ⎛         x - xj     ⎞
# p(x) =   ∑  ⎜    ∏   ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯  ⎟ yi
#         i=0 ⎝  0≤j≤n  xi - xj    ⎠
#                 j≠i

# Lagrange polynomial in second barycentric form
#
# xj, yj: data points, wj: barymetric weight
#
# wj =  ∏  (xj - xm)⁻¹  
#      m≠j
#
#           k  ⎛    wj      ⎞
#           ∑  ⎜ ⎯⎯⎯⎯⎯⎯⎯ yj ⎟
#          j=0 ⎝  x - xj    ⎠
# p(x) = ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#           k  ⎛    wj   ⎞
#           ∑  ⎜ ⎯⎯⎯⎯⎯⎯⎯ ⎟ 
#          j=0 ⎝  x - xj ⎠
#


def lagrange(x, x_data, y_data):
    """Interpolation using Lagrange Polynomial
    Accepts one x value to interpolate y value at
    x: x value to interpolate at
    x_data: x values of data to be used
    y_data: y values of data to be used"""
    p = 0.0
    for xn, yn in zip(x_data, y_data):
        basis_polynom = 1.0
        for xp in x_data:
            if xn != xp:
                basis_polynom *= (x - xp) / (xn - xp)
        p += yn * basis_polynom
    return p


# Interpolate y values for list of x values using using Lagrange Polynomial
# in second barycentric form. barycentric weights are computed once beforehand for each node 
def lagrange_arr(xx, x_data, y_data):
    """Interpolation using Lagrange Polynomial
    in second barycentric form
    Accepts a list of x values to interpolate y values at
    xx: list of x values to interpolate y at
    x_data: x values of data to be used
    y_data: y values of data to be used"""
    barycentric_w = []
    for xj in x_data: # compute list of barycentric weights for each node
        w = 1.0
        for xk in x_data:
            if xj != xk:
                w *= 1 / (xj - xk)
        barycentric_w.append(w)
    p = []
    for x in xx:
        if x in x_data: # to avoid division by 0 use y_data at nodes
            index = x_data.index(x)
            p.append(y_data[index]) 
        else: # x is in between nodes
            nom = 0.0; denom = 0.0
            for wj, xj, yj in zip(barycentric_w, x_data, y_data):
                dx = x - xj # dx cannot be 0 as at this point x is not in x_data
                nom += wj / dx * yj
                denom += wj / dx
            p.append(nom/denom)
    return p
                

# data points
x_data = [-5.2 ,-3.5 ,-1.2 ,0.2 ,1.5 ,3.6 ,4.7, 5.7]
y_data = [-10.3,-6.2, 0.3, 1.7, 3.4, 11.4, 6.1, 8.3]
print("data points: ", end="")
print( *zip(x_data,y_data))

# parameters
n = 200 # number of interpolated values 

# generate x values to interpolate at
xl = min(x_data); xu = max(x_data)
dx = (xu-xl)/(n-1)
xx = [xl + k * dx for k in range(n)]
print(f"Generated x values from {xl} to {xu}")

# apply lagrange interpolation on data for range of x values
print("Interpolating y values using Python code")
#yy = [lagrange(x, x_data, y_data) for x in xx]
yy = lagrange_arr(xx, x_data, y_data)
print(f"{len(yy)} points interpolated")

# plot
print("Importing matplotlib.pyplot")
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 8))
plt.rcParams['font.size']="17"
plt.scatter(x_data,y_data,color="red",label="data points")
plt.plot(xx,yy,color="blue",label="interpolation python code")
plt.grid()
plt.title("Polynomial interpolation using Lagrange polynomial\nCoded in Python")
plt.xlabel("x"); plt.ylabel("y")
plt.legend()
plt.show()
