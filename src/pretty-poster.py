from prettymaps import *
from matplotlib import pyplot as plt
from matplotlib import patheffects as pe

# import matplotlib.font_manager as fm


class Poster:
    """
    This module creates a beautiful poster for you to print on your dumb little wall.
    """

    # Class Attributes

    # Static Layers, in the future there will be options
    map_layers = {
        # Controls the drawing mode ,{} That is, it is equivalent to circular drawing mode
        "perimeter": {},
        # The following parameters are used to define from OsmStreetMap Select the acquired vector layer features
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

    """
    Beef
    """

    def __init__(
        self,
        coordinates: tuple or str,
        figsize: tuple = (14, 14),
        show: bool = False,
        radius: int = 2500,
        annotation: str = None,
    ) -> None:
        """
        Construction of the poster object.
        """
        self.fig, self.ax = plt.subplots(figsize=figsize, constrained_layout=True)
        self.layers = plt.plot(
            coordinates, radius, ax=self.ax, layers=Poster.map_layers
        )

        if annotation != None:
            print("Placeholder for annotations.")
        if show:
            Poster.ax.show()
        pass

    def reveal(self):
        """
        Reveals the poster on-screen.
        """
        return self.ax.show()

    def export(self, filename):
        """
        Exports the poster to a given location.
        """
        try:
            self.savefig(filename + ".svg", dpi=500)
        except:
            print("Invalid filepath")
            raise
        pass
