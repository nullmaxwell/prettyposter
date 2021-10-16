import json


class ThemeLoader:
    """
    Loads color themes!
    """

    theme_dir = "src/themes/"

    @classmethod
    def loadTheme(cls, name: str) -> dict:
        """
        Loads a theme from the `themes/` directory.
        """
        try:
            f = open(ThemeLoader.theme_dir + name + ".json")
            data = json.load(f)
            f.close()
        except FileNotFoundError:
            print(">>> Theme not found... Using default theme.")
            f = open(ThemeLoader.theme_dir + "default.json")
            data = json.load(f)
            f.close()

        return data
