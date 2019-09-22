import instrument
import battery

class Charger:
  def __init__(self, i, d, b, v=False):
    self._verbose = v
    self._instr_output_ch = 1
    self._instr = instrument.newInstrument(i, d)
    self._instr.setVerbose(v)
    self._instr.connect()
    self._instr.reset()
    self._btr = battery.newBattery(b)
    self._btr.setVerbose(v)

  def initInstrParams(self, par):
    self._instr.setOutChOverVoltLimit(self._instr_output_ch, par['max_voltage'])
    self._instr.setOutChOverCurLimit(self._instr_output_ch, par['max_current'])
    self._instr.setOutChVoltCur(self._instr_output_ch, par['voltage'], par['current'])
    self._instr.enableOutChOverVoltProt(self._instr_output_ch)
    self._instr.enableOutChOverCurProt(self._instr_output_ch)
#    self._instr.enableOutCh(self._insr_output_ch)

  def setInstrParams(self, par):
    if 'voltage' in par.keys() and 'current' in par.keys():
      self._instr.setOutChVoltCur(self._instr_output_ch, par['voltage'], par['current'])

  def charge(self):
    try:
      self.initInstrParams(self._btr.charge(0, 0))
      while True:
        i, v, p = self._instr.getOutChVoltCurPow(self._instr_output_ch)
        par = self._btr.charge(i, v)
        self.setInstrParam(par)
    finally:
      print 'Stopping charging due to a fatal error! It wasn\'t finished'
      self._instr.disableOutCh(self._instr_output_ch)
      
