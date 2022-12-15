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



df = pd.read_excel('Eca payment 13.xlsx',sheet_name='Sheet1',header=0,converters={'Revised Ref. 1':str})

for p in df['Master file'].unique():
    df['MM/DD/YY'] = pd.to_datetime(df['MM/DD/YY']).dt.date
    #df['Ref1 (เลขบัตรประชาชน)'].astype(str)
  
    
    df.loc[df['Master file'] == p].to_excel(f'ECA payment {p} 1-13.xlsx',index=False)