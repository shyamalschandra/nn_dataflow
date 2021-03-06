""" $lic$
Copyright (C) 2016-2017 by The Board of Trustees of Stanford University

This program is free software: you can redistribute it and/or modify it under
the terms of the Modified BSD-3 License as published by the Open Source
Initiative.

If you use this program in your research, we request that you reference the
TETRIS paper ("TETRIS: Scalable and Efficient Neural Network Acceleration with
3D Memory", in ASPLOS'17. April, 2017), and that you send us a citation of your
work.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the BSD-3 License for more details.

You should have received a copy of the Modified BSD-3 License along with this
program. If not, see <https://opensource.org/licenses/BSD-3-Clause>.
"""

from nn_dataflow import Network
from nn_dataflow import InputLayer, ConvLayer, FCLayer, PoolingLayer

'''
ZFNet

Zeiler and Fergus, 2013
'''

NN = Network('ZFNet')

NN.set_input(InputLayer(3, 224))

NN.add('conv1', ConvLayer(3, 96, 110, 7, 2))
NN.add('pool1', PoolingLayer(96, 55, 3, strd=2))
# Norm layer is ignored.
NN.add('conv2', ConvLayer(96, 256, 26, 5, 2))
NN.add('pool2', PoolingLayer(256, 13, 3, strd=2))
# Norm layer is ignored.
NN.add('conv3', ConvLayer(256, 512, 13, 3))
NN.add('conv4', ConvLayer(512, 1024, 13, 3))
NN.add('conv5', ConvLayer(1024, 512, 13, 3))
NN.add('pool3', PoolingLayer(512, 6, 3, strd=2))
NN.add('fc1', FCLayer(512, 4096, 6))
NN.add('fc2', FCLayer(4096, 4096, 1))
NN.add('fc3', FCLayer(4096, 1000, 1))

