import cgi,cgitb,os,sqlite3
cgitb.enable()
form=cgi.FieldStorage()
id1=form.getvalue('id')
conn=sqlite3.connect('e-articles.db')
c=conn.execute("select Area from SArticles where Aid=?",(id1,))
c1=c.fetchall()
d=conn.execute("select count(Farea) from Faculty where Farea=?",(c1[0][0],))
d1=d.fetchall()
n=d1[0][0]
d2=conn.execute("select count1 from SArticles where Aid=?",(id1,))
d3=d2.fetchall()
m=d3[0][0]
if m==(int)(n/2):
    conn.execute("update SArticles set status='accepted' where Aid=?",(id1,))
else:
    conn.execute("update SArticles set count1=count1+1 where Aid=?",(id1,))
conn.commit()
conn.close()
print("Content-type:text/html")
print()
print("""<html><h1>The Article has been accepted by you<br>will be available for all the users if atleast half of the faculty from the same genre accepted it</h1><br><a href="fhome.py"><h2>Return to Home</h2></a></html>""")




