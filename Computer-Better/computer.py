# type: ignore
import math as m
import time as t
import sys as s
import os
global addr
global space
space = 8
addr = []
global data
data = []
for i in range(1, space):
  addr.append(i)
pass
for i in addr:
  data.append(0)
pass
print("Started Computer")
class config:

  def Update():
    global oldspace
    oldspace = space
    if not space == oldspace:
      t.sleep(1)
      for i in addr:
        addr.pop(i)
      pass
      for i in data:
        data.pop(i)
      pass
      for i in range(1, space):
        addr.append(i)
      pass
      for i in addr:
        data.append(0)
      pass
    pass
    if int(space) > 640:
      s.set_int_max_str_digits(int(space))
    pass
    oldspace = space

  pass


pass


class al:
  # assembly language
  def read(reg):
    return data[reg]

  pass

  def set(regDist, set):
    data[regDist] = set
    return set

  pass

  def wait(ms):
    t.sleep(ms / 1000)
    return True

  pass

  class ALU:
    # Arithemtic Logic Unit
    def add(regDist, regA, regB):
      x = data[regA] + data[regB]
      data[regDist] = x
      return x

    pass

    def sub(regDist, regA, regB):
      x = data[regA] - data[regB]
      data[regDist] = x
      return x

    pass

    def mul(regDist, regA, regB):
      x = data[regA] * data[regB]
      data[regDist] = x
      return x

    pass

    def div(regDist, regA, regB):
      x = data[regA] / data[regB]
      data[regDist] = x
      return x

    pass

    def pow(regDist, regA, regB):
      x = m.pow(data[regA], data[regB])
      data[regDist] = x
      return x

    pass

    def powA(regDist, regA, regB):
      x = m.exp(data[regA], data[regB])
      data[regDist] = x
      return x

    pass

    def inc(regDist, reg):
      x = reg + 1
      data[regDist] = x
      return x

    pass

    def dec(regDist, reg):
      x = reg - 1
      data[regDist] = x
      return x

    pass

    def bit(bit):
      bits = "2" + str(bit)
      limit = m.pow(2, float(bit) - 1)
      return float(limit)

    pass

    def orr(regDist, regA, regB):
      x = regA | regB
      data[regDist] = x
      return x

    pass

    def andd(regDist, regA, regB):
      x = regA & regB
      data[regDist] = x
      return x

    pass

    def xor(regDist, regA, regB):
      x = regA ^ regB
      data[regDist] = x
      return x

    pass

    def lsh(regDist, regA, regB):
      x = regA << regB
      data[regDist] = x
      return x

    pass

    def rsh(regDist, regA, regB):
      x = regA >> regB
      data[regDist] = x
      return x

    pass

    def nor(regDist, regA, regB):
      x = not regA | regB
      data[regDist] = x
      return x

    pass

  pass


pass
