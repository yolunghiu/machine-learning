import time  # 引入time模块

currentTime = time.time()
print("current time is:", currentTime)

localTime = time.localtime(time.time())
localTime_y = time.localtime(time.time()).tm_year
print('local time is: ', localTime)
print('local year is: ', localTime_y)

localtime = time.asctime( time.localtime(time.time()) )
print("local asctime is :", localtime)
