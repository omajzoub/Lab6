from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def sql_database():
  from functions.sqlquery import sql_query
  results = sql_query('''SELECT * FROM data_table''')
  msg = 'Select * from data_table'
  return render_template('sqldatabase.html', results=results, msg=msg)

if __name__ = "__main__":
  app.run(debug=True)