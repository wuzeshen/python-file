from distutils.core import setup
import py2exe

options = {
    "bundle_files":1,
    "compressed":1,
    "optimize":2,
}
setup(
    console = ["backdoorclient.py"],
    options = {"py2exe":options},
    zipfile = None
)
