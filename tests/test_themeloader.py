import pytest
from src.themeloader import ThemeLoader


def test_loadTheme():
    """Verifies that the default theme can be loaded."""
    test_theme = ThemeLoader.loadTheme("default")
    assert (test_theme != None, "Theme not loaded...")


def test_loadInvalidTheme():
    """Verifies that the default theme is loaded even when user provides invalied theme reference."""
    test_theme = ThemeLoader.loadTheme("invalid_theme")
    assert (test_theme != None, "Theme not loaded...")
