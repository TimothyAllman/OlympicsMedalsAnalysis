# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# Add description here
#
# *Note:* You can open this file as a notebook (JupyterLab: right-click on it in the side bar -> Open With -> Notebook)


# %%
# Uncomment the next two lines to enable auto reloading for imported modules
# # %load_ext autoreload
# # %autoreload 2
# For more info, see:
# https://docs.ploomber.io/en/latest/user-guide/faq_index.html#auto-reloading-code-in-jupyter

# %% tags=["parameters"]
# If this task has dependencies, list them them here
# (e.g. upstream = ['some_task']), otherwise leave as None.
upstream = [
    "ConstantsFromFilePaths"
]

# This is a placeholder, leave it as None
product = None


# %%
# your code here...

# %%
# python imports
from pathlib import Path
import pickle
import pandas as pd

# %%
# unpickle stored shared variables
_ABSOLUTE_PATH_TO_MEDALS_CSV_FILE = pickle.loads(upstream["ConstantsFromFilePaths"]["ABSOLUTE_PATH_TO_MEDALS_CSV_FILE"].read_bytes())

# %%
dfMedals = pd.read_csv(_ABSOLUTE_PATH_TO_MEDALS_CSV_FILE)

# %%
MEDALS_DF = dfMedals
# pickle it to use it later
Path(product["MEDALS_DF"]).parent.mkdir(exist_ok=True,parents=True)
Path(product["MEDALS_DF"]).write_bytes(pickle.dumps(MEDALS_DF))
#print output
MEDALS_DF

# %%
