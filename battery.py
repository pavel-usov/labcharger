import time

all = {}

_prefix = '_BTR_'
_all = {}

def _btrIndex():
  for g, r in globals().items():
    if g.startswith(_prefix):
      n = g[len(_prefix):]
      all[n] = r.desc
      _all[n] = r

def newBattery(n):
  b = _all[n]()
  return b

class _Battery:
  cycleLen = 10

  def __init__(self, v=False):
    self.verbose = v
    self.charge_step = self.charge_process()
    next(self.charge_step)

  def _info(self, m):
    if self._verbose:
      print m

  def setCapacity(self, c):
    self.capacity = c

  def setVoltage(self, v):
    self.voltage = v

  def setVerbose(self, v):
    self._verbose = v

  def _MTD_dV(self):
    print 'Method dV'

class _BTR_NiMH(_Battery):
  desc = 'Nickel-metal hydride'
  
  capacity = 2.2
  voltage = 1.2
  method = 'dV'

  check = True
  keep = True

  _test_ratio = 0.1
  _charge_ratio = 0.85
  _keep_ratio = 0.05
  _max_current_ratio = 1
  _max_voltage = 8

  def charge_process(self):
    if self.check == True:
      self.charge = self.btr_check
      yield

    self.charge = self.btr_qualify
    yield

  def init_charge(self):
    self._info('Starting instrument initialisation')
    return {
      'max_voltage': self._max_voltage,
      'max_current': self.capacity * self._max_current_ratio,
      'voltage_current': [self._max_voltage, self.capacity * self._test_ratio]
    }

  def btr_check(self, i, v):
    print 'Battery check'
    next(self.charge_step)
    return {True}

  def btr_qualify(self, i, v):
    print 'Battery qualify'
    return {}

#  charge = init_charge

_btrIndex()
