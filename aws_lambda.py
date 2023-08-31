import json
import random
import time

def lambda_handler(event, context):
    time.sleep(random.randint(1,5))
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }

