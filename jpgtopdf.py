from PIL import Image
from tkinter import filedialog

def jpgtopdf():
    images=[]
    chose="yes"
    while(chose=="yes"):
        import_file_path = filedialog.askopenfilename()

        print(import_file_path)
        im = Image.open(import_file_path)
        if im.mode == "RGBA":
            im = im.convert("RGB")
        images.append(im)
        chose=input("Do you want add other photo:(yes/no):")

    print("Enter do you want this pdf save path:")
    out_fname = filedialog.asksaveasfilename(defaultextension='.pdf')
    images[0].save(out_fname, save_all = True, quality=100, append_images = images[1:])






