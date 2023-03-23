import numpy as np
import pyedflib

data = pyedflib.EdfReader('1.rec')
signal = data.readSignal(6)
label = data.getSignalLabels()
head = data.getSignalHeaders()
print(data)
print(label)
print(head)