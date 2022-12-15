from ast import If
import numpy as np
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

# server = 'localhost\sqlexpress' # for a named instance

# server = 'myserver,port' # to specify an alternate port

server = 'collectiusdwhph.database.windows.net'

database = 'dwh_th_2022'

username = 'atiwat'

password = '2a#$dfERat^%'

connect_database = pyodbc.connect(

    'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD=' + password)

# LPC

print(f"RUN PYTHON file: Call Activities" )

sql_cmd_LPC = """

            --Last Call

            SELECT



                a.alternis_portfolioidname as 'Portfolio',

                a.alternis_number as 'Account Number',

                a.alternis_invoicenumber as 'Invoice',

                a.alternis_contactidname as 'Name',

                phone.alternis_phonetypename as 'Phone Type',

                phone_call.phonenumber as 'Phone Number',

                phone_call.alternis_contactdispositionname as 'Contact Disposition',

                phone_call.alternis_calloutcomename as 'Calloutcome',

                phone_call.description as 'Description',

                phone_call.createdon as 'Last Phonecall Createdon',

                phone_call.actualdurationminutes as 'Duration',

                phone_call.subject as 'Phone Subject',

                phone_call.modifiedbyname as 'Agent Call'



            FROM Stage.alternis_account a

            FULL JOIN Stage.alternis_phone phone on phone.alternis_contactid = a.alternis_contactid

            FULL JOIN Stage.phonecall phone_call on phone_call.phonenumber = phone.alternis_number and phone_call.regardingobjectid = a.alternis_accountid

            WHERE a.alternis_portfolioidname IN ('KKP1 TH')

            --Change The Date

            AND phone_call.createdon >= '2022-12-12 00:00:00.000'

            ORDER BY phone_call.createdon DESC

            """
print("SQL querying.....")
df = pd.read_sql(sql_cmd_LPC, connect_database)

#print(df.values.tolist()) 
df.to_excel('test.xlsx',index=False)
print("SQL query sql_cmd_LPC...is DONE!")