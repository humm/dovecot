from __future__ import division, print_function
import sys
import time

from pydyn import MotorSet
import env
from surrogates.stemsim import stemcfg

stem = stemcfg.stems[int(sys.argv[1])]
stem.cycle_usb()

ms = MotorSet(serial_id=stem.serial_id, motor_range=stem.motorid_range, verbose=True)
ms.zero_pose = stem.zero_pose

ms.compliant = False
# for m in ms.motors:
#     m.request_write('torque_enable', True)
time.sleep(0.1)
ms.max_speed  = 100
ms.torque_limit = 100
ms.pose = (20.0, 10.0, 10.0, 10.0, 10.0, 10.0)
time.sleep(1.0)
ms.pose = (1.0, 0.0, 0.0, 3.0, 0.0, -20.0)

time.sleep(3.0)
print("pos: [{}]".format(', '.join('{:.1f}'.format(p) for p in ms.pose)))
print("pos: [{}]".format(', '.join('{:.1f}'.format(m.position) for m in ms.motors)))