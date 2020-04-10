Labcharger! - Battery charging software for your lab
====================================================

This software makes possible to use a regulated power supply to charge batteries. It implements logic of a smart charger to make sure that batteries are treated correctly accordig their type. Labcharger! controls your power supply, gets feedback from connected battery and step by step delivers proper amount of power to your battery.

How Labcharger! works you can see here: [https://youtu.be/D2OLo1EAESY](https://youtu.be/D2OLo1EAESY)

Requirements
============

* Regulated power supply supporting VISA I/O API and SCPI commands set.
* Python with PyVISA package and pyvisa-py backend.

Installation
============

1. Checkout this repository. PIP package is coming soon.
2. Install pyvisa and pyvisa-py packages.

Using Labcharger!
=================

Connect your computer with power supply, connect a battery with output channel 1 and start batterycharger.py from your command line.

    batterycharger.py [-h] [-v] -i INSTRUMENT -d ADDRESS -b BATTERY

Labcharger! supports following options:

-h Shows short help and hints.
-v Verbose mode to show debug messages and battery feedback info during charging.
-i Power supply you are using. Labcharger! was tested only with Rigol DP832A, but adding another instruments is pretty easy.
-d Address of power supply with VISA notation.
-b Battery type. NiMH is currently the only one implemented battery type.

Example

    batterycharger.py -i DP800 -i TCPIP::192.168.0.1::INSTR -b NiMH
