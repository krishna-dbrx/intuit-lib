# Databricks notebook source
from lib import libFunction
libFunction()

# COMMAND ----------

/Workspace/Repos/krishna.satyavarapu@databricks.com/intuit-pvc/

# COMMAND ----------

import os
import sys
print("Before", os.path.abspath("."))
module_path = os.path.abspath(os.path.join('/Workspace/Repos/krishna.satyavarapu@databricks.com/intuit-pvc/'))
if module_path not in sys.path:
    sys.path.append(module_path)
print("module path", module_path)

from lib_file import functionFile
functionFile()


# COMMAND ----------

from lib_file import functionFile
functionFile()

# COMMAND ----------


