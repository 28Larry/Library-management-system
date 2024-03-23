# Import necessary libraries
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="RLAWI",
  database="LIBRARY MANAGEMENT SYSTEM"
)

# Create a cursor object using the cursor() method
cursor = db.cursor()

# Define functions for each operation
def add_book(book_id, title, author,InStock):
    # SQL command to add a book
    sql = "INSERT INTO bookRecord (Bno, Title, Author,InStock) VALUES (A1,MR.ROBOT,CILLIAN,40)"
    values = (book_id, title, author,)
    cursor.execute(sql, values)
    db.commit()

def issue_book(book_id, member_id, issue_date, due_date):
    # SQL command to issue a book
    sql = "INSERT INTO issue (Bno, MemberID, IssueDate, DueDate) VALUES (B1, A1, 9/2/2024, 19/2/2024)"
    values = (book_id, member_id, issue_date, due_date)
    cursor.execute(sql, values)
    db.commit()

def return_book(book_id, member_id):
    # SQL command to return a book
    sql = "DELETE FROM issue WHERE Bno = B1 AND MemberID = AI"
    values = (book_id, member_id)
    cursor.execute(sql, values)
    db.commit()

def add_member(member_id, name,TicketNo):
    # SQL command for   addition of a member
    sql = "INSERT INTO member (MemberID, Name,TicketNo) VALUES (A1,MWENDE,28)"
    values = (member_id, name,TicketNo)
    cursor.execute(sql, values)
    db.commit()



# Close the connection
db.close()


