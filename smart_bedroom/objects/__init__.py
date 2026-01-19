"""
Drawable 3D objects for Smart Interactive Bedroom.
"""

# =========================
# FURNITURE & OBJECTS
# =========================
from .bed import draw_bed
from .table import draw_table
from .window import draw_window
from .door import draw_door

# =========================
# POSTERS
# =========================
from .poster import draw_poster          # Poster 1
from .poster_2 import draw_poster_2      # Poster 2
from .poster_3 import draw_poster_3      # Poster 3
from .poster_4 import draw_poster_4      # Poster 4

# =========================
# LIGHT OBJECTS (GEOMETRY)
# =========================
from .table_lamp import draw_table_lamp
from .ceiling_lamp import draw_ceiling_lamp

# =========================
# DECOR & UTILITIES
# =========================
from .curtain import draw_curtain
from .plant import draw_plant
from .workstation import draw_workstation
from .bookshelf import draw_bookshelf
from .trash_bin import draw_trash_bin

# =========================
# STORAGE
# =========================
from .wardrobe import draw_wardrobe, toggle_wardrobe, update_wardrobe

# =========================
# TIME & MECHANICAL
# =========================
from .clock import draw_clock
from .central_ac import draw_ac_central   # ← AC CUSTOM KAMU

# =========================
# EXPORT LIST
# =========================
__all__ = [
    # furniture
    "draw_bed",
    "draw_table",
    "draw_window",
    "draw_door",

    # posters
    "draw_poster",
    "draw_poster_2",
    "draw_poster_3",
    "draw_poster_4",

    # lamps (geometry only)
    "draw_table_lamp",
    "draw_ceiling_lamp",

    # decor
    "draw_curtain",
    "draw_plant",
    "draw_workstation",
    "draw_bookshelf",
    "draw_trash_bin",

    # wardrobe
    "draw_wardrobe",
    "toggle_wardrobe",
    "update_wardrobe",

    # others
    "draw_clock",
    "draw_ac_central",
]
