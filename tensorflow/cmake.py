from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import text_format

import tensorflow.extra_actions_base_pb2 as extra_actions_base_pb2

arg = sys.argv[1]
xa_file = arg.split("=")[1]

with open(xa_file) as f:
    contents = f.read()
    info = extra_actions_base_pb2.ExtraActionInfo()
    info.ParseFromString(contents)
    print(info)
