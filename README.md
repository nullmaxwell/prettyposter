prettyposter
==============================

A simple object oriented wrapper for the [prettymaps](https://github.com/marceloprates/prettymaps) package to help you generate pretty looking posters in minutes!

## Built With
A special thanks to the following projects. This project was built using the following open source packages.
- [black](https://github.com/psf/black)
- [prettymaps](https://github.com/marceloprates/prettymaps)
- [matplotlib](https://github.com/matplotlib/matplotlib)

## Getting Started
If you would like to create a pyenv environment you can do so with `make create_environment`. To then initialize that environment you may use `make init_environment`. Please note that this is completely optional.

### Prerequisites
- dependencies - To install dependencies simply run `make requirements`.

## Usage
Simply import the prettyposter wrapper and instantiate a Poster object with your desired dimensions. 500 DPI is the default pixel density for each image rendered.

Please note that if you are not seeing much detail with your output, consider double-checking your coordinate to ensure that the signage on your latitude and longitude are correct. 

## Example Posters

### Default Theme
![Default Poster Theme of New York City](docs/images/default_sample.png)

### Bluescale Theme
![Bluescale Poster Theme of New York City](docs/images/bluescale_sample.png)
