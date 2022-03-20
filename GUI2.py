from tkinter import *
from tkinter.font import *
from tkinter.ttk import *
import tkinter as tk1
import tkinter as tk2
from tkinter.filedialog import askopenfilename
from Test import Testing

class Gui():
    #User Interface Klasifikasi#
    new_window= ''
    tampil = Tk()

    def openwindow(tampil=tampil):
        global new_window
        new_window = tk1.Toplevel(tampil)
        new_window.title("Classification")
        new_window.iconbitmap('logo.ico')
        new_window.geometry("1070x500")

        fontStyle = Font(family = "Tempus Sans ITC Regular", size = 20)
        judul = Label(new_window, text = "Classification", font = fontStyle)

        def open_file():
            filepath = askopenfilename(
                filetypes=[("Text Data", ".xlsx"), ("All Files", ".*")]
            )
            entryPath.delete(0,END)
            entryPath.insert(0, filepath)

        def start_file():
            filepath = (entryPath.get())
            dataAcc, conf_matrix, class_report = Testing.testing(filepath)

            textbox.delete('1.0', END) #menghapus isi textbox
            textbox.insert(END, "Accuracy Score: %0.2f%% " % (dataAcc * 100))
            textbox.insert(END, "\n")
            textbox.insert(END, conf_matrix)
            textbox.insert(END, "\n")
            textbox.insert(END, class_report)

        entryPath = Entry(new_window,width = 50) #textbar untuk menampilkan path file dataset
        entryPath.insert(0, "Select File...")
        browse = Button(new_window, text = "Browse File", command = lambda:open_file()) #ini isi perintah button" (panggil fungsi open_file)
        start = Button(new_window, text = "Start Classification", command = lambda:start_file()) #ini isi perintah button" (panggil fungsi start_file)

        # progress = Progressbar(new_window, orient = HORIZONTAL, length = 750, mode = 'determinate')
        textbox = Text(new_window,width = 130)
        scroll = Scrollbar(new_window)
        scroll.config(command = textbox.yview)
        textbox.config(yscrollcommand = scroll.set)

        judul.grid(row = 0, column = 0,columnspan = 3,padx = 3,pady = 3)
        entryPath.grid(row = 1, column = 0,sticky = W+E+N+S,padx = 3,pady = 3)
        browse.grid(row = 1,column = 1,sticky = W+E+N+S,padx = 3,pady = 3)
        start.grid(row = 1,column = 2,sticky = W+E+N+S,padx = 3,pady = 3)
        # progress.grid(row = 2, column = 0, columnspan = 3,sticky = W+E+N+S,padx = 3,pady = 3)
        textbox.grid(row = 3, column = 0, columnspan = 3,padx = 3,pady = 3)
        scroll.grid(row = 3, column = 3, sticky = W+E+N+S)
    #End User Interface Klasifikasi#

    #User Interface Model Summary#
    new_window2= ''
    def openwindow2(tampil=tampil):
        global new_window2
        new_window2 = tk2.Toplevel(tampil)
        new_window2.title("Summary Model")
        new_window2.iconbitmap('logo.ico')
        new_window2.geometry("1260x600")

        gambar = PhotoImage(file='ModelSummary.png')
        fontStyle = Font(family = "Tempus Sans ITC Regular", size = 20)
        label = Label(new_window2, compound=BOTTOM, font=fontStyle, text="Summary Model", image=gambar).pack()
        # label.grid(row=3, column=3)

        # judul = Label(new_window2, text = "Summary Model", font = fontStyle)
        #
        # textbox = Text(new_window2,width = 130)
        # scroll = Scrollbar(new_window2)
        # scroll.config(command = textbox.yview)
        # textbox.config(yscrollcommand = scroll.set)
        #
        # judul.grid(row = 0, column = 0,columnspan = 3,padx = 3,pady = 3)
        # textbox.grid(row = 3, column = 0, columnspan = 3,padx = 3,pady = 3)
        # scroll.grid(row = 3, column = 3, sticky = W+E+N+S)

        new_window2.mainloop()
    #End User Interface Summary#

    tampil.geometry("912x400")
    tampil.title("Classification with Long Short-Term Memory")
    tampil.iconbitmap('logo.ico')
    fontStyle = Font(family = "Tempus Sans ITC Regular", size = 48)
    fontStyle2 = Font(family = "Tempus Sans ITC Regular", size = 18)
    judul = Label(tampil, text = "Select Menu", font = fontStyle)
    judul.grid(row = 0, column = 5, columnspan = 3,padx = 3,pady = 3)

    judul2 = Label(tampil, text = "Classification", font = fontStyle2)
    judul2.grid(row = 20, column = 2, columnspan = 3,padx = 3,pady = 3)
    btn1 = Button(tampil, text = "Classification", command = openwindow)
    img1 = PhotoImage(file = 'logo3.png')
    btn1.config(image = img1)
    btn1.grid(row = 10, column = 2, columnspan = 3,padx = 3,pady = 3)

    judul3 = Label(tampil, text = "Summary Model", font = fontStyle2)
    judul3.grid(row = 20, column = 12, columnspan = 3,padx = 3,pady = 3)
    btn2 = Button(tampil, text = "Summary Model", command = openwindow2)
    img2 = PhotoImage(file = 'logo2.png')
    btn2.config(image = img2)
    btn2.grid(row = 10, column = 12, columnspan = 3,padx = 3,pady = 3)

    tampil.mainloop()