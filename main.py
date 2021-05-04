import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Progressbar
import pandas as pd
from threading import Thread

def getCSV ():
    global read_file
    
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_csv (import_file_path, delimiter=';')

def convertToExcel ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    read_file.to_excel (export_file_path, index = None, header=True)

def run_function(name, func):
    # Disable all Buttons
    for btn in buttons:
        btn['state'] = 'disabled'
    
    xlsx_progress.start(interval=10)
    print(name, 'started')
    try:
        func()
    except Exception:
        print('File opening closed or no such file/directory!')
        for btn in buttons:
            btn['state'] = 'normal'

    xlsx_progress.stop()
    print(name, 'stopped')

    # Enable Buttons
    for btn in buttons:
        btn['state'] = 'normal'

def run_thread(name, func):
    t1 = Thread(target=run_function, args=(name, func))
    t1.start()


def csv_clicked():
    run_thread('csv_read', getCSV)

def xlsx_clicked():
    run_thread('save_xlsx', convertToExcel)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

xlsx_progress = Progressbar(root, orient=tk.HORIZONTAL, length=150, mode='indeterminate')
xlsx_progress.pack(pady=5)

browseButton_CSV = tk.Button(text="      Import CSV File     ", command=csv_clicked, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_CSV)

saveAsButton_Excel = tk.Button(text='Convert CSV to Excel', command=xlsx_clicked, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_Excel)
     
exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

buttons = [browseButton_CSV, saveAsButton_Excel, exitButton]

root.mainloop()