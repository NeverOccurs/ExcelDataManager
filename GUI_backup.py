import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
from pandastable import Table

# Initialize Tkinter window
root = tk.Tk()
root.title('Excel/CSV File Editor')

# Control Panel
control_frame = ttk.LabelFrame(root, text='Control Panel')
control_frame.grid(row=0, column=0, padx=10, pady=10)

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx'), ('CSV Files', '*.csv')])
    if file_path:
        if file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            df = pd.read_csv(file_path)
        update_table(df)

ttk.Button(control_frame, text='Upload File', command=upload_file).grid(row=0, column=0)

# Information Status
info_frame = ttk.LabelFrame(root, text='Information Status')
info_frame.grid(row=0, column=1, padx=10, pady=10)
ttk.Label(info_frame, text='Real-time information will be displayed here.').grid(row=0, column=0)

# Data Table
data_frame = ttk.LabelFrame(root, text='Data Table')
data_frame.grid(row=1, columnspan=2, padx=10, pady=10)

def update_table(data):
    for widget in data_frame.winfo_children():
        widget.destroy()
    table = Table(data_frame, dataframe=data)
    table.show()

root.mainloop()