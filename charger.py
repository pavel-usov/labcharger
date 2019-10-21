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

  def setInstrParams(self, par):
    for p in par:
      if p == 'current':
        self._instr.setOutChCur(self._instr_output_ch, par[p])
      elif p == 'voltage':
        self._instr.setOutChVolt(self._instr_output_ch, par[p])
      elif p == 'voltage_current':
        self._instr.setOutChVoltCur(self._instr_output_ch, par[p][0], par[p][1])
      elif p == 'max_voltage':
        self._instr.setOutChOverVoltLimit(self._instr_output_ch, par[p])
        self._instr.enableOutChOverVoltProt(self._instr_output_ch)
      elif p == 'max_current':
        self._instr.setOutChOverCurLimit(self._instr_output_ch, par[p])
        self._instr.enableOutChOverVoltProt(self._instr_output_ch)

  def initInstrParams(self):
    self.setInstrParams(self._btr.init_charge())
    self._instr.enableOutCh(self._instr_output_ch)

  def charge(self):
    res = True
    try:
      self.initInstrParams()
      while res:
        self._btr.waitCycle()
        v, i, p = self._instr.getOutChVoltCurPow(self._instr_output_ch)
        res = self._btr.charge(i, v)
        self.setInstrParams(res)
    except Exception as e:
      self._instr.disableOutCh(self._instr_output_ch)
      print 'Stopping charging due to a fatal error! Process wasn\'t finished'
      print e
      quit(1)
    self._instr.disableOutCh(self._instr_output_ch)
    print 'Charging success!'  
