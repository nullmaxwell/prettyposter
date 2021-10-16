from prettymaps import *
from matplotlib import pyplot as plt
from matplotlib import patheffects as pe
from src.themeloader import ThemeLoader


class Poster:
    """
    This module creates a beautiful poster for you to print or use as a wallpaper.


    ## Parameters
    `coordinates` tuple or str:
        Location to depict on poster.
        tuple: (lat: float, long: float)

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

    osm_credit = {"color": "#2F373700"}

    def __init__(
        self,
        coordinates: any,
        figsize: tuple = (14, 14),
        radius: int = 2500,
        theme: str = "default",
    ):
        """
        Construction of the poster object.
        """
        fig, ax = plt.subplots(figsize=figsize, constrained_layout=True)
        layers = plot(
            coordinates,
            radius=int(radius),
            ax=ax,
            layers=Poster.map_layers,
            drawing_kwargs=ThemeLoader.loadTheme(theme),
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
