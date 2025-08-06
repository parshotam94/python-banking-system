import random #for random number generation
import qrcode as qr #for qrcode

#mysql connector
import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="267694",
  db="bankmgt"
)
mycursor=mydb.cursor()

# mycursor.execute("""
#                  CREATE TABLE mainBank(
#                  account_no INT PRIMARY KEY, 
#                  first_name VARCHAR(20), 
#                  last_name VARCHAR(20),
#                  address VARCHAR(30), 
#                  balance NUMERIC(20,2), 
#                  Date DATETIME DEFAULT CURRENT_TIMESTAMP
#               )
#         """)

# sql="INSERT INTO mainBank(account_no, first_name, last_name, address, balance) VALUES (%s, %s, %s, %s, %s)"
# val=[
#   ('1840','Prshotm','Manhas','Doda', '10000'),
#   ('1850','Kamran','Akmal','Doda', '8000'),
#   ('1860','Manpreet','Singh','Rajouri', '9000')
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"row(s) inserted.")


class Bank:
  def createAcc(self):
    print("*** Welcome to the XYZ Bank ***")
    accNo=random.randint(1000,9999)
    fname=input("Enter first name: ")
    lname=input("Enter last name: ")
    addr=input("Enter address: ")
    bal=input("Enter inital balance(500): ")
    sql="SELECT balance FROM mainBank WHERE account_no=%s"
    mycursor.execute(sql,(accNo,))
    myresult=mycursor.fetchone()
    if myresult:
      print("Account Number already exist.")
    else:
      sql="INSERT INTO mainBank(account_no, first_name, last_name, address, balance) VALUES (%s, %s, %s, %s, %s)"
      val=(accNo, fname, lname, addr, bal)
      mycursor.execute(sql, (val))
      mydb.commit()
      print("Thank you for creating an account in our bank.")
      print("Your Account Number is: XXXXXXXXXXXX",accNo)
      print(mycursor.rowcount, "row(s) inserted.")

  def balance(self):
    accNo=input("Enter 4-digit account Number: ")
    sql="SELECT balance FROM mainBank WHERE account_no=%s"
    mycursor.execute(sql,(accNo,)) #this accNo must be tuple
    myresult=mycursor.fetchone()
    if myresult:
      print("Account found! ")
      print("Your balance is: Rs.",myresult[0])
    else:
      print("No record found!")

  def credit(self):
    accNo=input("Enter 4-digit account Number: ")
    sql="SELECT balance FROM mainBank WHERE account_no=%s"
    mycursor.execute(sql,(accNo,)) #this accNo must be tuple
    myresult=mycursor.fetchone()
    bal=myresult[0]
    amt=int(input("Enter amount you want to credit: "))
    int(bal)
    bal+=amt
    str(bal)
    print(f"Rs.{amt} credited to your account number XXXXXXXXXXXX{accNo}")
    print("Total Balance, Rs.",bal)
    sql="UPDATE mainBank SET balance=%s WHERE account_no=%s"
    mycursor.execute(sql,(bal, accNo,))
    mydb.commit()

  def debit(self):
    accNo=input("Enter 4-digit account Number: ")
    sql="SELECT balance FROM mainBank WHERE account_no=%s"
    mycursor.execute(sql,(accNo,)) #this accNo must be tuple
    myresult=mycursor.fetchone()
    bal=myresult[0]
    int(bal)
    amt=int(input("Enter amount you want to debit: "))
    if amt>bal:
      print("Insufficient Balance")
    else:
      bal-=amt
      str(bal)
      print(f"Rs.{amt} debited from your account number XXXXXXXXXXXX{accNo}")
      print("Total Balance, Rs.",bal)
      sql="UPDATE mainBank SET balance=%s WHERE account_no=%s"
      mycursor.execute(sql,(bal, accNo,))
      mydb.commit()
    
  def createQr(self):
    accNo=input("Enter 4-digit account Number: ")
    sql="SELECT first_name FROM mainBank WHERE account_no=%s"
    mycursor.execute(sql,(accNo,)) #this accNo must be tuple
    myresult=mycursor.fetchone()
    if myresult:
      data=f"Name: {myresult[0]}\nAccount Number: {accNo}"
      img=qr.make(data)
      
      img.save("QR-CODE.png") 
      print("QR for you account has been generated. Check you Gallery.")


  
p1=Bank()
print("Enter 1 for creating account")
print("Enter 2 for Balance enquriy")
print("Enter 3 to Credit")
print("Enter 4 to Debit")
print("Enter 5 to generate QR")
print("Enter 0 to exit")
while(True):
  a=int(input("Enter choice: "))
  if a==1:
    p1.createAcc()
  elif a==2:
    p1.balance()
  elif a==3:
    p1.credit()
  elif a==4:
    p1.debit()
  elif a==5:
    p1.createQr()
  elif a==0:
    break
  else:
    print("invalid Choice!")



