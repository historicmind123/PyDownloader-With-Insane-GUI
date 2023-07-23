import requests
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import requests

class Downloader:
    def __init__(self) -> None:
        self.save_to = ''
        self.window = tk.Tk()
        self.window.title("Pyloader")
        self.window.config(bg='light yellow')
        self.window.geometry('844x344')
        tk.Label(text="    ",bg='light yellow').pack()
        self.url_label = tk.Label(text="Enter URL")
        self.url_label.config(font='arial 40 bold',bg='light yellow')
        self.url_label.pack()
        tk.Label(text="    ",bg='light yellow').pack()
        self.url_entry = tk.Entry()
        self.url_entry.configure(width=100,bg='white')
        self.url_entry.pack()
        tk.Label(text="    ",bg='light yellow').pack()
        self.browse_button = tk.Button(text="Browse",command=self.browse_file)
        self.browse_button.pack()
        tk.Label(text="    ",bg='light yellow').pack()
        self.download_button = tk.Button(text="Download",command=self.download)
        self.download_button.pack()
        tk.Label(text="    ",bg='light yellow').pack()
        self.progress_bar = ttk.Progressbar(self.window,orient='horizontal',maximum=100,length=300,mode='determinate')
        self.progress_bar.pack()
        self.window.mainloop()
    def browse_file(self):
        file_name = filedialog.asksaveasfilename(initialdir='G:\\PyDownloader\\Downloads\\',initialfile=self.url_entry.get().split('/')[-1])
        self.save_to = file_name

    def download(self):
        url = self.url_entry.get()
        responce = requests.get(url,stream=True)
        total_size_in_bytes = int(responce.headers.get('content-length'))
        block_size = 10000
        file_name = self.url_entry.get().split('/')[-1]
        self.progress_bar['value'] = 0
        with open(self.save_to,'wb') as f:
            for data in responce.iter_content(block_size):
                self.progress_bar['value']+=(100*block_size)/total_size_in_bytes
                self.window.update()
                f.write(data)


Downloader()

