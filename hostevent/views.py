from django.shortcuts import render
import mysql.connector as sql
from login.views import loginaction  

event_n=''
date=''
time=''
location=''


# Create your views here.
def host(request):
    global event_n,date,time,location 
    userid=request.session.get('userid')
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Tharik@1810",database='event')
        cursor=m.cursor()
        
        d=request.POST
        for key,value in d.items():
            if key=="event_n":
                event_n=value 
            if key=="date":
                date=value 
            if key=="time":
                time=value 
            if key=="location":
                location="value"
        # print(type(date))
        c="insert into post (event_n,date,location,time,userid) Values('{}','{}','{}','{}','{}')".format(event_n,date,location,time,userid)
        cursor.execute(c)
        m.commit()
    return render(request,'hostevent.html')