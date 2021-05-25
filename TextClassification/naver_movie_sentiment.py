# https://wikidocs.net/44249
# Naver Movie Review Sentiment Analysis

import pandas as pd
import numpy as np
# %matplotlib inline
import matplotlib.pyplot as plt
import re
import urllib.request
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

