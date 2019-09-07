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

class _Battery():
  def _init_(v=False):
    self.verbose = v

  def setCapacity(c):
    self.capacity = c

class _BTR_NiMH:
  desc = 'Nickel-metal hydride'

_btrIndex()
