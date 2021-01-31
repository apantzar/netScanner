#!/usr/bin/env python
import scapy.all as scapy

def scan():
   arpRequest = scapy.ARP()
   print (arpRequest.summary())
