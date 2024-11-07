#!/usr/bin/env python3
import sys, os, platform
import folder_navigation

p_name = "Linux Administration"
p_des = "This program is designed to manage Linux"


def p_id():
    print(p_name.center(50, "-"))
    print(p_des, "(Hex = %s , Size = %s)" % (hex(id(p_des)), sys.getsizeof(p_des)))
    print("PID = {}".format(os.getpid()))
    print(f"CMD = {os.getcwd()}")
    print("OS = %s(%s%s)" % (platform.system(),platform.release(),platform.architecture()))


def Load_module():
    print("List of loaded modules ...")
    print(
        folder_navigation.__name__
        + " "
        + "-" * 3
        + ">  "
        + repr(folder_navigation.__doc__)
    )


def main():
    p_id()
    Load_module()


if __name__ == "__main__":
    main()
