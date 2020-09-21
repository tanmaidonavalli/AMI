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

def lambda_handler(event, context):
    ssm = boto3.client('ssm')
    ssm_parameter = ssm.get_parameter(Name='/GoldenAMI/Linux/RedHat-7/source', WithDecryption=True)
    save_parameter = (ssm_parameter['Parameter']['Value'])
    print (save_parameter)
    print('This message will be displayed on the screen.')
    original_stdout = sys.stdout # Save a reference to the original standard output
    with open('/tmp/var.txt', 'w') as f:
        sys.stdout = original_stdout
        f = open("/tmp/var.txt", "r")
        f.readline()
    subprocess.call("set /P id=</tmp/var.txt", shell=True)
    print(os.environ)
