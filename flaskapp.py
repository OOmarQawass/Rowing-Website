from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def connect_db():
return  sqlite3.connect('membersdb.db')

# Route to display the members from the database
@app.route('/')
def show_members():
    # Connect to the database
    db = connect_db()
    # Create a cursor object
    cur = db.cursor()
    # Execute a query to select all members
    cur.execute('SELECT * FROM member_name')
    # Fetch all rows
    members = cur.fetchall()
    # Close the cursor and database connection
    cur.close()
    db.close()
    # Render the HTML template with the members data
    return render_template('members.html', members=members)

if __name__ == '__main__':
    app.run(debug=True)
