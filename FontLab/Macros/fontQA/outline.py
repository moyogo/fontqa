#FLM: outline test

from FL import *
from fontQAlib import TestSuite
from fontQA_Outline import *

mySuite = TestSuite()
Outline_Tests = mySuite.addBlock('Outline', 'Outline')
Outline_Tests.addItem(Contour_Statistic)
Outline_Tests.addItem(Node_Statistic)
Outline_Tests.addItem(Area_Statistic)
Outline_Tests.addItem(MinContourLength)
Outline_Tests.addItem(MinContourArea)
Outline_Tests.addItem(ExtremumPoint)
Outline_Tests.addItem(UnnecInflect)
Outline_Tests.addItem(UnnecExtreme)
mySuite.doTest()

