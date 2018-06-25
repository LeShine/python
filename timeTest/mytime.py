import time

myTime = time.time()
print('从1970到现在过去了', myTime, 's')

second = int(myTime) % 60
minutes = int(myTime)//60
hours = int(minutes)//60
minutes = minutes % 60
days = int(hours)//24
hours = hours % 24
month = days//30
days = days % 30
years = int(month)//12
month = month % 12


print('从1970年到现在过去了',
      years, '年',
      days, '日',
      hours, '小时',
      minutes, '分钟',
      second, '秒',
      )
