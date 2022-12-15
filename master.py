from ast import If

import datetime

import glob

import os

import shutil

from tkinter import HIDDEN

import uuid

from doctest import DocFileTest

from email.utils import format_datetime

from math import fabs

from operator import index

from pickle import NONE

import pandas as pd

import pyodbc

import xlsxwriter

from matplotlib.pyplot import axis
import xlrd
import jinja2



df = pd.read_excel("TMB2_Monthly Master Dec'22 OG.xlsb")

for p in df['OA(Dec22)'].unique():
    
    
    
    df.loc[df['OA(Dec22)'] == p].to_excel(f'ECA payment {p} Final.xlsx',index=False)
