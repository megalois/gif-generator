import math
import argparse
import os
from PIL import Image


DURATION = 200
LOOP = 0

# Command-line arguments
parser = argparse.ArgumentParser(prog='gifgen',
                                 description='GIF Generator. '
                                 'Generate GIF from a sprite sheet or directory.')
parser.add_argument('src', type=str, help='File or directory name')
parser.add_argument('-w', '--width',
                    type=int,
                    help='Width of the sprite sheet in number of images. Required for sprite sheets.')
parser.add_argument('-t', '--total',
                    type=int,
                    help='Total number of images on the sprite sheet. Required for sprite sheets.')
parser.add_argument('-d', '--duration',
                    type=int,
                    help='The time to display the current frame of the GIF, in milliseconds. '
                    f'Default: {DURATION}.')
parser.add_argument('-l', '--loop',
                    type=int,
                    help='The number of times the GIF should loop. Set to 0 for infinite. '
                    f'Default: {LOOP}.')
args = parser.parse_args()


def main(
    src=args.src,
    w_images=args.width,
    total_images=args.total,
    duration=args.duration or DURATION,
    loop=args.loop or LOOP
):

    gif_images = []

    # Sprite Sheet:
    if os.path.isfile(src):
        if w_images is None or total_images is None:
            raise ValueError(
                '--width and --total parameters are required for sprite sheets')
        with Image.open(src) as im:
            w, h = im.size
            h_images = math.ceil(total_images / w_images)
            assert(w % w_images == 0 and h % h_images == 0)  # Exact divisions
            sprite_w = w / w_images
            sprite_h = h / h_images
            for i in range(total_images):
                pos_x = i % w_images * sprite_w     # (0...7)(0...7)(0...7) * W
                pos_y = i // w_images * sprite_h    # (0...0)(1...1)(2...2) * H
                gif_images.append(im.crop((pos_x, pos_y,
                                           pos_x + sprite_w, pos_y + sprite_h)))
            fn, _ = os.path.splitext(src)
    # Folder:
    else:
        gif_images = [Image.open(os.path.join(src, f))
                      for f in os.listdir(src)]
        fn = src

    gif_images[0].save('{}.gif'.format(fn),
                       save_all=True,
                       append_images=gif_images[1:],
                       optimize=False,
                       duration=duration,
                       loop=loop)
