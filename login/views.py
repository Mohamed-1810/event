from django.shortcuts import render, redirect
import mysql.connector as sql
from userevent.views import event
em=''
pwd=''
k=''
# Create your views here.
def loginaction(request):
    global em,pwd,k
    print("hello")
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Tharik@1810",database='event')
        cursor=m.cursor()

        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
    
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        id=''
        
        request.session['my_variable']='Hello World'
        request.session['data']=t[0]
        k=request.session['data']
        
        for i in k:
            id=i 
            # print(i)
            break
        
        request.session['userid']=id 
        data={'id':id}
        if t==():
            return render(request,'error.html')
        else:
            return redirect(event)
            # return render(request,'userevent.html',context=data)
    return render(request,'login_page.html')


