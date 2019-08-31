import instrument
#import battery

class Charger:
  def __init__(self, i, d, b, v=False):
    self._verbose = v
    self._instr = instrument.newInstrument(i, d)
    self._instr.setVerbose(v)
    self._instr.connect()
    self._instr.reset()
    self._instr.setOutChCurVolt(1,5,1)
    self._instr.setOutChOverVoltLimit(1,6)
    self._instr.enableOutChOverVoltProt(1)
    self._instr.setOutChOverCurLimit(1, 2)
    self._instr.enableOutChOverCurProt(1)
    self._instr.enableOutCh(1)

#    self._btr = battery(b)

