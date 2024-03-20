import sys
from game import menu

# check python version requirement
min_ver = (3, 7)
if sys.version_info[:2] < min_ver:
    sys.exit(
        'This game requires Python {}.{}.'.format(*min_ver)
    )

try:
    import panda3d
except:
    sys.exit(
        'Panda3D is required to run'
    )

try:
    from menu import Menu
except:
    sys.exit(
        'Your installation is corrupt'
    )