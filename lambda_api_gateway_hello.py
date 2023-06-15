

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': {"name": "World"},
        'headers': {
            'Content-Type': 'application/json',
        },
    }

