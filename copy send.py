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


src_folder = "C:\\Users\\chatchapol.p\\Desktop\\New folder"


#1
dst_folder = "Z:\\FTPS\\ABIZ\\ECA Payment\\Nov 22"
pattern = src_folder + "\*ABIZ*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)

#2
dst_folder = "Z:\\FTPS\\ACT\\ECA Payment\\Nov 22"
pattern = src_folder + "\*ACT*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)
  
#3    
dst_folder = "Z:\\FTPS\\APS\\ECA Payment\\Nov 22"
pattern = src_folder + "\*APS*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
#4
dst_folder = "Z:\\FTPS\\ART\\ECA Payment\\Nov 22"
pattern = src_folder + "\*ART*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)

#5
dst_folder = "Z:\\FTPS\\CHOT\\ECA Payment\\Nov 22"
pattern = src_folder + "\*CHOT*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)
  
#6    
dst_folder = "Z:\\FTPS\\EKN\\ECA Payment\\Nov 22"
pattern = src_folder + "\*EKN*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
#7    
dst_folder = "Z:\\FTPS\\LAW\\ECA Payment\\Nov 22"
pattern = src_folder + "\*LAW*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
  #8  
dst_folder = "Z:\\FTPS\\MIT\\ECA Payment\\Nov 22"
pattern = src_folder + "\*MIT*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
  #9  
dst_folder = "Z:\\FTPS\\MMN\\ECA Payment\\Nov 22"
pattern = src_folder + "\*MMN*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
    #10
dst_folder = "Z:\\FTPS\\NSR\\ECA Payment\\Nov 22"
pattern = src_folder + "\*NSR*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
    #11
dst_folder = "Z:\\FTPS\\PAT\\ECA Payment\\Nov 22"
pattern = src_folder + "\*PAT*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
    #12
dst_folder = "Z:\\FTPS\\PNR\\ECA Payment\\Nov 22"
pattern = src_folder + "\*PNR*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
 #13   
dst_folder = "Z:\\FTPS\\PRE\\ECA Payment\\Nov 22"
pattern = src_folder + "\*PRE*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
    #14
dst_folder = "Z:\\FTPS\\PSC\\ECA Payment\\Nov 22"
pattern = src_folder + "\*PSC*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
    #15
dst_folder = "Z:\\FTPS\\PWM\\ECA Payment\\Nov 22"
pattern = src_folder + "\*PWM*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
  #16  
dst_folder = "Z:\\FTPS\\PWS\\ECA Payment\\Nov 22"
pattern = src_folder + "\*PWS*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
    #17
dst_folder = "Z:\\FTPS\\SPB\\ECA Payment\\Nov 22"
pattern = src_folder + "\*SPB*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
    #18"
dst_folder = "Z:\\FTPS\\STW\\ECA Payment\\Nov 22"
pattern = src_folder + "\*STW*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
    #19
dst_folder = "Z:\\FTPS\\TBS\\ECA Payment\\Nov 22"
pattern = src_folder + "\*TBS*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
    #20
dst_folder = "Z:\\FTPS\\TOP\\ECA Payment\\Nov 22"
pattern = src_folder + "\*TOP*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
    #21
dst_folder = "Z:\\FTPS\\TOP\\ECA Payment\\Nov 22"
pattern = src_folder + "\*TOP2*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
    #22
dst_folder = "Z:\\FTPS\\TTK\\ECA Payment\\Nov 22"
pattern = src_folder + "\*TTK*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
    #23
dst_folder = "Z:\\FTPS\\UPP\\ECA Payment\\Nov 22"
pattern = src_folder + "\*UPP*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    
    #24
dst_folder = "Z:\\FTPS\\WEL\\ECA Payment\\Nov 22"
pattern = src_folder + "\*WEL*"
for files in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(files)
    shutil.copy(files, dst_folder)    