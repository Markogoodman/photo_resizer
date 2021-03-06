from PIL import Image, ImageOps, ExifTags
import os

def rotate(image):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = image._getexif()
        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)
        return image

    except (AttributeError, KeyError, IndexError):
        return image


def auto_add_border(img, color):
    width, height = img.size
    m = max(width, height)
    return ImageOps.expand(img, border=((m-width)//2, (m-height)//2), fill=color)

if __name__ == '__main__':
    print("put this file next to your photo directory")
    color = input("Border color (black, white...): ")
    directory = input("Input photo directory path: ")

    # create output folder
    output_path = "output"
    try:
        os.stat(output_path)
    except:
        os.mkdir(output_path)

    for filename in os.listdir(directory):
        print("processing " + filename + " ...")
        path = os.path.join(directory, filename)
        img = Image.open(path)
        img = rotate(img)
        img = auto_add_border(img, color)
        img.save(os.path.join(output_path, 'new_' + filename), quality=100)






