import math
import argparse
import os
from PIL import Image

parser = argparse.ArgumentParser(description='Generate GIF from single image.')
parser.add_argument('file_name', type=str, help='File name')
parser.add_argument('w_images', type=int, help='How many times is the image in the horizontal axis of the file?')
parser.add_argument('total_images', type=int, help='How many images are there in the file?')
args = parser.parse_args()

with Image.open(args.file_name) as im:
    w, h = im.size
    h_images = math.ceil(args.total_images / args.w_images)
    assert(w % args.w_images == 0 and h % h_images == 0) # Exact divisions
    sprite_w = w / args.w_images
    sprite_h = h / h_images
    gif_images = []
    for i in range(args.total_images):
        pos_x = i % args.w_images * sprite_w     # (0...7)(0...7)(0...7) * W
        pos_y = i // args.w_images * sprite_h    # (0...0)(1...1)(2...2) * H
        gif_images.append(im.crop((pos_x, pos_y, pos_x + sprite_w, pos_y + sprite_h)))
        fn, _ = os.path.splitext(args.file_name)
    gif_images[0].save('{}.gif'.format(fn),
                       save_all=True,
                       append_images=gif_images[1:],
                       optimize=False, 
                       duration=40, 
                       loop=0)
