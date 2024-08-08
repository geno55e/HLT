import pyvisa
from time import sleep

# HM8143 Spannungsquelle
def HM8143_Quelle_remoteOn():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('RM1')
    my_instrument.close()


def HM8143_Quelle_remoteOff():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('RM0')
    my_instrument.close()


def HM8143_Quelle_SpannungLinks(spannung):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('SU1:'+str(spannung))
    my_instrument.close()


def HM8143_Quelle_SpannungRechts(spannung):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('SU2:'+str(spannung))
    my_instrument.close()


def HM8143_Quelle_StromLinks(strom):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('SI1:'+str(strom))
    my_instrument.close()


def HM8143_Quelle_StromRechts(strom):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('SI2:'+str(strom))
    my_instrument.close()


def HM8143_Quelle_AusgangOn():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('OP1')
    my_instrument.close()


def HM8143_Quelle_AusgangOff():
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('OP0')
    my_instrument.close()


# Fluke
def Fluke_LeseGleichspannung(messbereich):
    rm = pyvisa.ResourceManager()
    my_instrument = rm.open_resource('ASRL6::INSTR', write_termination='\r', read_termination='\r')
    my_instrument.write('*RST;*CLS;CONF:VOLT:DC '+str(messbereich)+';:VOLT:DC:NPLC 1;:TRIG:SOUR BUS')
    spannung = my_instrument.query(':INIT;*TRG;FETCH?')
    my_instrument.write('*RST;syst:local')
    my_instrument.close()
    return spannung








