from dateutil.relativedelta import datetime

def lambda_handler(event, context):
    now = datetime.now()
    print(now)
    print("DONE")
