rom PIL import Image


def test(image):
   im = Image.open(image) 
   if im.mode == "RGBA":
        im = im.convert("RGB")
    
