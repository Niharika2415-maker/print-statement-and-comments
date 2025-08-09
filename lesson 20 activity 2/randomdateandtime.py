import random
from datetime import datetime
def getRandomDate(startDate, endDate):
 print("Random date and time between", startDate, "and", endDate)
 start_dt = datetime.strptime(startDate, "%d/%m/%Y")
 end_dt = datetime.strptime(endDate, "%d/%m/%Y")
 start_ts = start_dt.timestamp()
 end_ts = end_dt.timestamp()
 random_ts = random.uniform(start_ts, end_ts)
 return datetime.fromtimestamp(random_ts).strftime("%d/%m/%Y %H:%M:%S")
print("Random date:", getRandomDate("1/1/2016", "12/12/2018"))