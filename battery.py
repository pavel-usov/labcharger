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

  def init_charge(self, i, v):
    if self.check == True:
      self._info('Starting battery check')
      self.charge = self.btr_check
    else:
      self._info('Starting battety qualification')
      self.charge = self.btr_qualify
    return ({
      'max_voltage': self._max_voltage,
      'max_current': self.capacity * self._max_current_ratio,
      'voltage': self._max_voltage,
      'current': self.capacity * self._test_ratio
    })

  def btr_check(self, i, v):
    print 'Battery check'

  def btr_qualify(self, i, v):
    print 'Battery qualify'

  charge = init_charge

_btrIndex()
