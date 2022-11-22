from setuptools import setup

setup(name='gifgen',
      version='0.1',
      description='GIF generator command-line utility',
      url=None,
      author='megalois',
      author_email='santi@systemaris.com',
      license='MIT',
      packages=['gifgen'],
      zip_safe=False,
      entry_points = {
          'console_scripts': ['gifgen=gifgen.gifgen:main'],
      },
      install_requires=[
          'Pillow==9.3.0'
      ])
