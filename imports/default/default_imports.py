#data processing
import pandas as pd
import numpy as np

#utils
import os
import sys
import time
import json
import random
import warnings
import datetime
import requests

#remove warnings
warnings.filterwarnings('ignore')

#pandas display options 2 decimal places and show all columns
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_columns', None)