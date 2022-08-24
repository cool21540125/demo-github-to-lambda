from datetime import datetime
from dateutil.relativedelta import *

def lambda_handler(event, context):
    now = datetime.now()
    now += relativedelta(months=1)
    print(now)
    print("DONE")
