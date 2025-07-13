import boto3
import os
import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    backup_data = "Sample backup data"
    bucket_name = os.environ['BACKUP_BUCKET']
    key = f"backup-{now}.txt"

    s3.put_object(Bucket=bucket_name, Key=key, Body=backup_data)
    return {
        'statusCode': 200,
        'body': f'Backup created: s3://{bucket_name}/{key}'
    }
