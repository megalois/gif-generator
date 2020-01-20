# GIF generator

Command-line tool to generate a GIF from a sprite sheet or directory.

usage:

~~~~
gifgen [-h] [--w W] [--t T] [--d D] [--loop LOOP] src
~~~~

positional arguments:
  * src: File or directory name

optional arguments:
  * -h, --help: show this help message and exit
  * --w W: Width of the sprite sheet in number of images. Required for sprite sheets.
  * --t T: Total number of images on the sprite sheet. Required for sprite sheets.
  * --d D: The time to display the current frame of the GIF, in milliseconds.
  * --loop LOOP: The number of times the GIF should loop. Do not set or set to 0 for infinite.

## Installation

You can optionally create an environment.
Then run:

~~~~
$ cd gifgen
$ pip install .
~~~~

## Examples

~~~~
$ gifgen examples/yoga_frog.png --w 8 --t 48
~~~~

~~~~
$ gifgen examples/fox.png --w 6 --t 28 --d 50
~~~~

~~~~
$ gifgen examples/shrine --d 500
~~~~

## Next
* Multi-animation
