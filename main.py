import mysql.connector
Mydb= mysql.connector.connect(host='localhost',
                        user='root',
                        password='1234',
                        database='Bank_management',
                        auth_plugin= "caching_sha2_password")
def OpenAcc():
    n=input("enter the name")
    acc=input("enter an account number")
    db=input("enter the date of birth")
    add=input("enter the address")
    cn=input("enter the contact number")
    ob=int(input("enter the opening balance"))
    data1=(n,acc,db,add,cn,ob)
    data2=(n,ob,acc)
    sql1=('insert into account values(%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values(%s,%s,%s)')
    x=Mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    Mydb.commit()
    print("data entered succesfully")
    main()

def Deposit():
    amount=int(input("enter the amount to be deposited"))
    ac=input("enter the account number")
    a='select balance from amount  Where Account_no=%s'
    data=(ac,)

    x=Mydb.cursor()

    x.execute(a,data)
    result =x.fetchone()
    print(result)
    if result is not None:
        curr_balance = result[0]
        t = curr_balance + amount
        sql = ('UPDATE Amount SET balance = %s WHERE Account_no = %s')
        d = (t , ac)
        x.execute(sql , d)
        Mydb.commit()
    else:
        print("account not found")
    x.close()
    main()
def Withdraw():
    amount = int(input("enter the amount to be withdraw"))
    ac = input("enter the account number")
    a = 'select balance from amount  Where Account_no=%s'
    data = (ac,)
    x = Mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amount
    sql = ('update Amount set balance=%s where Account_no=%s')
    d = (t, ac)
    x.execute(sql, d)
    Mydb.commit()
    main()
def Bal_enquiry():
    ac= input("enter the account number")
    a='select * from amount where Account_no=%s'
    data=(ac,)
    x=Mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    balance=result[-2]
    print('balance in account',ac,'is',balance)
    main()
def Customer_details():
    ac = input("enter the account number")
    a = 'select * from account where Account_no=%s'
    data = (ac,)
    x = Mydb.cursor()
    x.execute(a, data)
    result = x.fetchall()
    for i in result:
        print(i)
    main()

def Close():
    ac = input("enter the account number")
    sql1='delete from account where Account_no=%s'
    sql2='delete from amount where Account_no=%s'
    data=(ac,)
    x = Mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    print("closed")
    Mydb.commit()
    main()


def main():
    print('''
              1.Open a new Account
              2.Deposit An amount
              3.Withdraw an amount
              4. Balance enquiry
              5. Display customer Details
              6.Close an Account''')
    choice=input("Enter the task you have to perform")
    if (choice=='1'):
        OpenAcc()
    elif (choice=='2'):
        Deposit()
    elif (choice=='3'):
        Withdraw()
    elif (choice=='4'):
        Bal_enquiry()
    elif (choice=='5'):
        Customer_details()
    elif (choice=='6'):
        Close()
    else:
        print("Invalid choice")
        main()
main()
