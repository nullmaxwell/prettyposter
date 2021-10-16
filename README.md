prettyposter
==============================

A simple object oriented wrapper for the [prettymaps](https://github.com/marceloprates/prettymaps) package to help you generate pretty looking posters for you to print yourself in minutes!

## License Info
**Under no circumstance is this package to be used for commercial purposes.**
This project was created in compliance with the [Creative Commons Attribution-NonCommercial 4.0 International license](http://creativecommons.org/licenses/by-nc/4.0/). The OpenStreetMap and [original repo](https://github.com/marceloprates/prettymaps) credits on the figures are **NOT** to be removed. 

If you love this package consider thanking [ Avatar
Marcelo de Oliveira Rosa Prates](https://github.com/marceloprates), it wouldn't exist without them.

## Built With
A special thanks to the following projects. This project was built using the following open source packages.
- [black](https://github.com/psf/black)
- [prettymaps](https://github.com/marceloprates/prettymaps)
- [matplotlib](https://github.com/matplotlib/matplotlib)

## Getting Started
If you would like to create a pyenv environment you can do so with `make create_environment`. To then initialize that environment you may use `make init_environment`. Please note that this is completely optional.

### Prerequisites
- Dependencies - To install dependencies simply run `make requirements`.

## Usage
Simply import the prettyposter wrapper and instantiate a Poster object with your desired dimensions. 500 DPI is the default pixel density for each image rendered.

Below are the default variable values for a poster if you decide not to specify them:

    poster_height = 15 # in inches
    poster_width = 15 # in inches
    radius = 2500
    poster_theme = "default"

Please note that if you are not seeing much detail with your output, consider double-checking your coordinate to ensure that the signage on your latitude and longitude are correct. 

In a Python file or Jupyter notebook use the following syntax to generate a poster:
    from prettyposter import Poster

    # Variables you can control
    lat = 0.00
    long = 0.00
    """
    Alternatively you may set `location` to an address, city, or state as a string.
    """
    poster_height = 15
    poster_width = 15
    poster_radius = 1900
    poster_theme = "default"

    # Creating the poster
    your_poster = Poster(
        location=(lat, long),
        figsize=(poster_height, poster_width),
        radius=poster_radius,
        theme=poster_theme
    )

    # Exporting the poster
    your_poster.export("myPoster.png")

Exporting your poster will generate an image file with the name your specified in the output folder.

## Example Posters and Themes
There are currently only two themes available, but I plan and encourage others to add more!

You can add your own theme by running `make new_theme`, editing the values marked `#FFFFFF` within the newly generated `new_theme.json`, and using the name of that new theme as an arguemnt to the `Poster` constructor by setting `theme="new_theme"`.

Below are a couple of examples of the exported posters created by this package in different themes.

### Default Theme
![Default Poster Theme of New York City](docs/images/default_sample.png)

### Bluescale Theme
![Bluescale Poster Theme of New York City](docs/images/bluescale_sample.png)
