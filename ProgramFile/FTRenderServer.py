#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
import os


TRACE = False
DEBUG = False
from contextlib import closing

class SendingMessageControl(object):
	"""Control object for SendinMessage"""



	def __init__(self):
		"""constructor for this class"""
		if TRACE: print_doc(__name__, self)

		self.initialize_()

		self._command_for = False
		self._ip_addrs = []

		return

	def initialize_(self):
		print '/////please type number of client'
		self._number_of_clients = int(float(raw_input()))

		self._partner_clients_ip = []

		print '/////please type client ip'
		for each in range(self._number_of_clients):
			print "{} of client ip:".format(each)
			self._partner_clients_ip.append('192.168.10.113' if DEBUG else raw_input())

		print '/////please type port number'
		self._port = 4000 if DEBUG else int(float(raw_input()))

		print '/////connecting...'

		self._add_motion_data = False

		print '/////done.'

		print '/////start connection (enable to exit with typing exit_0)'

		return


	def set_message(self, message):
		"""this is the method to set sending the message"""
		self._message = message.split(' / ')
		return

	def start(self):
		"""this is the method to sending the message"""
		if TRACE: print_doc(__name__, self)

		while True:
			sending_message = "hello / i'm / okamoto / exit_0" if DEBUG else raw_input()
			self.set_message(sending_message)
			self.sending()

	def sending(self):
		"""this is the method to sending the message"""
		if TRACE: print_doc(__name__, self)

		self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		with closing(self._sock):
			if(DEBUG): print self._message
			if DEBUG: print "message: {}".format(each_message)
			for each_message in self._message:
				if each_message == 'exit_0':
					self._command_for = False
					self._ip_addrs = []
					self.send_message_('exit_0')
					sys.exit(0)
				elif each_message == 'command_for':
					self._command_for = True
				elif each_message == 'command_for_end':
					self._ip_addrs = []
				elif self._command_for:
					self._ip_addrs = each_message.split(',')
					self._command_for = False
				elif self._add_motion_data:
					for each in self.get_motion_data(each_message):
						self.send_message_(each)
					self._add_motion_data = False
				elif each_message == 'send_motion_data':
					self._add_motion_data = True
				else:
					self.send_message_(each_message)
				
		return

	def send_message_(self, line):
		for each_client in self._partner_clients_ip if len(self._ip_addrs) == 0 else self._ip_addrs:
			self._sock.sendto(line, (each_client, self._port))

		return

	def get_motion_data(self, path):
		"""モーションデータをコマンドリストに変換"""
		if TRACE: print_doc(__name__, self)

		filename = os.path.join(os.getcwd(), 'motion_data' + os.sep + path)

		if os.path.exists(filename) and os.path.isfile(filename):
			pass
		else:
			print 'error to find the motion data file path'
			sys.exit(1)

		a_command_list = []
		with open(filename, "rU") as a_file:
			while True:
				a_string = a_file.readline()
				if len(a_string) == 0: break
				output = ''
				for char in a_string:
					if char != '\n': output = output + char
				a_command_list.append(output)

		return a_command_list

def main():
	"""
	
	"""

	message = SendingMessageControl()

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