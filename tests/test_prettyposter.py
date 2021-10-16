import pytest
from src.prettyposter import Poster


@pytest.fixture
def test_instantiation():
    """Verifies the instantiation of a poster object."""
    test_poster = Poster((39.8283, 98.5795), (5, 5), 2500, "default")
    return test_poster


@pytest.fixture
def test_instantiation_string():
    """Verifies the instantiation of a poster object."""
    test_poster = Poster("New York, New York", (5, 5), 2500, "default")
    return test_poster


def test_classAttributes(test_instantiation) -> Poster:
    """Tests the instantiation of the poster object"""
    assert (test_instantiation.fig != None, "Poster's fig == None")
    assert (test_instantiation.ax != None, "Poster's ax == ax")
    assert (test_instantiation.layers != None, "Poster's layers == None")
    return


def test_reveal(test_instantiation):
    """Verify poster can be shown."""
    try:
        test_instantiation.reveal()
    except:
        print(">>>> Failure to show poster.")
        raise
    return


def test_export_png(test_instantiation):
    """
    Verify the exporting functionality of the poster object as a PNG.
    """
    try:
        test_instantiation.export("test_poster.png")
    except:
        print(">>>> Failure to export poster in default format.")
        raise
    return


def test_export_png(test_instantiation):
    """
    Verify the exporting functionality of the poster object as a SVG.
    """
    try:
        test_instantiation.export("test_poster.svg")
    except:
        print(">>>> Failure to export poster in default format.")
        raise
    return
