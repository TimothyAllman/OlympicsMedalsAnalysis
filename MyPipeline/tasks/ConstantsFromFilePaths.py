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
# <h1> Folders paths </h1>
# We could create folders here and then use them
#
# ```
# e.g. ABSOLUTE_PATH_TO_DATA_FOLDER = f"../MyDataFolder"
# ```
#
# but this poses the problem that the `../` part is relative to whatever directory we are running the code from
# and if we run it in different contexts (i.e. when debugging the notebook vs when running the entire piepline) the relative path is different
# i.e. we get this error
#
# >
# > FileNotFoundError: [Errno 2] No such file or directory: '../Data/olympic_athletes.csv'
# >
# in simple terms we could get errors because this is a relative path
#
# To fix we need to create the folder in the pipeline.yaml (similar to how we would create any other shared variable)
# e.g.
#
# ```
#  product:
#      nb: products/{{MY_FOLDER}}/notebooks/ConstantsFromFilePaths.ipynb
#
#      # hardcoded/defined paths for top level folders
#      HARD_CODED_PATH_TO_DATA_FOLDER: ../MyDataFolder
# ```
#
# and then inside this task we bring it into scope using `str()`
#
# ```
# ABSOLUTE_PATH_TO_DATA_FOLDER = str(product["HARD_CODED_PATH_TO_DATA_FOLDER"])
# ```
#
# However this does have the unintended consequence of creating `.MyDataFolder.metadata` files
# inside the same same folder that `MyDataFolder` exists in
# so it might be good to check
# TODO: check if just having ../ in pipeline yaml is better and then use tht and build the various folders in here
# i.e. try
#
# ```
#  product:
#      nb: products/{{MY_FOLDER}}/notebooks/ConstantsFromFilePaths.ipynb
#
#      # hardcoded/defined paths for top level folders
#      HARD_CODED_PATH_TO_TOP_LEVEL_FOLDER: ../
# ```
#
# and then inside
#
# ```
# ABSOLUTE_PATH_TO_TOP_LEVEL_FOLDER = str(product["HARD_CODED_PATH_TO_DATA_FOLDER"])
# ABSOLUTE_PATH_TO_DATA_FOLDER = f"{ABSOLUTE_PATH_TO_TOP_LEVEL_FOLDER}\MyDataFolder"
# ```
#
# %%
ABSOLUTE_PATH_TO_DATA_FOLDER = str(product["HARD_CODED_PATH_TO_DATA_FOLDER"])
ABSOLUTE_PATH_TO_DATA_FOLDER
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
Path(product["ABSOLUTE_PATH_TO_ATHLETES_CSV_FILE"]).parent.mkdir(exist_ok=True, parents=True)
Path(product["ABSOLUTE_PATH_TO_ATHLETES_CSV_FILE"]).write_bytes(pickle.dumps(ABSOLUTE_PATH_TO_ATHLETES_CSV_FILE))
# print output
ABSOLUTE_PATH_TO_ATHLETES_CSV_FILE

# %%
ABSOLUTE_PATH_TO_HOSTS_CSV_FILE = f"{ABSOLUTE_PATH_TO_DATA_FOLDER}/olympic_hosts.csv"
# pickle it to use it later
Path(product["ABSOLUTE_PATH_TO_HOSTS_CSV_FILE"]).parent.mkdir(exist_ok=True, parents=True)
Path(product["ABSOLUTE_PATH_TO_HOSTS_CSV_FILE"]).write_bytes(pickle.dumps(ABSOLUTE_PATH_TO_HOSTS_CSV_FILE))
# print output
ABSOLUTE_PATH_TO_HOSTS_CSV_FILE

# %%
ABSOLUTE_PATH_TO_MEDALS_CSV_FILE = f"{ABSOLUTE_PATH_TO_DATA_FOLDER}/olympic_medals.csv"
# pickle it to use it later
Path(product["ABSOLUTE_PATH_TO_MEDALS_CSV_FILE"]).parent.mkdir(exist_ok=True, parents=True)
Path(product["ABSOLUTE_PATH_TO_MEDALS_CSV_FILE"]).write_bytes(pickle.dumps(ABSOLUTE_PATH_TO_MEDALS_CSV_FILE))
# print output
ABSOLUTE_PATH_TO_MEDALS_CSV_FILE

# %%
ABSOLUTE_PATH_TO_RESULTS_CSV_FILE = f"{ABSOLUTE_PATH_TO_DATA_FOLDER}/olympic_results.csv"
# pickle it to use it later
Path(product["ABSOLUTE_PATH_TO_RESULTS_CSV_FILE"]).parent.mkdir(exist_ok=True, parents=True)
Path(product["ABSOLUTE_PATH_TO_RESULTS_CSV_FILE"]).write_bytes(pickle.dumps(ABSOLUTE_PATH_TO_RESULTS_CSV_FILE))
# print output
ABSOLUTE_PATH_TO_RESULTS_CSV_FILE

# %%

# %%
