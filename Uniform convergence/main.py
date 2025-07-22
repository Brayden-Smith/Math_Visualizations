import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt
import numpy as np


def ask_epsilon():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    epsilon = simpledialog.askfloat("Epsilon Input", "Enter epsilon value (e.g., 0.001):")

    if epsilon is not None:
        messagebox.showinfo("Epsilon Received", f"You entered: {epsilon}")
    else:
        messagebox.showinfo("No Input", "No epsilon value entered.")

    root.destroy()
    return epsilon


def function(x, n):
    return x / n


def compute_uniform_convergence(epsilon, num_points=100):
    xs = np.linspace(0, 1, num_points)
    n = 1
    max_error = float('inf')
    errors_by_n = []

    while max_error > epsilon:
        errors = [abs(function(x, n)) for x in xs]
        max_error = max(errors)
        errors_by_n.append((n, max_error))
        n += 1

        if n > 1000:  # Safety break in case something goes wrong
            break

    return errors_by_n


def plot_convergence(errors_by_n, epsilon):
    ns, errors = zip(*errors_by_n)

    plt.figure(figsize=(8, 5))
    plt.plot(ns, errors, marker='o')
    plt.axhline(y=epsilon, color='r', linestyle='--', label=f"Epsilon = {epsilon}")
    plt.xlabel("n")
    plt.ylabel("max |f_n(x) - 0|")
    plt.title("Uniform Convergence of f_n(x) = x / n")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("plot.png")
    print("Plot saved to plot.png")


def main():
    epsilon = ask_epsilon()
    if epsilon is None:
        return

    errors_by_n = compute_uniform_convergence(epsilon)
    plot_convergence(errors_by_n, epsilon)


if __name__ == '__main__':
    main()
