import requests as rq
# cas验证

def CasGetTicket(url:str, castgc:str, JSESession:str, ICDC):
    cookies = "CASTGC="+castgc+";JSESSIONID="+JSESession+";BIGipServerpool-icdc-cas2"+ICDC
    cookie = {
        "CASTGC": castgc,
        "JSESSIONID": JSESession,
        "BIGipServerpool-icdc-cas2":ICDC,
    }
    ret = rq.get("https://pass.hust.edu.cn/cas/login?service="+url, cookies=cookie)
    print(ret.content.decode('utf8'))