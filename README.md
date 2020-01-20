# GIF generator

Command-line tool to generate a GIF from a sprite sheet or directory.

usage:

~~~~
$ gifgen [-h] [-w WIDTH] [-t TOTAL] [-d DURATION] [-l LOOP] src
~~~~

positional arguments:
  * src: file or directory name

optional arguments:
  * -h, --help: show this help message and exit
  * -w, --width, WIDTH: Width of the sprite sheet in number of images. Required for sprite sheets.
  * -t, --total, TOTAL: Total number of images on the sprite sheet. Required for sprite sheets.
  * -d, --duration, DURATION: The time to display the current frame of the GIF, in milliseconds.
  * -l, --loop, LOOP: The number of times the GIF should loop. Do not set or set to 0 for infinite.

## Installation

You can optionally create an environment.
Then run:

~~~~
$ cd gifgen
$ pip install .
~~~~

## Examples

~~~~
$ gifgen examples/yoga_frog.png -w 8 -t 48
~~~~

~~~~
$ gifgen examples/fox.png --width 6 --total 28 --duration 50
~~~~

~~~~
$ gifgen examples/shrine -d 500 -l 3
~~~~

## Next
* Multi-animation
