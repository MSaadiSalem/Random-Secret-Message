#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Docs links
# https://docs.python.org/2/library/os.html#os-file-dir
# https://docs.python.org/2/library/shutil.html
import os
import random
import shutil
import sys


def secret_msg_dir(path):
    """ Create a new fresh secret message directory"""

    msg_dir = path + "secret_msg/"
    # https://docs.python.org/2/library/os.path.html#module-os.path
    if os.path.isdir(msg_dir):
        shutil.rmtree(msg_dir)
    os.mkdir(msg_dir)
    return msg_dir


def del_secret_msg_dir(msg_dir):
    """Ask to delete or keep the secret message directory."""

    answer = raw_input(
        "The secret_msg directory has been created. Do you want to keep it? (Y/N)")
    if answer.lower() != "y":
        shutil.rmtree(msg_dir)


def message(msg, path):
    """Create the letter images corresponding to the secret message"""

    msg_lst = list(msg)

    alpha_dir = "alphabet/"
    img_ext = ".jpg"
    msg_dir = secret_msg_dir(path)
    order = 0
    for chr in msg_lst:

        # especial characters
        if chr == " ":
            chr = "space"
        if chr == ".":
            chr = "dot"

        chr_src = path + alpha_dir + chr + img_ext
        renamed_chr = msg_dir + str(order) + img_ext
        # http://www.pythonforbeginners.com/os/python-the-shutil-module
        shutil.copyfile(chr_src, renamed_chr)
        order += 1


def rename_file(path):
    """Remove the random numbers from alphabet letters images"""

    file_list = os.listdir(path)
    for old_name in file_list:
        os.chdir(path)
        new_name = old_name.translate(None, "01234567899")
        os.rename(old_name, new_name)
        # print "Old name:", old_name, "| New name:", new_name
    return file_list


def rand_rename_file(path):
    """Random rename alphabet letters images"""

    file_list = os.listdir(path)
    for old_name in file_list:
        os.chdir(path)
        new_name = str(random.randint(1, 20)) + old_name
        os.rename(old_name, new_name)
        # print "Old name:", old_name, "| New name:", new_name
    return file_list


msg = "hi there are here or there strange ok."


def rand_msg():
    """Return a random message"""

    msg = ["Love does not make the world go round love is what makes the ride worthwhile. Elizabeth Browning",
           "mazuma mazuma",
           "try again",
           "game over",
           "python maze runners"]
    return msg[random.randint(0, len(msg) - 1)]


def msg_dir_open(path):
    """open the secret message directory in OS file manager"""

    # https://docs.python.org/2/library/sys.html
    if sys.platform.startswith("linux"):
        # os.system("xdg-open " + path)
        os.system("gio open " + path)
    if sys.platform.startswith("darwin"):
        os.system("open " + path)
    if sys.platform.startswith("win"):
        os.system("start " + path)


def main():
    path = os.getcwd() + '/'
    rename_file(path + "alphabet/")
    message(rand_msg().lower(), path)
    rand_rename_file(path + "alphabet/")
    msg_dir_open(path + "secret_msg/")
    del_secret_msg_dir(path + "secret_msg/")


main()
