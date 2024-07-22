import pyvisa

from pyvisa import constants

constants.VI_ASRL_FLOW_NONE
constants.VI_ASRL_FLOW_XON_XOFF
constants.VI_ASRL_FLOW_RTS_CTS
constants.VI_ASRL_FLOW_DTR_DSR

from time import sleep
import tkinter as tk

rm = pyvisa.ResourceManager()

instr_fluke_multi = rm.open_resource('ASRL5::INSTR', read_termination = '\r\n', query_delay = 0.21)
instr_fluke_multi.set_visa_attribute(constants.VI_ATTR_ASRL_FLOW_CNTRL, constants.VI_ASRL_FLOW_RTS_CTS)
# instr_fluke_multi.write('*RST;*CLS;CONF:VOLT:DC 1;:VOLT:DC:NPLC 2;:TRIG:SOUR IMM;:INIT')
instr_fluke_multi.write('*RST;*CLS')
instr_fluke_multi.write(':SYST:REM')
instr_fluke_multi.write('CONF:VOLT:DC 10;:VOLT:DC:NPLC 2')
instr_fluke_multi.write('SAMP:COUNT 1')
instr_fluke_multi.write(':TRIG:SOUR IMM')
instr_fluke_multi.write(':TRIG:DEL 0')


# instr_hm8150_freq = rm.open_resource('ASRL3::INSTR', write_termination = '\r', read_termination = '\r')
instr_hm8143_power = rm.open_resource('ASRL6::INSTR', write_termination = '\r', read_termination = '\r')

instr_hm8143_power.write('RM1')
instr_hm8143_power.write('SI1:0.1')
instr_hm8143_power.write('OP1')

x = 1
while x<5:
    instr_hm8143_power.write('SU1:'+str(x)+'.01')
    instr_fluke_multi.write('INIT')
    print(instr_fluke_multi.query('FETCH?'))
    sleep(2)
    x+=1
    
instr_hm8143_power.write('OP0')
instr_fluke_multi.write(':SYST:LOC')
instr_fluke_multi.write('*RST;*CLS')


