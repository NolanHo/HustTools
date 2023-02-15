import requests as rq

rs = rq.get("https://ifulibl.net/fulibl-55261.html")
print(rs.content.decode())