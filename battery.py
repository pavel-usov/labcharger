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
  chargeType = 'safe'
  cycleLen = 10

  methods = []
  types = []

  _mtd_prefix = '_MTD_'
  _typ_prefix = '_TYP_'

  def __init__(self, v=False):
    self.verbose = v
    self._idxTypesMethods()
    self._charge = self.charge
    self.charge = self.charge_init

  def _idxTypesMethods(self):
    for m in dir(self):
      if m.startswith(self._mtd_prefix):
        self.methods.append(m[len(self._mtd_prefix):])
      elif m.startswith(self._typ_prefix):
        self.types.append(m[len(self._typ_prefix):])

  def _getType(self, t):
    if t in self.types:
      return getattr(self, self._typ_prefix + t)
    return None

  def _getMethod(self, m):
    if m in self.methods:
      return getattr(self, self._mtd_prefix + m)
    return None

  def setCapacity(self, c):
    self.capacity = c

  def setVoltage(self, v):
    self.voltage = v

  def charge_init(self):
    self._stage = 0
    self.charge = charge

class _BTR_NiMH(_Battery):
  desc = 'Nickel-metal hydride'
  
  capacity = 2200
  voltage = 1.2
  method = 'dV'

  def charge():

  def _TYP_safe(self):
    print 'Method safe'

  def _TYP_fast(self):
    print 'Type fast'

  def _MTD_dV(self):
    print 'Method dV'

_btrIndex()
