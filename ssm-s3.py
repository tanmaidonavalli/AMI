from __future__ import print_function
import boto3
import io
import json
import subprocess
from packerpy import PackerExecutable
import os 
from botocore.exceptions import ClientError

BUCKET_NAME = 'YOUR_BUCKET_NAME'

def lambda_handler(event, context):
    ssm = boto3.client('ssm')
    s3 = boto3.resource('s3')
    s3Client = boto3.client('s3')
    ssm_parameter = ssm.get_parameter(Name='/GoldenAMI/Linux/RedHat-7/source', WithDecryption=True)
    save_parameter = print (ssm_parameter['Parameter']['Value'])
    print (save_parameter)
    s3_content = s3.Object(BUCKET_NAME, 'var.txt').put(Body="save_parameter")
    print (s3_content)
    
    return {
        'status': 'success',
        'message': 'storing ssm parameter in s3',
    }
    
   
