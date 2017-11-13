'''

TERMINALNOTIFIER.

:author: Jake
:license: MIT

'''

__version__ = "1.0"

from tnot import *

import os
import subprocess

proc = subprocess.Popen(["which", "terminal-notifier"], stdout=subprocess.PIPE)
env_bin_path = proc.communicate()[0].strip()

if not os.path.exists(env_bin_path):
	raise exc.NotFound("Dependency terminal-notifier is not installed.")