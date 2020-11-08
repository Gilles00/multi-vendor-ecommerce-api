from datetime import datetime

fmt = '%Y-%m-%d'
d = '2013-09-01'
d1 = datetime.strptime(d, fmt)
print(datetime.today() - d1)
