from __future__ import division, print_function
import time
import random
import sys

import treedict

from toolbox import gfx
from natnet import FrameBuffer

import env
from surrogates.stemsim import calibration
from surrogates.stemsim import stemsensors
from surrogates.stemsim import stembot
from surrogates.stemsim import optivrepar
from surrogates.stemsim import stemcfg

cfg = treedict.TreeDict()

cfg.stem.dt = 0.01
cfg.stem.uid = int(sys.argv[1])
cfg.stem.verbose_com = True
cfg.stem.verbose_dyn = True

cfg.sprims.names     = ['push']
cfg.sprim.tip        = False
cfg.sprims.uniformze = False

cfg.mprim.name = 'dmpg'
cfg.mprim.motor_steps = 500
cfg.mprim.max_steps   = 500
cfg.mprim.uniformze   = False
cfg.mprim.n_basis     = 2
cfg.mprim.max_speed   = 1.0
cfg.mprim.end_time    = 1.45

cfg.mprim.init_states   = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
cfg.mprim.target_states = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

stem = stemcfg.stems[cfg.stem.uid]
M_trans = calibration.load_calibration(stem)
print("{}launching serial... {}".format(gfx.purple, gfx.end))
sb = stembot.StemBot(cfg)
vs = stemsensors.VrepSensors(cfg)

fb = FrameBuffer(40.0)
print("{}launching vrep... {}".format(gfx.cyan, gfx.end))
ovar = optivrepar.OptiVrepAR(verbose=False)

total = 1 if len(sys.argv) <= 2 else int(sys.argv[2])
count = 0
start_time = time.time()

print('')

try:
    while count < total:
        try:
            order = tuple(random.uniform(lb, hb) for lb, hb in sb.m_bounds)

            print("{}executing movement on stem...{}".format(gfx.purple, gfx.end), end='\r')
            sys.stdout.flush()

            # execute movement on stem
            fb.track(stem.optitrack_side)
            start, end = sb.execute_order(order)
            fb.stop_tracking()
            print('')
            time.sleep(0.01)

            # get optitrack trajectory
            opti_traj = fb.tracking_slice(start, end)
            count += 1

            # fill gaps
            opti_traj = calibration.transform.fill_gaps(opti_traj)
            vrep_traj = calibration.transform.opti2vrep(opti_traj, M_trans)

            print("{}executing movement in vrep...{}".format(gfx.cyan, gfx.end))

            # execute in vrep
            object_sensors, joint_sensors, tip_sensors = ovar.execute(vrep_traj)

            # produce sensory feedback
            effect = vs.process_sensors(object_sensors, joint_sensors, tip_sensors)
            #print("{}order:{} {}".format(gfx.purple, gfx.end, gfx.ppv(order)))
            print("{}effect:{} {}".format(gfx.cyan, gfx.end, gfx.ppv(effect)))

        except stembot.CollisionError:
            fb.stop_tracking()

finally:
    sb.close()

dur = time.time() - start_time

print("{} movements, {:.1f}s ({:.1f}s per movements)".format(total, dur, dur/total))