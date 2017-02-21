#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket


TRACE = False
DEBUG = False
from contextlib import closing

class SendingMessageControl(object):
	"""Control object for SendinMessage"""



	def __init__(self, partner_host, port):
		"""constructor for this class"""
		if TRACE: print_doc(__name__, self)
		self._partner_host_ip = partner_host
		self._port = port

		return

	def set_message(self, message):
		"""this is the method to set sending the message"""
		self._message = message.split(' / ')
		return

	def start(self):
		"""this is the method to sending the message"""
		if TRACE: print_doc(__name__, self)

		self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		with closing(self._sock):
			while True:
				if(DEBUG): print self._message
				for each_message in self._message:
					self._sock.sendto(each_message, (self._partner_host_ip, self._port))
					if(each_message == 'exit_0'): sys.exit(0)
				break

		return


def main():
	"""
	
	"""

	print '/////please input client ip'
	partner_ip = '192.168.10.113' if DEBUG else raw_input()

	print '/////please input port number'
	port = 4000 if DEBUG else int(float(raw_input()))

	print '/////connecting...'
	message = SendingMessageControl(partner_ip, port)
	print '/////done.'

	print '/////start connection (enable to exit with typing exit_0)'

	while True:
		sending_message = "hello / i'm / okamoto / exit_0" if DEBUG else raw_input()
		message.set_message(sending_message)
		message.start()


	return 0

def print_doc(namespace, object):
	"""
	
	"""
	
	import inspect
	# method_name = inspect.currentframe().f_back.f_code.co_name
	method_name = inspect.stack(1)[1][0].f_code.co_name
	document_string = getattr(object, method_name).__doc__
	print('{0} [{1}] {2}'.format(namespace, method_name, document_string))

if __name__ == '__main__':
	sys.exit(main())