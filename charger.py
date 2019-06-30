import instrument
#import battery

class Charger:
  def __init__(self, i, d, b, v=False):
    self._verbose = v
    self._instr = instrument.newInstrument(i, d)
    self._instr.setVerbose(v)
    self._instr.connect()
#    self._instr.reset()
    self._instr.setOutputChannel(1,-5,1)
#    self._instr.enableOutputChannel(1)
#    self._btr = battery(b)

