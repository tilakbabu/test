import cgi,cgitb,os,sqlite3
cgitb.enable()
form=cgi.FieldStorage()
aname=form.getvalue('aname')
genre=form.getvalue('aos')
desc=form.getvalue('desc')
content=form.getvalue('file')
email=""
status="request pending"
count1=0
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
conn.execute("insert into SArticles values(?,?,?,?,?,?,?,?)",(aid,aname,genre,content,desc,email,status,count1))
print("Content-type:text/html")
print()
print("""<html><h1>Your article has been sent to Renowned professors.<br>You have to wait until it is accepted by corresponding professor of your genre</h1><br><a href="shome.py"><h1>Return to Home</h2></a></html>""")
conn.commit()
conn.close()
