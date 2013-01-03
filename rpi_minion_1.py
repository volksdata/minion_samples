#!/usr/bin/python.

"""
@file rpi_minion_1.py
@author Greg Crawford
@date 2012-01-02
@brief Sample script for interfacing Minion with Raspberry Pi using serial-over-usb

"""
import sys
import os
import serial
import io

print "Start"

# configure the serial connections
ser = serial.Serial(
  port='/dev/ttyACM0',
  baudrate=57600
)

ser.isOpen()

try:
  while True:
    line = ser.readline()
    print 'Serial In: ',line

except KeyboardInterrupt:
  pass # do cleanup here

ser.close()

print "Done"


