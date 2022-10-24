# Write a Python program to get OS name, platform and release information.
import platform
import os
print("the os is ",os.name)
print("the name of os is ",platform.system())
print("the version of os is ",platform.release())