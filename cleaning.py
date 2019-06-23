#!/usr/local/bin/python3

import missingno as msno
import pandas as pd
from CLEARapi import get_info

data = get_info()

Crime = pd.DataFrame(data)

msno.matrix(Crime)

print(Crime.tail())