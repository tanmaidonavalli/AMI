from __future__ import print_function
import boto3
import io
import json
import subprocess
from packerpy import PackerExecutable
from botocore.exceptions import ClientError

BUCKET_NAME = 'demo-s3lambda'
def lambda_handler(event, context):
    ssm = boto3.client('ssm')
    s3 = boto3.resource('s3')
    s3Client = boto3.client('s3')
    parameter = ssm.get_parameter(Name='/GoldenAMI/Linux/RedHat-7/source', WithDecryption=True)
    print(parameter)
    s3.Object(BUCKET_NAME, 'var.txt').put(Body="parameter")
   
    return {
        'status': 'success',
        'message': 'storing ssm parameter in s3',
    }
    
   
