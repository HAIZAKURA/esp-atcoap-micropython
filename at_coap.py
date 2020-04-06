""" 
CoAP Over AT
Author: HAIZAKURA
For: ESP8266 / ESP32
2020.April
""" 

import machine
from machine import UART, Timer
import ubinascii

WRIT_OKK = 'OK'
WRIT_ERR = 'ERROR'
SEND_CMD = 'AT+NMGS='
RECV_CMD = '+NNMI:'

class AT_CoAP(object):
	def __init__(self, uartid, rxpin, txpin, callback):
		"""
		uartid - the id of uart which only can be 1 or 2 on ESP32 / 0 on ESP8266
		rxpin - the GPIO that used as uart rx
		txpin - the GPIO that used as uart tx
		callback - the function called (with an arg: rev_msg) when received messages.
		"""
		self.uart = UART(uartid, baudrate=9600, bits=8, parity=None, stop=1, rx=rxpin, tx=txpin)
		self.callback = callback
		self.timer = Timer(1)
		self.timer.init(period=50, mode=Timer.PERIODIC, callback=self._handler)

	def send(self, data):
		length = str(len(data))
		msg = ubinascii.hexlify(data)
		cmd = bytes(SEND_CMD + length, 'utf-8') + b',' + msg + b'\r\n'
		# print('send:', cmd)
		self.uart.write(cmd)

	def _handler(self, timer):
		if self.uart.any():
			# transfrom received message to utf-8 string and format
			rev_data = str(self.uart.read(), 'utf-8').replace('\r\n', '')
			# print(rev_data)
			if rev_data == WRIT_OKK:
				pass
			elif rev_data == WRIT_ERR:
				rev_msg = '_ERR_'
				self.callback(rev_msg)
			elif rev_data.startswith(RECV_CMD):
				hex_msg = rev_data.split(',')[1]
				rev_msg = str(ubinascii.unhexlify(hex_msg), 'utf-8')
				self.callback(rev_msg)
