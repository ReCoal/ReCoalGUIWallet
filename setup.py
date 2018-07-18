import sys
from cx_Freeze import setup,Executable

setup(
    name = "ReCoal GUI Wallet",
    version = "0.2.0",
    options = {"build_exe": {"packages":["idna"]}},
    description = "A GUI Wallet for the ReCoal Cryptocurrency",
    executables = [Executable("wallet.py", base = "Win32GUI")])