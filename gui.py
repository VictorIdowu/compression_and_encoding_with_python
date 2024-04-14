import tkinter as tk
from tkinter import filedialog
from compressmodule import compress,decompress

def open_file():
  filename = filedialog.askopenfilename(initialdir='/', title='Seclect a file to compress')
  return filename

def compression():
  # i = input_entry.get()
  o = output_entry.get()
  compress(open_file(),o)

def decompression():
  # i = input_entry.get()
  o = output_entry.get()
  # decompress(i,o)


window = tk.Tk()
window.title("Compression Engine")
window.geometry('600x400')

# input_label = tk.Label(window, text='File to be compressed')
# input_entry = tk.Entry(window)
output_label = tk.Label(window, text='Name of the commpressed file')
output_entry = tk.Entry(window)

compress_button = tk.Button(window, text='Compress', command=compression)
decompress_button = tk.Button(window, text='DeCompress', command=decompression)

# input_label.grid(row=0, column=0)
# input_entry.grid(row=0, column=1, pady=5)
output_label.grid(row=1, column=0)
output_entry.grid(row=1, column=1,pady=5)
compress_button.grid(row=2,column=0, pady=15)
decompress_button.grid(row=2,column=1, pady=15)

window.mainloop()