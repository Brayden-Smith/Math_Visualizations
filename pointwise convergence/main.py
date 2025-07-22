import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt


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

def function(input, iteration):
    return input ** iteration
def main():
    epsilon = ask_epsilon()
    if epsilon is None:
        return


    delta = .05
    point = 0.01
    data = {}

    while(point <= 3):
        result = epsilon + 1 #start larger than epsilon
        iteration = 1

        while(result > epsilon): #go through iterations until we hit epsilon target
            result = function(point, iteration)
            iteration = iteration + 1

        #we have hit epsilon target, log iteration count
        data[point] = iteration

        #move onto next point
        point = round(point + delta, 10)

    # Plotting
    x_vals = list(data.keys())
    y_vals = list(data.values())

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, marker='o')
    plt.xlabel("Input Value")
    plt.ylabel("Iterations Until < Epsilon")
    plt.title(f"Iterations to Reach f(x)^n < Epsilon ({epsilon})")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plot.png")
    print("Plot saved to plot.png")

if __name__ == '__main__':
    main()
