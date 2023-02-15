import time
import sender

import labor

Interval = 1800
BiGServer = "2466908682.22811.0000"
JSESession = "PJBT_rLlhpzVTJgC2NOGJU01LMC5H8nOHgptTtWfHsIBXknapjz_!1156296110"

# labor.get_labor_list(cookies)
# labor.get_course_list(cookies, 44)

while True:
    data = labor.get_labor_list(BiGServer, JSESession)
    print(data)
    # sender.send_labor_list(data)
    time.sleep(Interval)
