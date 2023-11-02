# %%
from matplotlib import pyplot as plt
import numpy as np
import random as rnd
def f3plt1(color):

    ax = plt.axes(projection='3d')

    # Data for a three-dimensional line
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, color)

    # Data for three-dimensional scattered points
    zdata = 15 * np.random.random(100)
    xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
    ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='greens');

# %%
plt.rcParams['figure.figsize'] = [10,10]

#%%
def f1(x, y):
    #return np.sqrt((np.sin(x) ** 2 - np.cos(y) ** 2 )) #+ 10 * np.random.randn(100)
    return np.sin(np.sqrt(x ** 2 + y ** 2 )) #+ 10 * np.random.randn(100)
#%%
x = np.linspace(-6, 6, 100)
y = np.linspace(-6, 6, 100)

X, Y = np.meshgrid(x, y)
Z = f1(X, Y)

#%%
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='Greens')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');


# %%
print(Z)

#%%
f3plt1('green')
# %%
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='black')
ax.set_title('wireframe');
# %%


ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface');


# %%
r = np.linspace(0, 6, 20)
theta = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 40)
r, theta = np.meshgrid(r, theta)

X = r * np.sin(theta)
Y = r * np.cos(theta)
Z = f1(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none');
# %%
theta
# %%
theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))
z = f1(x, y)
# %%
ax = plt.axes(projection='3d')
ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5);
# %%


ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z,
                cmap='viridis', edgecolor='none');


# %%
#mobius strip
theta = np.linspace(0, 2 * np.pi, 30)
w = np.linspace(-0.25, 0.25, 8)
w, theta = np.meshgrid(w, theta)


phi = 0.5 * theta


# radius in x-y plane
r = 1 + w * np.cos(phi)

x = np.ravel(r * np.cos(theta))
y = np.ravel(r * np.sin(theta))
z = np.ravel(w * np.sin(phi))



# %%
