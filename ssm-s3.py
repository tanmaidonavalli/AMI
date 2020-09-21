from __future__ import print_function
import boto3
import io
import json
import subprocess
from packerpy import PackerExecutable
import os 
import sys
from botocore.exceptions import ClientError

BUCKET_NAME = 'demo-s3lambda'
download_dir = '/tmp/'


def lambda_handler(event, context):
    ssm = boto3.client('ssm')
    s3 = boto3.resource('s3')
    s3Client = boto3.client('s3')
    ssm_parameter = ssm.get_parameter(Name='/GoldenAMI/Linux/RedHat-7/source', WithDecryption=True)
    save_parameter = (ssm_parameter['Parameter']['Value'])
    print (save_parameter)
    print('This message will be displayed on the screen.')
    original_stdout = sys.stdout # Save a reference to the original standard output
    with open('/tmp/var.txt', 'w') as f:
    sys.stdout = f 
    print('This message will be written to a file.')
    sys.stdout = original_stdout
    f= open("/tmp/var.txt","r")
    contents = f.read()
    print(contents)
