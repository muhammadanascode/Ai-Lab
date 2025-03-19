import tkinter as tk
from tkinter import messagebox

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    """ DFS Stack (LIFO) """
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        return self.frontier.pop()  # LIFO

class QueueFrontier(StackFrontier):
    """ BFS Queue (FIFO) """
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        return self.frontier.pop(0)  # FIFO

class WaterJug():
    def __init__(self, jugACapacity, jugBCapacity, goal):
        self.jugACapacity = jugACapacity
        self.jugBCapacity = jugBCapacity
        self.goal = goal

    def successors(self, state):
        """ Generate all possible next states. """
        jugA, jugB = state
        return [
            ((self.jugACapacity, jugB), "Fill Jug A"),
            ((jugA, self.jugBCapacity), "Fill Jug B"),
            ((0, jugB), "Empty Jug A"),
            ((jugA, 0), "Empty Jug B"),
            ((jugA - min(jugA, self.jugBCapacity - jugB), jugB + min(jugA, self.jugBCapacity - jugB)), "Pour A → B"),
            ((jugA + min(jugB, self.jugACapacity - jugA), jugB - min(jugB, self.jugACapacity - jugA)), "Pour B → A")
        ]

    def solve(self, method="BFS"):
        """ Solve using BFS or DFS. """
        start = (0, 0)
        frontier = QueueFrontier() if method == "BFS" else StackFrontier()
        frontier.add(Node(start, None, None))
        explored = set()

        while not frontier.empty():
            node = frontier.remove()
            jugA, jugB = node.state

            if jugA == self.goal or jugB == self.goal:
                return self.reconstruct_path(node)

            explored.add(node.state)

            for state, action in self.successors(node.state):
                if state not in explored and not frontier.contains_state(state):
                    frontier.add(Node(state, node, action))

        return None

    def reconstruct_path(self, node):
        """ Reconstruct the solution path. """
        path = []
        while node is not None:
            path.append((node.state, node.action))
            node = node.parent
        return path[::-1]

# GUI Class
class WaterJugGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Jug Solver")
        self.root.geometry("500x400")

        # Labels & Inputs
        tk.Label(root, text="Jug A Capacity:").grid(row=0, column=0, padx=10, pady=5)
        self.jugA_entry = tk.Entry(root)
        self.jugA_entry.grid(row=0, column=1)

        tk.Label(root, text="Jug B Capacity:").grid(row=1, column=0, padx=10, pady=5)
        self.jugB_entry = tk.Entry(root)
        self.jugB_entry.grid(row=1, column=1)

        tk.Label(root, text="Goal Capacity:").grid(row=2, column=0, padx=10, pady=5)
        self.goal_entry = tk.Entry(root)
        self.goal_entry.grid(row=2, column=1)

        # Algorithm Selection
        self.method = tk.StringVar(value="BFS")
        tk.Radiobutton(root, text="BFS", variable=self.method, value="BFS").grid(row=3, column=0, pady=5)
        tk.Radiobutton(root, text="DFS", variable=self.method, value="DFS").grid(row=3, column=1, pady=5)

        # Solve Button
        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Output Box
        self.output_box = tk.Text(root, height=10, width=55)
        self.output_box.grid(row=5, column=0, columnspan=2, pady=10)

    def solve(self):
        """ Solve the problem and display the solution. """
        try:
            jugA = int(self.jugA_entry.get())
            jugB = int(self.jugB_entry.get())
            goal = int(self.goal_entry.get())

            if goal > max(jugA, jugB):
                messagebox.showerror("Error", "Goal cannot be larger than both jugs!")
                return

            problem = WaterJug(jugA, jugB, goal)
            solution = problem.solve(method=self.method.get())

            self.output_box.delete("1.0", tk.END)
            if solution:
                for state, action in solution:
                    if action:
                        self.output_box.insert(tk.END, f"{state} : {action}\n")
                self.output_box.insert(tk.END, f"Steps: {len(solution)-1}")
            else:
                self.output_box.insert(tk.END, "No solution found!")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")

# Run the GUI
root = tk.Tk()
app = WaterJugGUI(root)
root.mainloop()
