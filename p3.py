#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]


def y1(t, y):
    return 3 - 2 * y / t


def asol(t):
    return t - 1 / t**2


yasol = np.vectorize(asol)
h = 0.1
t0 = 1.0
y0 = 0.0
t = np.arange(1.0, 2.0, h)
y = np.zeros(t.size)
y[0] = y0


for i in range(1, t.size):
    y_intermediate = y[i - 1] + h * y1(t[i - 1], y[i - 1])

    y[i] = y[i - 1] + (h / 2.0) * (y1(t[i - 1], y[i - 1]) + y1(t[i], y_intermediate))


def plot():
    plt.cla()
    plt.grid()
    plt.plot(t, yasol(t), "bo--", label="Approximate")
    plt.plot(t, y, "g", label="Exact")
    plt.xlabel(r"$x$")
    plt.ylabel(r"$f(x)$")
    plt.title("Solución exacta y aproximada para la EDO")
    plt.legend(title="Leyenda", shadow=True, fancybox=True)
    plt.savefig("p3.pdf", transparent=True, bbox_inches="tight")


if __name__ == "__main__":
    plot()
