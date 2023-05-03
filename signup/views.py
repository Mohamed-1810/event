# from django.shortcuts import render
# import mysql.connector as sql

# fn=''
# ln=''
# s=''
# em=''
# pwd=''
# # print("hello")
# # Create your views here.
# def signaction(request):
#     global fn,ln,s,em,pwd
#     print("hello")
    
#     if request.method=="POST":
        
#         m=sql.connect(host="localhost",user="root",passwd="Tharik@1810",database='event')
#         # if 
#         cursor=m.cursor()
#         d=request.POST
#         for key,value in d.items():
#             if key=="fname":
#                 fn=value 
#             if key=="lname":
#                 ln=value 
#             if key=="email":
#                 em=value 
#             if key=="password":
#                 pwd=value 
#         c="insert into users (first_name,last_name,email,password) Values('{}','{}','{}','{}')".format( fn,ln,em,pwd)
#         cursor.execute(c)
#         m.commit()
#         # return render(request,'login_page.html')

        
#     return render(request,'signup_page.html')
    
from django.shortcuts import render
import mysql.connector as sql
from django.contrib.auth.decorators import login_required 


fn=''
ln=''
s=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Tharik@1810",database='event')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            # print(key,value)
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into users (first_name,last_name,email,password) Values('{}','{}','{}','{}')".format( fn,ln,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page1.html') 

# @login_required(login_url='/login')
def home(request):
    return render(request,'home.html')

