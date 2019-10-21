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
  cycleLen = 5

  def __init__(self, v=False):
    self._verbose = v
    self.charge_step = self.charge_process()

  def _info(self, m):
    if self._verbose:
      print m

  def setCapacity(self, c):
    self.capacity = c

  def setVoltage(self, v):
    self.voltage = v

  def setVerbose(self, v):
    self._verbose = v

  def waitCycle(self):
    time.sleep(self.cycleLen)

  def charge(self, i, v):
    self._measured_current = i
    self._measured_voltage = v
    return next(self.charge_step)

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
  _test_voltage = 1.8
  _precharge_voltage = 0.85

  def charge_process(self):
    if self.check == True:
      self._info('Checking battery')
      if self._measured_voltage > self._test_voltage:
        raise Exception('Battery has wrong type or not connected')
    
    self._info('Starting precharging')
    while self._measured_voltage < self._precharge_voltage:
      yield {True}

    self._info('Starting fast charging')
    yield {'current': self.capacity * self._charge_ratio}
    while 

  def init_charge(self):
    self._info('Starting instrument initialisation')
    return {
      'max_voltage': self._max_voltage,
      'max_current': self.capacity * self._max_current_ratio,
      'voltage_current': [self._max_voltage, self.capacity * self._test_ratio]
    }

  def _MTD_

_btrIndex()
