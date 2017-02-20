#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket


TRACE = True
DEBUG = True
from contextlib import closing

class ReceivingMessageControl(object):
	"""Control object for SendinMessage"""



	def __init__(self, super_host, port, buffer_size):
		"""constructor for this class"""
		if TRACE: print_doc(__name__, self)
		self._super_host_ip = super_host
		self._port = port
		self._buffer_size = buffer_size
		self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		return

	def start(self):
		"""this is the method to recieve the message"""
		if TRACE: print_doc(__name__, self)
		with closing(self._sock):
			self._sock.bind((self._super_host_ip, self._port))
			stock = ''
			while True:
				recieved_message = self._sock.recv(self._buffer_size)
				if recieved_message == 'exit_0' : break
				print(recieved_message)

		return


def main():
	"""
	
	"""

	print '/////please type this pcs ip addr'
	partner_ip = '192.168.10.113'
	port = 4000
	buffer_size = 4096

	message = ReceivingMessageControl(partner_ip, port, buffer_size)
	message.start()


	return

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