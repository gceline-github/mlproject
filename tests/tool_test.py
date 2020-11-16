# -*- coding: UTF-8 -*-
# Import from standard library

import os
import mlproject
import pandas as pd
# Import from our lib
from mlproject.tools import haversine
import pytest

def test_haversine():
    assert haversine(2.380009, 48.865070, 13.3920879, 52.5068068) == 873.8563057261038
