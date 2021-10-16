from prettymaps import *
from matplotlib import pyplot as plt
from matplotlib import patheffects as pe

# import matplotlib.font_manager as fm


class Poster:
    """
    This module creates a beautiful poster for you to print or use as a wallpaper.


    ## Parameters
    `coordinates` tuple or str:
        Location to depict on poster.
        tuple: (lat: float, long: float)
        str: "City, State" or "City, Country"

    `figsize` tuple of ints:
        (L, W) of poster in inches to be rendered.

    `radius` int:
        Radius of the poster (roundedness).
        The higher the value the more round the map area is.
    """

    # Class Attributes

    # Static Layers, in the future there will be options
    map_layers = {
        # Controls the drawing mode ,{} That is, it is equivalent to circular drawing mode
        "perimeter": {},
        # The following parameters are used to define from OsmStreetMap Select the acquired vector layer features , If you don't understand it, you can copy it without change
        "streets": {
            "custom_filter": '["highway"~"motorway|trunk|primary|secondary|tertiary|residential|service|unclassified|pedestrian|footway"]',
            "width": {
                "motorway": 5,
                "trunk": 5,
                "primary": 4.5,
                "secondary": 4,
                "tertiary": 3.5,
                "residential": 3,
                "service": 2,
                "unclassified": 2,
                "pedestrian": 2,
                "footway": 1,
            },
        },
        "building": {
            "tags": {"building": True, "landuse": "construction"},
            "union": False,
        },
        "water": {"tags": {"natural": ["water", "bay"]}},
        "green": {
            "tags": {
                "landuse": "grass",
                "natural": ["island", "wood"],
                "leisure": "park",
            }
        },
        "forest": {"tags": {"landuse": "forest"}},
        "parking": {
            "tags": {"amenity": "parking", "highway": "pedestrian", "man_made": "pier"}
        },
    }

    """
    Below are the styling options for the poster.
    """
    drawing_kwargs = {
        "background": {
            "fc": "#F2F4CB",
            "ec": "#dadbc1",
            "hatch": "ooo...",
            "zorder": -1,
        },
        "perimeter": {
            "fc": "#F2F4CB",
            "ec": "#dadbc1",
            "lw": 0,
            "hatch": "ooo...",
            "zorder": 0,
        },
        "green": {"fc": "#D0F1BF", "ec": "#2F3737", "lw": 1, "zorder": 1},
        "forest": {"fc": "#64B96A", "ec": "#2F3737", "lw": 1, "zorder": 1},
        "water": {
            "fc": "#a1e3ff",
            "ec": "#2F3737",
            "hatch": "ooo...",
            "hatch_c": "#85c9e6",
            "lw": 1,
            "zorder": 2,
        },
        "parking": {"fc": "#F2F4CB", "ec": "#2F3737", "lw": 1, "zorder": 3},
        "streets": {"fc": "#2F3737", "ec": "#475657", "alpha": 1, "lw": 0, "zorder": 3},
        "building": {
            "palette": ["#FFC857", "#E9724C", "#C5283D"],
            "ec": "#2F3737",
            "lw": 0.5,
            "zorder": 4,
        },
    }

    osm_credit = {"color": "#2F373700"}

    def __init__(self, coordinates: any, figsize: tuple = (14, 14), radius: int = 2500):
        """
        Construction of the poster object.
        """
        fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
        layers = plot(
            coordinates,
            radius=int(radius),
            ax=ax,
            layers=Poster.map_layers,
            drawing_kwargs=Poster.drawing_kwargs,
            osm_credit=Poster.osm_credit,
        )

        self.layers = layers
        self.fig = fig
        self.ax = ax

        return

    def reveal(self):
        """
        Reveals the poster on-screen.
        """
        return self.fig.show()

    def export(self, filename, ext: str = ".svg"):
        """
        Exports the poster to a given location.
        """
        try:
            self.fig.savefig("output/" + filename + ext, dpi=500)
        except:
            print("Invalid filepath")
            raise
        pass
