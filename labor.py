import json

import requests as rq


# 返回json信息
def get_labor_list(Big: str, JSE: str):
    url = "http://gcxl.hust.edu.cn/ldjy_wechat/publicBenLabor/student/queryOptionalCourseList.do"
    params = {
        "pageNum": 1,
        "pageSize": 100,
    }
    response = rq.request(method="get", url=url, params=params, cookies={
        "BIGipServerpoolhub-gcxlgl": Big,
        "JSESSIONID": JSE
    })
    cookies = "BIGipServerpoolhub-gcxlgl=" + Big + ";JSESSIONID=" + JSE
    try:
        data = json.loads(response.content.decode())
    except json.JSONDecodeError:
        print("loads failed")
        print(response.content.decode())
        return

    CourseList = data["returnData"]["list"]
    # print(data)

    # 打印空闲课堂
    for i in CourseList:
        # print(i)
        if i["KXKTS"] != 0:
            print("课程名称:{0} 空闲课堂数:{1}".format(i["KCMC"], i["KXKTS"]))
            get_course_list(cookies, i["KCID"])


def get_course_list(cookies, kcid: int):
    url = "http://gcxl.hust.edu.cn/ldjy_wechat/publicBenLabor/student/queryOptionalCLRMList.do"
    params = {
        "pageNum": 1,
        "pageSize": 200,
        "kcid": kcid,
    }
    response = rq.request(method="get", url=url, params=params, cookies=cookies)
    data = json.loads(response.content.decode())
    if data["returnMsg"] == "您好，没有找到符合条件的课堂！":
        print("您好，没有找到符合条件的课堂！")

    Courses = data["returnData"]["list"]
    for i in Courses:
        name = i["kcmc"]
        tea_list = i["clrmTeaList"]
        teas = ""
        for t in tea_list:
            teas += t["zdjsxm"] + " "
        time_place = ""
        plan_list = i["clrmPlanList"]
        for p in plan_list:
            time_place += "{0} {1} {2} {3}\n".format(p["skrq"], p["xqmc"], p["jc"], p["jsmc"])
        available = i["kxrl"]
        capacity = i["xmrl"]
        credit = i["kczxs"]
        print("课程名称:{0} 授课教师:{1} 课堂学时:{2} 课堂容量:{3}/{4}\n"
              "时间地点:\n{5} ".format(name, teas, credit, available, capacity, time_place))
        return {"course_name": name,
                "teacher": teas,
                "time": credit,
                "capacity": "{0}/{1}".format(available, capacity),
                "time_place": time_place}
