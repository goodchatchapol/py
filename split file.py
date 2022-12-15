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

import jinja2



df = pd.read_excel('payment k 16.xlsx')


for p in df['Master file'].unique():
    df.loc[df['Master file'] == p].to_excel(f'ECA payment {p} Final.xlsx',index=False)