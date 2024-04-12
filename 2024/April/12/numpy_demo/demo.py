import psutil
import threading
import time
from rich.console import Console
from rich.prompt import Prompt
from rich.syntax import Syntax
import numpy as np
from multiprocessing import Pool, cpu_count
import inspect

console = Console()
monitor_running = True

def monitor_resources():
    global monitor_running
    try:
        while monitor_running:
            cpu_usage = psutil.cpu_percent(interval=0.1)
            memory = psutil.virtual_memory()
            disk_usage = psutil.disk_usage('/')
            console.print(f"CPU: {cpu_usage}% | Memory: {memory.percent}% | Disk: {disk_usage.percent}%", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        pass

def square(x):
    return x * x

def square_numbers():
    start_time = time.time()
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(square, range(10))
    console.print(f"Squared numbers: {results}")
    end_time = time.time()
    execution_time = end_time - start_time
    console.print(f"Execution time: {execution_time:.2f} seconds")

def fibonacci(n):
    start_time = time.time()
    fib_numbers = [0, 1]
    console.print("Calculating Fibonacci numbers...")
    console.print("F(0) = 0")
    console.print("F(1) = 1")

    for i in range(2, n + 1):
        fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
        console.print(f"F({i}) = {fib_numbers[i]}")

    end_time = time.time()
    execution_time = end_time - start_time

    return fib_numbers[n], execution_time

def large_array_operations():
    start_time = time.time()
    console.print("Generating large array...")
    large_array = np.random.rand(3000, 3000)
    console.print("Calculating determinant...")
    sign, logdet = np.linalg.slogdet(large_array)
    console.print(f"Sign of determinant: {sign}")
    console.print(f"Natural logarithm of the absolute value of determinant: {logdet}")
    end_time = time.time()
    execution_time = end_time - start_time
    console.print(f"Execution time: {execution_time:.2f} seconds")

def write_read_file():
    start_time = time.time()
    path = "largefile.txt"
    console.print(f"Writing to file: {path}")
    with open(path, "w") as file:
        for i in range(10000):
            file.write(f"This is line {i+1}\n")
    console.print("Reading from file...")
    with open(path, "r") as file:
        lines = file.readlines()
    console.print(f"File has {len(lines)} lines")
    end_time = time.time()
    execution_time = end_time - start_time
    console.print(f"Execution time: {execution_time:.2f} seconds")

def task_runner(task_func, *args):
    task_thread = threading.Thread(target=task_func, args=args)
    task_thread.start()
    task_thread.join()

def main_menu():
    tasks = {
        "1": ("Calculate 100000th Fibonacci Number", fibonacci, 100000),
        "2": ("Square Numbers Using Multiprocessing", square_numbers),
        "3": ("Manipulate a Large NumPy Array", large_array_operations),
        "4": ("Read and Write to a Large File", write_read_file),
        "5": ("Exit", None)
    }

    while True:
        console.print("Choose an option to execute:")
        for key, (description, _, *args) in tasks.items():
            console.print(f"{key}: {description}")

        choice = Prompt.ask("Enter your choice", choices=tasks.keys())
        if choice == "5":
            console.print("Exiting...")
            break

        _, func, *args = tasks[choice]

        if Prompt.ask("Do you want to execute this code? (yes/no)", choices=["yes", "no"]) == "yes":
            lines, _ = inspect.getsourcelines(func)
            code = "".join(lines)
            syntax = Syntax(code, "python", line_numbers=True)
            console.print("Code:")
            console.print(syntax)

            monitor_thread = threading.Thread(target=monitor_resources, daemon=True)
            monitor_thread.start()

            task_runner(func, *args)

            global monitor_running
            monitor_running = False
            monitor_thread.join()

        console.print()  # Print an empty line for separation

if __name__ == "__main__":
    main_menu()