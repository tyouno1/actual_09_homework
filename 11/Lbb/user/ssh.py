#!encoding:utf-8
import paramiko
import getpass
'''
手动连接ssh

客户端选择验证策略(服务器端密码策略)
ip, port, username
password/加载public key

操作

close

'''

def ssh_execute(host, username, password, cmds=[], port=22):

     _rt_list = []
     ssh = None
     try:
        #创建ssh连接对象
        ssh = paramiko.SSHClient()

        #设置客户端登录验证方式
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #连接服务器信息
        ssh.connect(host, port, username, password)

        for _cmd in cmds:
            #操作
            stdin, stdout, stderr = ssh.exec_command(_cmd)
            #获取反馈信息
            _rt_list.append([_cmd, stdout.readlines(), stderr.readlines()])
        return True,_rt_list
     except BaseException as e:
         return False,['请检查你的系统用户名和密码还有连接是否正常']
        #关闭
     finally:
         if ssh:
            ssh.close()


def ssh_upload(host, username, password, files=[], port=22):
    t = paramiko.Transport((host, port))
    t.connect(username=username, password= password)
    sftp = paramiko.SFTPClient.from_transport(t)
    for _local, _remote in files:
        sftp.put(_local,_remote)
    t.close()

if __name__ == '__main__':
    host = '182.61.42.4'
    port = 22
    username = 'root'
    password = getpass.getpass('please input password:')
    print '"%s"' % password
    cmds = [
                "ps aux | grep python | grep kk | awk '{print $2}' | xargs kill -9",
                'nohup python /tmp/kk.py >/dev/null 2>&1 &'
            ]
    files = [('test.py', '/tmp/kk.py')]
    _rt_list = ssh_upload(host, username, password, files, port)
    _rt_list = ssh_execute(host, username, password, cmds, port)
    for _cmd, _out, _err in _rt_list:
        print _cmd, _out, _err