import instrument
import battery

class Charger:
  def __init__(self, i, d, b, v=False):
    self._verbose = v
#    self._instr = instrument.newInstrument(i, d)
#    self._instr.setVerbose(v)
#    self._instr.connect()
#    self._instr.reset()
#    self._instr.setOutChVoltCur(1,5,1)
#    self._instr.setOutChOverVoltLimit(1,6)
#    self._instr.enableOutChOverVoltProt(1)
#    self._instr.setOutChOverCurLimit(1, 2)
#    self._instr.enableOutChOverCurProt(1)
#    self._instr.enableOutCh(1)
#    v, i, p = self._instr.getOutChVoltCurPow(1)
#    print "V: " + str(v) + ", I: " + str(i) + ", P: " + str(p)
    self._btr = battery.newBattery(b)
    self._btr._getMethod('dV')()

