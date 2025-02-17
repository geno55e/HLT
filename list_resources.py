# Requirements
# Python (tested with 3.6+)
# VISA (tested with NI-VISA 17.5, Win7, from www.ni.com/visa and Keysight-VISA )
# pip install pyvisa-py
# pip install pyserial

import pyvisa
rm = pyvisa.ResourceManager()
rm.list_resources()


