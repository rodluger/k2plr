# -*- coding: utf-8 -*-

from __future__ import absolute_import

__version__ = "0.2.9"

try:
    __KPLR_SETUP__
except NameError:
    __KPLR_SETUP__ = False

if not __KPLR_SETUP__:
    __all__ = ["KBJD_ZERO", "EXPOSURE_TIMES", "API", "KOI", "Planet", "Star",
               "LightCurve", "TargetPixelFile", "ld", "huber"]

    from .kplr import KBJD_ZERO, EXPOSURE_TIMES
    from .api import API, KOI, Planet, Star, LightCurve, TargetPixelFile, K2SFF, K2VARCAT, K2SC, EVEREST
    from . import ld, huber
