from __future__ import division, print_function
import sys
import time

from pydyn import MotorSet
import env
from dovecot.stemsim import stemcfg

uid = None if len(sys.argv) == 1 else int(sys.argv[1])

stem = stemcfg.stems[uid]
stem.cycle_usb()

ms = MotorSet(serial_id=stem.serial_id, motor_range=(0, 253), timeout=10, verbose=True)

def change(id_change):
    for m in ms.motors:
        if m.id == id_change[0]:
            print("changing id of motor {} to {}".format(*id_change))
            m.id = id_change[1]
            time.sleep(1.0)

change((1, 13))
#change((52, 11))