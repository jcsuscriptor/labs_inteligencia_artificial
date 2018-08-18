from PIL import Image
import os, sys

path = sys.argv[1]


dirs = os.listdir( path )
final_size = 224;


def resize_aspect_fit():
    for item in dirs:
        file_name = os.path.join(path, item)
        if os.path.isfile(file_name):
            print("resize file: ", file_name)
            im = Image.open(file_name)
            f, e = os.path.splitext(file_name)
            size = im.size
            ratio = float(final_size) / max(size)
            new_image_size = tuple([int(x*ratio) for x in size])
            im = im.resize(new_image_size, Image.ANTIALIAS)
            new_im = Image.new("RGB", (final_size, final_size))
            new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
            new_im.save(f + '_resized.jpg', 'JPEG', quality=90)

resize_aspect_fit()