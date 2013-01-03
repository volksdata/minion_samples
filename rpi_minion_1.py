#!/usr/bin/python.

"""
@file rpi_minion_1.py
@author Greg Crawford
@date 2012-01-02
@brief Sample script for interfacing Minion with Raspberry Pi using serial-over-usb

@note A nice reference on connecting Arduinos to RPi:  http://raspberrypi.stackexchange.com/questions/1505/how-to-attach-an-arduino

This script simply echoes all data received from a Minion to the console.
"""
import sys
import os
import serial
import io

print "Start"

# configure the serial connections
ser = serial.Serial(
  # Note that the specific port name will depend on the device being connected.
  # On my RPi, minions appear on 'dev/ttyACM0'
  port='/dev/ttyACM0',
  baudrate=57600
)

ser.isOpen()

try:
  while True:
    line = ser.readline()
    #Echo all received data
    print 'Serial In: ',line

# Ctrl-C should break this loop
except KeyboardInterrupt:
  pass # do cleanup here

ser.close()

print "Done"


