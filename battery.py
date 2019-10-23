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
  methods = {}
  cycleLen = 5

  def __init__(self, v=False):
    self._verbose = v
    self.charge_step = self.charge_process()
    self.charge_finished = getattr(self, '_mtd_' + self.method)

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

class _MTD_dV:
  _mtd_dv_desc = 'most common and reliable method'
  _mtd_dv_delta_voltage = 0.03
  _mtd_dv_max_measured_voltage = 0

  def _mtd_dV(self):
    if self._measured_voltage > self._mtd_dv_max_measured_voltage:
      self._mtd_dv_max_measured_voltage = self._measured_voltage
      return False
    if self._mtd_dv_max_measured_voltage - self._measured_voltage > self._mtd_dv_delta_voltage:
      return True
    return False

class _BTR_NiMH(_Battery, _MTD_dV):
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
  _preparing_cycles = 24

  def charge_process(self):
    charge_current = self.capacity * self._charge_ratio

    if self.check == True:
      self._info('Checking battery')
      if self._measured_voltage > self._test_voltage:
        raise Exception('Battery has wrong type or not connected')
    
    self._info('Starting precharging')
    while self._measured_voltage < self._precharge_voltage:
      yield {'keep'}

    self._info('Preparing fast charging')
    set_current = self.capacity * self._test_ratio
    cur_increase = (charge_current - set_current) / self._preparing_cycles
    
    for step in range(0, self._preparing_cycles):
      if self.charge_finished():
        break
      set_current += cur_increase
      yield {'current': set_current}

    self._info('Starting fast charging')
    yield {'current': charge_current}
    while not self.charge_finished():
      yield {'keep'}

    if self.keep == True:
      yield {'current': self.capacity * self._keep_ratio}
      while self._measured_voltage < self._test_voltage:
        yield {'keep'}

    yield {}

  def init_charge(self):
    self._info('Starting instrument initialisation')
    return {
      'max_voltage': self._max_voltage,
      'max_current': self.capacity * self._max_current_ratio,
      'voltage_current': [self._max_voltage, self.capacity * self._test_ratio]
    }

_btrIndex()
