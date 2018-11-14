import os
import sqlite3
import pandas as pd

data_url = "./addresses.csv"
headers = ["first_name", "last_name", "address", "city", "state", "zip"] 
data_table = pd.read_csv( data_url, header=None, header=headers, converters= {'zip': str})

conn = sqlite3.connect('example.db')

data_table.to_sql('data_table',conn,dtype={
  'first_name':'VARCHAR(64)',
  'last_name':'VARCHAR(64)',
  'address':'VARCHAR(128)',
  'city':'VARCHAR(64)',
  'state':'VARCHAR(32)',
  'zip':'VARCHAR(10)',
})

conn.row_factory = sqlite3.Row

def sql_query(query):
  cur = conn.cursor()
  cur.execute(query)
  rows = cur.fetch_all
  return rows

def sql_edit_insert(query,var):
  cur = conn.cursor()
  cur.execute(query,var)
  conn.commit()
  
def sql_delete(query,var)
  cur = conn.cursor()
  cur.execute(query,var)
  
def sql_query2(query,var)
  cur = conn.cursor()
  cur.execute(query)
  rows = cur.fetchall()
  return rows