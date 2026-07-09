"""Entry point: python -m gui_app"""
import os
import sys


def _fix_frozen_env():
    """Set GDAL_DATA / PROJ_DATA when running inside a PyInstaller bundle.

    PyInstaller extracts everything