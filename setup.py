from setuptools import setup
import sys

ANTLR_RUNTIME_VERSION = '4.8'

if sys.version_info.major == 3:
    antlr_runtime = "antlr4-python3-runtime"
else sys.version_info.major == 2:
    antlr_runtime = "antlr4-python2-runtime"

setup(
    name="antlr4-python-runtime",
    version=ANTLR_RUNTIME_VERSION,
    description="A stub package for antlr4 python runtime that requires the correct python version",
    install_requires=["{}=={}".format(antlr_runtime, ANTLR_RUNTIME_VERSION)]
)
