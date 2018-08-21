import cgi,cgitb,os,sqlite3
cgitb.enable()
form=cgi.FieldStorage()
aname=form.getvalue('aname')
desc=form.getvalue('desc')
content=form.getvalue('file')
email=""
aid=form.getvalue('aid')
handler = {}
if 'HTTP_COOKIE' in os.environ:
    cookies = os.environ['HTTP_COOKIE']
    cookies = cookies.split('; ')
    for cookie in cookies:
        cookie = cookie.split('=')
        handler[cookie[0]] = cookie[1]
for k in handler:
        email=handler[k]
conn=sqlite3.connect('e-articles.db')
d=conn.execute("select Farea from Faculty where F_email=?",(email,))
data=d.fetchall()
conn.execute("insert into Articles values(?,?,?,?,?,?)",(aid,aname,data[0][0],content,desc,email))
print("Content-type:text/html")
print()
print("""<html><h1>Your article has been published</h1><br><a href="fhome.py"><h1>Return to Home</h2></a></html>""")
conn.commit()
conn.close()
