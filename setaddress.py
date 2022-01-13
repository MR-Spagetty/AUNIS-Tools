##
# setaddress.py
# MR-Spagetty

import os
import sys
if sys.version_info < (3, 10):
    raise Exception('to run this programe you are required to use python 3.10\
or greater')

try:
    from tkinter import *
except ImportError:
    raise ImportError('to run this program you need the tkinter module')

try:
    from PIL import ImageTk, Image
except ImportError:
    raise ImportError('to run this program you need the PIL module')

try:
    import json
except ImportError:
    raise ImportError('to run this program you need the json module')

try:
    import re
except ImportError:
    raise ImportError('to run this program you need the re module')

try:
    import random
except ImportError:
    raise ImportError('to run this program you need the random module')

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)


class CommandGenerator:
    DEFAULT_CFG = """{
# when edited you must relaunch the program if it is running
"general": {
    # Randomizes the address on launch
    # and when you change between address types
    # If false glyphs will be set to None on launch
    # and when you change between address types
    "randomize address": true
}
"images": {
    # the width and height of the glyphs
    # used in the edit window
    "small glyph size px": 100,

    # the width and height of the glyphs
    # used in the display window
    "large glyph size px": 300
    }
}"""

    def __init__(self):
        self.config = {}
        self.load_config()
        self.glyph_type = 'MILKYWAY'
        self.glyphs = Glyph(self)
        self.glyph1 = 'None'
        self.glyph2 = 'None'
        self.glyph3 = 'None'
        self.glyph4 = 'None'
        self.glyph5 = 'None'
        self.glyph6 = 'None'
        self.glyph7 = 'None'
        self.glyph8 = 'None'
        if self.config['general']['randomize address'] is True:
            self.randomize_address()

    def randomize_address(self):
        self.glyph1 = random.choice(self.glyphs.GLYPHS[self.glyph_type])
        self.glyph2 = random.choice(self.glyphs.GLYPHS[self.glyph_type])
        self.glyph3 = random.choice(self.glyphs.GLYPHS[self.glyph_type])
        self.glyph4 = random.choice(self.glyphs.GLYPHS[self.glyph_type])
        self.glyph5 = random.choice(self.glyphs.GLYPHS[self.glyph_type])
        self.glyph6 = random.choice(self.glyphs.GLYPHS[self.glyph_type])
        self.glyph7 = random.choice(self.glyphs.GLYPHS[self.glyph_type])
        self.glyph8 = random.choice(self.glyphs.GLYPHS[self.glyph_type])

    def load_config(self):
        CFG_FILE = os.path.join(application_path, 'setaddress.cfg')
        if not os.path.isfile(CFG_FILE):
            with open(CFG_FILE, 'w') as cfg:
                cfg.write(self.DEFAULT_CFG)
        with open(os.path.join(application_path,
                               'setaddress.cfg'), 'r') as config_file:
            config = config_file.read()
            config = ''.join(re.sub(
                "#.*", "", config, flags=re.MULTILINE).split())
            self.config = json.loads(config)

    def generate_command(self):
        return f"""/sgsetaddress map={self.glyph_type} {self.glyph1} \
            {self.glyph2} {self.glyph3} {self.glyph4} {self.glyph5} \
            {self.glyph6} {self.glyph7} {self.glyph8}"""


class Glyph:
    TYPES = ['MILKYWAY', 'PEGASUS', 'UNIVERSE']
    GLYPHS = {'MILKYWAY': ['Crater', 'Virgo', 'Bootes', 'Centaurus', 'Libra',
                           'Serpens Caput', 'Norma', 'Scorpius',
                           'Corona Australis', 'Scutum', 'Sagittarius',
                           'Aquila', 'Microscopium', 'Capricornus',
                           'Piscis Austrinus', 'Equuleus', 'Aquarius',
                           'Pegasus', 'Sculptor', 'Pisces', 'Andromeda',
                           'Triangulum', 'Aries', 'Perseus', 'Cetus',
                           'Taurus', 'Auriga', 'Eridanus', 'Orion',
                           'Canis Minor', 'Monoceros', 'Gemini', 'Hydra',
                           'Lynx', 'Cancer', 'Sextans', 'Leo Minor', 'Leo'],
              'PEGASUS': ['Acjesis', 'Lenchan', 'Alura',
                          'Ca Po', 'Laylox', 'Ecrumig', 'Avoniv', 'Bydo',
                          'Aaxel', 'Aldeni', 'Setas', 'Arami', 'Danami',
                          'Robandus', 'Recktic', 'Zamilloz', 'Subido',
                          'Dawnre', 'Salma', 'Hamlinto', 'Elenami', 'Tahnan',
                          'Zeo', 'Roehi', 'Once El', 'Sandovi', 'Illume',
                          'Amiwill', 'Sibbron', 'Gilltin', 'Ramnon', 'Olavii',
                          'Hacemill', 'Poco Re', 'Abrin', 'Baselai'],
              'UNIVERSE': ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                           'g9', 'g10', 'g11', 'g12', 'g13', 'g14', 'g15',
                           'g16', 'g17', 'g18', 'g19', 'g20', 'g21', 'g22',
                           'g23', 'g24', 'g25', 'g26', 'g27', 'g28', 'g29',
                           'g30', 'g31', 'g32', 'g33', 'g34', 'g35', 'g36']}

    def __init__(self, parent) -> None:
        self.parent = parent
        self.window = Toplevel(parent.window)
        self.window.withdraw()
