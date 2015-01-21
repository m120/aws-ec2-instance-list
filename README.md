# Instance list of AWS EC2

## Description:
Instance list of AWS EC2.

```bash
[[[ AWS Segument-01 ]]]
+--------------+-----------------+------------------+--------------+-----------+------------+-------------------------------------------------------
|  Name        |  Global_IPAddr  |  Private_IPAddr  |   Inst_ID    | Status    |  Inst_Type |  Public_Name
+--------------+-----------------+------------------+--------------+-----------+-------------+------------------------------------------------------
|  AP01        |  54.64.nn.nnn   |  172.31.nn.nnn   |  i-1980hori  |  running  |  m1.small  | ec2-54-64-nn-nnn.ap-northeast-1.compute..amazonaws.com
|  AP02        |  54.65.nn.nnn   |  172.31.nn.nnn   |  i-1213mitsuo|  running  |  m1.small  | ec2-54-65-nn-nnn.ap-northeast-1.compute..amazonaws.com
+--------------+-----------------+------------------+--------------+-----------+-------------+------------------------------------------------------

[[[ AWS Segument-02]]]
+--------------------+------------------+------------------+--------------+-----------+-------------+-------------------------------------------------------
|  Name              |  Global_IPAddr   |  Private_IPAddr  |   Inst_ID    |   Status  |  Inst_Type  |  Public_Name
+--------------------+------------------+------------------+--------------+-----------+-------------+-------------------------------------------------------
|  AP1               |  54.64.nn.nnn    |  172.31.nn.nnn   |  i-naomi     |  running  |  m3.medium  | ec2-54-64-nn-nnn.ap-northeast-1.compute.amazonaws.com
|  AP2               |  54.64.nn.nnn    |  172.31.nn.nn    |  i-loveyou   |  running  |  m1.small   | ec2-54-64-nn-nnn.ap-northeast-1.compute.amazonaws.com
|  AP3               |  None            |  172.31.nn.nnn   |  i-hehehe :-)|  stopped  |  m3.medium  |
|  ImageAP1          |  54.65.nn.nnn    |  172.31.nn.nnn   |  i-kanamu    |  running  |  m1.small   | ec2-54-65-nn-nnn.ap-northeast-1.compute.amazonaws.com
|  ImageAP2          |  54.65.nn.nnn    |  172.31.nn.nnn   |  i-haruya    |  running  |  m1.small   | ec2-54-65-nn-nnn.ap-northeast-1.compute.amazonaws.com
|  Honeypod01        |  54.238.nn.nnn   |  172.31.nn.nnn   |  i-youre     |  running  |  t1.micro   | ec2-54-238-nn-nn.ap-northeast-1.compute.amazonaws.com
|  ContorolTower01   |  54.65.nn.nnn    |  172.31.nn.nnn   |  i-everything|  running  |  t1.micro   | ec2-54-65-nn-nnn.ap-northeast-1.compute.amazonaws.com
|  Launcher01        |  None            |  172.31.nn.nnn   |  i-150120    |  stopped  |  t1.micro   |
+--------------------+------------------+------------------+--------------+-----------+-------------+-------------------------------------------------------
```

## Getting Started:
Install Python Library.
```bash
$ pip install boto
$ pip install prettytable
```

Create a Credentials File. (e.g. ~/awsconf.txt)
```bash
<Name>:<aws_access_key_id>:<aws_secret_access_key>:<region>

Example.
AWS Segument-01:AKIev2ff2fvjfjf:5ns5pddldldlo40cfkcmejfjfF:ap-northeast-1
AWS Segument-02:AKIAJjdo30dj30k:5ns5ddkldldld3jd049dpdpddF:ap-northeast-1
```

## Using:
```bash
$ python ./aws_ec2_info.py {craedentials file}
```
---
*I am a Python noob :-)* 

