#!/usr/bin/env python
# coding: UTF-8

import sys
import os 
import boto.ec2
from prettytable import PrettyTable

if len(sys.argv) !=2:
    sys.exit("Usage: %s {craedentials file}" % sys.argv[0]) 
if not os.path.exists(sys.argv[1]):
    sys.exit('ERROR: File %s was Not Found!' % sys.argv[1]) 
else:
    awsconf = sys.argv[1]

f = open(awsconf)
line = f.readlines()
for aws_info in line:
    aws_info = aws_info.rstrip()
    aws_info = aws_info.split(':')
    a_name = aws_info[0]
    a_keyid = aws_info[1]
    a_sec = aws_info[2]
    a_region = aws_info[3]

    conn = boto.ec2.connect_to_region(a_region,
    aws_access_key_id=a_keyid,
    aws_secret_access_key=a_sec)
	
    table = PrettyTable(['Name', 'Global_IPAddr', 'Private_IPAddr', 'Inst_ID', 'Status', 'Inst_Type', 'Public_Name'])
    table.align['Name'] = 'l'
    table.align['Inst_Type'] = 'l'
    table.align['Public_Name'] = 'l'
    table.align['Private_IPAddr'] = 'l'
    table.align['Global_IPAddr'] = 'l'
    table.padding_width = 2

    reservations = conn.get_all_instances()
    instances = [ i for res in reservations for i in res.instances]
    for inst in instances:
        table.add_row([inst.tags['Name'], inst.ip_address, inst.private_ip_address, inst.id, inst.state, inst.instance_type, inst.public_dns_name])

    print "[[[ " + a_name + " ]]]"
    print table.get_string(sortby="Name") + "\n"

f.close
