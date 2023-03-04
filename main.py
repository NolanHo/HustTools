import time
import labor

Interval = 1800
BiGServer = "2785675786.22811.0000"
JSESession = "-UarbWsJPpq1XlCUYGvF5jz5qeSifCtCdz2MbTuXDzBpk2Rwj_pw!-318214320"

# labor.get_labor_list(cookies)
# labor.get_course_list(cookies, 44)

while True:
    data = labor.get_labor_list(BiGServer, JSESession)
    # print(data)
    # sender.send_labor_list(data)
    time.sleep(Interval)
