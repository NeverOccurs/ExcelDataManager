""" create a GUI that has five sections. 
The first section is for uploading files. It allows uploading 2 csv files.

The second section displays these two file contents.

The third section is split into two parts. Each part corresponds to a csv file and shows all column names which are non-blank in that file.
For each of these column names, there is a drop-down menu beside it showing all values that can be filtered.
The user can select multiple values he wants to filter.

The fourth section is split into two parts. Each part corresponds to a csv file.
For each part, there is a drop-down menu that user can specify a column, and another drop-down menu to dictate the action including sum, average, count, etc.
There will be a result box for each part showing the action applied to the filtered values of the column specified determined by user in section three.

The fifth section will show the difference between the result boxes of two parts in the fourth section.

"""
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

# Define the main application window
root = tk.Tk()
root.title("CSV Analysis Tool")
root.geometry("800x600")

# Variables to hold the dataframes
df1 = None
df2 = None

# Function to upload files and display the content
def upload_files():
    global df1, df2
    file_paths = filedialog.askopenfilenames(filetypes=[("CSV files", "*.csv")])
    if len(file_paths) != 2:
        messagebox.showerror("Error", "You must select exactly 2 CSV files.")
        return
    try:
        df1 = pd.read_csv(file_paths[0])
        df2 = pd.read_csv(file_paths[1])
        display_file_contents()
        populate_filter_menus()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read the files: {e}")

# Function to display file contents in the text widgets
def display_file_contents():
    text_widget1.delete("1.0", tk.END)
    text_widget1.insert(tk.END, df1.to_string())
    text_widget2.delete("1.0", tk.END)
    text_widget2.insert(tk.END, df2.to_string())

# Function to populate column names and corresponding dropdowns for filtering
def populate_filter_menus():
    # Clear previous dropdowns
    for widget in section3.winfo_children():
        widget.destroy()
    
    # Populate dropdowns for df1
    for col in df1.columns:
        if df1[col].notna().any():
            ttk.Label(section3, text=col).pack(side='top', fill='x', expand=True)
            values = df1[col].dropna().unique().tolist()
            cb = ttk.Combobox(section3, values=values, state="readonly")
            cb.pack(side='top', fill='x', expand=True)

    # Populate dropdowns for df2
    for col in df2.columns:
        if df2[col].notna().any():
            ttk.Label(section3, text=col).pack(side='top', fill='x', expand=True)
            values = df2[col].dropna().unique().tolist()
            cb = ttk.Combobox(section3, values=values, state="readonly")
            cb.pack(side='top', fill='x', expand=True)

# Section 1: File upload
section1 = ttk.LabelFrame(root, text="1. Upload CSV Files", height=100)
section1.pack(fill='x', padx=10, pady=5)
upload_button = tk.Button(section1, text="Upload CSV Files", command=upload_files)
upload_button.pack(side='left', padx=10, pady=10)

# Section 2: Display file contents
section2 = ttk.LabelFrame(root, text="2. Display File Contents", height=150)
section2.pack(fill='both', expand=True, padx=10, pady=5)
text_widget1 = tk.Text(section2, height=5)
text_widget1.pack(side='left', fill='both', expand=True)
text_widget2 = tk.Text(section2, height=5)
text_widget2.pack(side='left', fill='both', expand=True)

# Section 3: Column filtering interface
section3 = ttk.LabelFrame(root, text="3. Filter Columns", height=150)
section3.pack(fill='both', expand=True, padx=10, pady=5)

# Section 4: Calculation interface
section4 = ttk.LabelFrame(root, text="4. Apply Calculations", height=150)
section4.pack(fill='both', expand=True, padx=10, pady=5)
# This section will be filled similarly to section 3 with dropdowns for calculations

# Section 5: Result comparison
section5 = ttk.LabelFrame(root, text="5. Results Comparison", height=100)
section5.pack(fill='both', expand=True, padx=10, pady=5)
# This section will display the comparison of results

# Start the application loop
root.mainloop()