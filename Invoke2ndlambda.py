from __future__ import print_function
import boto3
import io
import json
import subprocess
from packerpy import PackerExecutable
import os 
import sys
from botocore.exceptions import ClientError
try:
    aws_session = boto3.Session()
    lambda_client = aws_session.client('lambda')
except botocore.exceptions.NoRegionError as e: 
    pass

def lambda_handler(event, context):
    invoke_response = lambda_client.invoke(FunctionName="Second_function_name",InvocationType='RequestResponse')
