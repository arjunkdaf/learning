from datetime import *
from dateutil.relativedelta import *
agora = datetime.now()
print(agora)

agora = agora + relativedelta(months=1, weeks=1, hour=10)

print(agora)