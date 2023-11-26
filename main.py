from tkinter import filedialog
import pyqrcode
import ttkbootstrap as tbs
from PIL import ImageTk, Image

root = tbs.Window(themename='superhero')
root.title('QR Generator')
root.geometry('400x500')


def create_qr():
    input_path = filedialog.asksaveasfilename(title='Save Image', defaultextension='png',
                                              filetypes=('PNG FILE', ('all files', '*.*')))
    if input_path.endswith('.png'):
        get_code = pyqrcode.create(entry_val.get())
        get_code.png(input_path, scale=5)
    else:
        input_path = f"{input_path}.png"
        get_code = pyqrcode.create(entry_val.get())
        get_code.png(input_path, scale=5)
    global gen_image
    gen_image = ImageTk.PhotoImage(Image.open(input_path))
    lbl_qr.config(image=gen_image)
    entry_val.delete(0, 'end')


def clear():
    entry_val.delete(0, 'end')
    lbl_qr.config(image="")


entry_val = tbs.Entry(root, font=('helvetica', 12), style='dark',  width=200)
entry_val.pack(pady=20, padx=50)

btn_go = tbs.Button(root, command=create_qr, text='Create', style='success', )
btn_go.pack(pady=20)

btn_clr = tbs.Button(root, command=clear, text='Clear', )
btn_clr.pack()

lbl_qr = tbs.Label(root, font='')
lbl_qr.pack(pady=20)

root.mainloop()
