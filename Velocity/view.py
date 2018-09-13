from tkinter import *
from tkinter import filedialog as tkFileDialog
from PIL import ImageTk, Image
import numpy
import skimage
from skimage import exposure

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Velocity")
        self.pack()

        canvas = Canvas(width=400, height=275, bg='#ffe5e0')
        canvas.place(relx=0, rely=0, anchor=NW)

        canvas2 = Canvas(width=400, height=275, bg='#ffe5e0')
        canvas2.place(relx=1, rely=0, anchor=NE)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        filemenu = Menu(menubar)
        filemenu.add_command(label='Open', command=lambda: self.onOpen(canvas, canvas2))
        menubar.add_cascade(label='File', menu=filemenu)

        b = Button(self.parent, text="Open Image", command=lambda: self.onOpen(canvas, canvas2), fg='white', bg="#D47E6C", borderwidth=0, padx=25, pady=10)
        b.place(relx=0.5, rely=0.9, anchor=S)
        # b.pack()

    def onOpen(self, pannel, pannel2):
        ftypes = [("All files", "*"), ("PNG files", "*.png"), ("JPG files", "*.jpg")]
        dlg = tkFileDialog.Open(self, filetypes=ftypes)
        fl = dlg.show()  # This contains path to the image

        img = self.process_img(fl)
        fixed_img = self.fix_processed_img(fl)

        pannel.create_image(0, 0, anchor=NW, image=img)

        pannel2.create_image(0, 0, anchor=NW, image=fixed_img)

        # pannel2.create_image(0, 0, anchor=NW, image=fixed_useable)

        # show_img(fix_img(open_img(fl)))

    def process_img(self, img):

        original = ImageTk.PhotoImage(Image.open(img).resize((400, 275), Image.ANTIALIAS))
        self.original = original

        return original

    def fix_processed_img(self, path):
        img = Image.open(path)
        array = numpy.array(img)
        img = Image.fromarray(array)
        return img


def main():
    master = Tk()
    app = App(master)
    master.geometry("800x375+300+300")
    mainloop()


'''
def callback():
    print("Callback")


def openfile(file):
    f = open(file)


def main():
    master = Tk()

    menu = Menu(master)
    master.config(menu=menu)

    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Open', command=callback)
    filemenu.add_command(label='Save', command=callback)
    filemenu.add_command(label='Save as', command=callback)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=exit)

    mainloop()
'''

if __name__ == "__main__":
    main()
