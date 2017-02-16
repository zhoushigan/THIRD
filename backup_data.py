#!/usr/bin/python35
#coding:utf-8

import os 
import traceback
from datetime import datetime


home_path = os.path.expanduser("~") + "/"
mysqldump_output_file_name = home_path + "mysql_backup/"


def mysqlduml(host,user,password,database_name,port=3306,skipdata=False):
	try:
		skipdata_string = ''
		if skipdata:
			skipdata_string = '-d'
		output_file = mysqldump_output_file_name + database_name + str(datetime.datetime.now().strftime("%Y-%m-%d")) + '.bak'
		mysqldumo_string = "mysqlduml --lock-tables=false -C -P{0} -h{1} -u{2} -p{3} {4} {5} > {6}".format(port,host,user,password,skipdata_string,database_name,output_file)

		os.system(mysqldumo_string)
	except:
		traceback.print_exc()


def backup_xxdata():
	shell_str = 'find /home/ -name "*.tar.gz" -mtime -500 | xargs -I {} scp {} /backup_data'
	os.system(shell_str)

def run():
	backup_xxdata()
	#备份mysqldump数据
	#mysqldump("127.0.0.1","root","admin","monitoring")

if __name__ == '__main__':
	run()

