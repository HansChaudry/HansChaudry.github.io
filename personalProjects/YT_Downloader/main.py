import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox

def createWidget(window, link):
    link_label = Label(window, text="Youtube Link: ", bg="#E8D579")
    link_label.grid(row=1, column=0, pady=5, padx=5)
    root.link_text = Entry(window, width=60, textvariable=link)
    window.link_text.grid(row=1, column=1, pady=5, padx=5)


root = tk.Tk()
root.geometry('600x120')
root.resizable(True, True)
root.title("DataFlair-youtube video downloader")
root.config(background="#000000")

video_link = StringVar()

createWidget(root, video_link)

root.mainloop()