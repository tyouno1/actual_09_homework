#coding:utf-8
import uconf
import json
from db_act import db_commit
def adduser(username,password,age):
    _sql="replace into user(username,password,age)values(%s,md5(%s),%s)"
    args=(username,password,age)
    db_commit(_sql,args)
    return 1

if __name__ == '__main__':
    adduser('test','test_p',17)
