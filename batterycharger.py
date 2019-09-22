#!/usr/bin/env python

import argparse
import charger

def getopts():
  parser = argparse.ArgumentParser(description="Smart battery charger with bench programmable power supply")
  parser.add_argument('-v', '--verbose', action='store_true', help='show additional debug info')
  parser.add_argument('-i', metavar='INSTRUMENT', help='type of power supply',\
    choices=charger.instrument.all.keys(), required=True)
  parser.add_argument('-d', metavar='ADDRESS', help='VISA address of power supply', required=True)
  parser.add_argument('-b', metavar='BATTERY', help='type of battery to be charged',\
    choices=charger.battery.all.keys(), required=True)
  return parser.parse_args()
  
def main():
  args = getopts()
  ch = charger.Charger(args.i, args.d, args.b, args.verbose)
  ch.charge()

main()
