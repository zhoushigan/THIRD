#!/usr/bin/python35
#coding:utf-8

import os
import psutil


def check_server_disk():
	path = '/pythonscript/put/'
	st = os.statvfs(path)
	free = st.f_bfree/st.f_blocks * 100
	print(free)

def check_cpu():
	print(psutil.virtual_memory())
	print(psutil.net_io_counters(pernic=True))


def run():
	check_server_disk()
	check_cpu()

if __name__ == '__main__':
	run()


