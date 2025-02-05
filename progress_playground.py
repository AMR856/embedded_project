import tkinter as tk
from tkinter import messagebox
import time
import threading
import requests

def program_arduino():
    local_host_url = 'http://localhost:3000'
    url = local_host_url + '/program'
    try:
        root.config(cursor="wait")
        label.config(text="Uploading the code, please wait")
        start_time = time.time()
        _ = requests.get(url) 
        elapsed_time = time.time() - start_time
        time.sleep(elapsed_time)
        root.config(cursor="")
        label.config(text="Uploading is complete!")
        messagebox.showinfo("Task Complete", "The task has finished successfully!")
    except requests.exceptions.RequestException as e:
        root.config(cursor="")
        label.config(text="Error occurred during the request!")
        print(f"Error: {e}")

def start_task():
    """Start the task in a separate thread."""
    # Start the fetch_data function in a separate thread to keep the UI responsive
    threading.Thread(target=program_arduino, daemon=True).start()

# Create the main window
root = tk.Tk()
root.title("Progress Window Example")

# Set window size
root.geometry("300x150")

# Add a label to explain what's happening
label = tk.Label(root, text="Processing, please wait...")
label.pack(pady=10)

# Create a start button to begin the task
start_button = tk.Button(root, text="Start Task", command=start_task)
start_button.pack()

# Start the Tkinter event loop
root.mainloop()
