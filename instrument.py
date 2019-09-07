import visa

all = {}
visa_lib = '@py'

_all = {}
_prefix = '_PS_'
_visa_rm = None

def _instrIndex():
  for g, r in globals().items():
    if g.startswith(_prefix):
      n = g[len(_prefix):]
      all[n] = r.desc
      _all[n] = r

def newInstrument(n, d):
  i = _all[n](d)
  return i

class SCPI_Cmd:
  def __init__(self, i=None):
    self._instr = i

  def setInstr(self, i):
    self._instr = i

  def query(self, c):
    r = self._instr.query(c)
    r = r.split(',')
    return r

class VISA_Cmd:
  def __init__(self, m=visa_lib):
    global _visa_rm
    if _visa_rm == None:
      _visa_rm = visa.ResourceManager(m)    
    self._rm = _visa_rm

  def connect(self, d):
    self._conn = self._rm.open_resource(d)

  def query(self, c):
    r = self._conn.query(c)
    return r

class _Instrument(object):
  def __init__(self, d, v=False):
    self._verbose = v
    self._dest = d
    if self.proto == 'VISA':
      self._instr = VISA_Cmd()
    if self._cmd_set == 'SCPI':
      self._cmd = SCPI_Cmd()
    self._cmd.setInstr(self._instr)

  def _info(self, m):
    if self._verbose:
      print m

  def setVerbose(self, v):
    self._verbose = True if v else False

  def connect(self):
    self._info('Connecting with instrument')
    self._instr.connect(self._dest)

  def query(self, c):
    r = self._cmd.query(c)
    return r

  def query_instr(self, c):
    r = self._instr.query(c)
    return r

#rm = visa.ResourceManager('@py')
#inst = rm.open_resource('TCPIP::192.168.1.2::INSTR')
#print(inst.query("*IDN?"))
#inst.query("APPL CH1,5,1")
#inst.query("OUTP CH1,ON")
#print(inst.query(":MEAS:ALL? CH1"))

class _SCPI_functions():
  _cmd_set = 'SCPI'

  VAR_ON = 'ON'
  VAR_OFF = 'OFF'

  CMD_IDN = '*IDN?'
  CMD_RST = '*RST'
  CMD_APPL = 'APPL CH{:d},{:d},{:d}'
  CMD_OUTP = 'OUTP CH{:d},{:3}'
  CMD_SOUR_CURR_PROT = ':SOUR{:d}:CURR:PROT {:d}'
  CMD_SOUR_CURR_PROT_STAT = ':SOUR{:d}:CURR:PROT:STAT {:3}'
  CMD_SOUR_VOLT_PROT = ':SOUR{:d}:VOLT:PROT {:d}'
  CMD_SOUR_VOLT_PROT_STAT = ':SOUR{:d}:VOLT:PROT:STAT {:3}'
  CMD_MEAS_ALL = ':MEAS:ALL? CH{:d}'

  # Get identification info from instrument
  def getIdentInfo(self):
    self._info('Getting instrument identification info')
    r = self.query(self.CMD_IDN)
    d = {'vendor': r[0], 'id': r[1], 'serial': [2], 'board': [3]}
    return d

  # Resets instrument to default state
  def reset(self):
    self._info('Reseting instrument')
    self.query(self.CMD_RST)

  # Enables output on specified channel c
  def enableOutCh(self, c):
    self._info('Enabling channel {:d}'.format(c))
    self.query(self.CMD_OUTP.format(c, self.VAR_ON))

  # Disables output on specified channel c
  def disableOutCh(self, c):
    self._info('Disabling channel {:d}'.format(c))
    self.query(self.CMD_OUTP.format(c, self.VAR_OFF))

  # Set output voltage v and current i values on specified channel
  def setOutChVoltCur(self, c, v, i):
    self._info('Setting channel {:d} to {:d}V, {:d}A'.format(c, v, i))
    self.query(self.CMD_APPL.format(c, v, i))

  # Set overcurrent protection limit on specified channel
  def setOutChOverCurLimit(self, c, i):
    self._info('Setting overcurrent protection limit on channel {:d} to {:d}A'.format(c, i))
    self.query(self.CMD_SOUR_CURR_PROT.format(c, i))

  # Enable overcurrent protection on specified channel
  def enableOutChOverCurProt(self, c):
    self._info('Enabling overcurrent protection on channel {:d}'.format(c))
    self.query(self.CMD_SOUR_CURR_PROT_STAT.format(c, self.VAR_ON))

  # Disable overcurrent protection on specified channel
  def disableOutChOverCurProt(self, c):
    self._info('Disabling overcurrent protection on channel {:d}'.format(c))
    self.query(self.CMD_SOUR_CURR_PROT_STAT.format(c, self.VAR_OFF))

  # Set overvoltage protection limit on specified channel
  def setOutChOverVoltLimit(self, c, v):
    self._info('Setting overvoltage protection limit on channel {:d} to {:d}V'.format(c, v))
    self.query(self.CMD_SOUR_VOLT_PROT.format(c, v))

  # Enable overvoltage protection on specified channel
  def enableOutChOverVoltProt(self, c):
    self._info('Enabling overvoltage protection on channel {:d}'.format(c))
    self.query(self.CMD_SOUR_VOLT_PROT_STAT.format(c, self.VAR_ON))

  # Disable overvoltage protection on specified channel
  def disableOutChOverCurProt(self, c):
    self._info('Disabling overvoltage protection on channel {:d}'.format(c))
    self.query(self.CMD_SOUR_VOLT_PROT_STAT.format(c, self.VAR_OFF))

  # Reads voltage and current output values on specified channel
  def getOutChVoltCurPow(self, c):
    self._info('Reading volatage, current and power values on channel {:d}'.format(c))
    res = self.query(self.CMD_MEAS_ALL.format(c))
    return float(res[0]), float(res[1]), float(res[2])

class _PS_DP800(_Instrument, _SCPI_functions):
  desc = 'Rigol DP800 Series'
  proto = 'VISA'

  def connect(self):
    super(_PS_DP800, self).connect()
    if self._verbose:
      r = self.getIdentInfo()
      print "Vendor: " + r['vendor']
      print "ID: " + r['id']

_instrIndex()
