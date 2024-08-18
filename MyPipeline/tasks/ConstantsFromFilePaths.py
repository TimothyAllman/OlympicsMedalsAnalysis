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
upstream = None

# This is a placeholder, leave it as None
product = None


# %%
# your code here...
from pathlib import Path
import pickle


# %% [markdown]
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <h1> Folders we will create and use </h1>
# %%
ABSOLUTE_PATH_TO_DATA_FOLDER = f"../Data"

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <br>
# <h1> Paths to source data filesn </h1>

# %%
ABSOLUTE_PATH_TO_ATHLETES_CSV_FILE = f"{ABSOLUTE_PATH_TO_DATA_FOLDER}/olympic_athletes.csv"
# pickle it to use it later
Path(product["ABSOLUTE_PATH_TO_ATHLETES_CSV_FILE"]).parent.mkdir(exist_ok=True,parents=True)
Path(product["ABSOLUTE_PATH_TO_ATHLETES_CSV_FILE"]).write_bytes(pickle.dumps(ABSOLUTE_PATH_TO_ATHLETES_CSV_FILE))
#print output
ABSOLUTE_PATH_TO_ATHLETES_CSV_FILE

# %%
ABSOLUTE_PATH_TO_HOSTS_CSV_FILE= f"{ABSOLUTE_PATH_TO_DATA_FOLDER}/olympic_hosts.csv"
# pickle it to use it later
Path(product["ABSOLUTE_PATH_TO_HOSTS_CSV_FILE"]).parent.mkdir(exist_ok=True,parents=True)
Path(product["ABSOLUTE_PATH_TO_HOSTS_CSV_FILE"]).write_bytes(pickle.dumps(ABSOLUTE_PATH_TO_HOSTS_CSV_FILE))
#print output
ABSOLUTE_PATH_TO_HOSTS_CSV_FILE

# %%
ABSOLUTE_PATH_TO_MEDALS_CSV_FILE = f"{ABSOLUTE_PATH_TO_DATA_FOLDER}/olympic_medals.csv"
# pickle it to use it later
Path(product["ABSOLUTE_PATH_TO_MEDALS_CSV_FILE"]).parent.mkdir(exist_ok=True,parents=True)
Path(product["ABSOLUTE_PATH_TO_MEDALS_CSV_FILE"]).write_bytes(pickle.dumps(ABSOLUTE_PATH_TO_MEDALS_CSV_FILE))
#print output
ABSOLUTE_PATH_TO_MEDALS_CSV_FILE

# %%
ABSOLUTE_PATH_TO_RESULTS_CSV_FILE = f"{ABSOLUTE_PATH_TO_DATA_FOLDER}/olympic_results.csv"
# pickle it to use it later
Path(product["ABSOLUTE_PATH_TO_RESULTS_CSV_FILE"]).parent.mkdir(exist_ok=True,parents=True)
Path(product["ABSOLUTE_PATH_TO_RESULTS_CSV_FILE"]).write_bytes(pickle.dumps(ABSOLUTE_PATH_TO_RESULTS_CSV_FILE))
#print output
ABSOLUTE_PATH_TO_RESULTS_CSV_FILE

# %%

# %%
