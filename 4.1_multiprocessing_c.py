import time
import os
from PIL import Image, ImageFilter

filenames = [
    'images/1.jpg',
    'images/2.jpg',
    'images/3.jpg',
    'images/4.jpg',
    'images/5.jpg',
]

def create_thumbnail(filename, size=(50,50), thumb_dir ='thumbs'):
    # open the image
    img = Image.open(filename)
    
    # apply the gaussian blur filter
    img = img.filter(ImageFilter.GaussianBlur())

    # create a thumbnail
    img.thumbnail(size)
    
    # save the image
    img.save(f'{thumb_dir}/{os.path.basename(filename)}')

    # display a message
    print(f'{filename} was processed...')


if __name__ == '__main__':
    start = time.perf_counter()

    for filename in filenames:
        create_thumbnail(filename)
        
    finish = time.perf_counter()

    print(f'It took {finish-start:.2f} second(s) to finish')