#!/bin/bash

ARTIFACT=`packer build -machine-readable gold-ami.json |awk -F, '$0 ~/artifact,0,id/ {print $6}'`
AMI_ID=`echo $ARTIFACT | cut -d ':' -f2`

echo 'variable "AMI_ID" { default = "'${AMI_ID}'" }' > amivar.txt
echo $AMI_ID


