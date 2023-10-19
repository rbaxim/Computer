# type: ignore
# We don't want pyrght because it will cause errors
# Just basic assembly language in python
import computer as c
import sys as s
import os
#config
c.space = c.al.ALU.bit(8)
c.config.Update()
# assembly
c.al.set(1, 2)
c.al.set(2, 2)
c.al.ALU.add(3, 1, 2)
print()