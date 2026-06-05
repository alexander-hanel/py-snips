

import json 

def load_json(file_path):
    pass


def write_json(file_path):
    pass 


def test_import():
    pass 

import glob 

def glob_dir(file_path="."):
    for _file in glob.glob(file_path + "/*"):
        print(_file)
# glob_dir("data")

def glob_dir_recur(file_path="."):
    #  glob.glob('**/*.txt', recursive=True)
    for _file in glob.glob(file_path + "/**/*", recursive=True):
        print(_file)
glob_dir_recur("data")

import ctypes 

def cytypes_math():
    pass


def cytype_enum():
    pass


import struct 
def read_value_little_endian():
    pass 


# import yara 
def scan_buffer_yara(buffer, yara):
    pass


import logging 
def logging_example():
    pass 

import yaml 
def load_yaml():
    pass 


from enum import IntEnum

from collections import namedtuple
from collections import deque

# datetime 

# gzip 

# zip 

# crc 

# sha256 hash 

# list comphrension 

# pefile 

def xor():
    pass 

# isinstance 

# set theory 
# is_subset 
# 
