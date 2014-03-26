import collections
import numbers

import forest

desc = forest.Tree()
desc._strict(True)

# FIXME should not not be in a branch
desc._isinstance('partial_mvt', bool)



    # Hardware stem config
desc._branch('stem')
# the stem number
desc._isinstance('stem.uid', numbers.Integral)
# FIXME meaning ?
desc._isinstance('stem.dt', numbers.Real)
# FIXME diff between the two ?
desc._isinstance('stem.verbose_com', bool)

desc._isinstance('stem.verbose_dyn', bool)



    # V-REP config
desc._branch('vrep')
# do we load vrep or not ?
desc._isinstance('vrep.load', bool)
# pass of the physic engine per frame (max 200)
desc._isinstance('vrep.ppf', numbers.Integral)

desc._isinstance('vrep.headless', bool)

desc._isinstance('vrep.vglrun', bool)

desc._isinstance('vrep.calibrdir', str)
# on mac, we need to know where vrep is
desc._isinstance('vrep.mac_folder', str)

    # Sensory primitives
desc._branch('sprims')

# the scene to load in vrep
# if equal to 'cube_center', experiments are pure simulation, then 'vrep_cube_center.ttt' is loaded
# else, 'ar_cube_center.ttt' is loaded
desc._isinstance('sprims.scene', str)

# the names of the sensory primitives whose sensory feedback is computed
desc._isinstance('sprims.names', collections.Iterable)

# do we track the tip during sim ?
desc._isinstance('sprims.tip', bool)

# recast every sensory dimension between 0 and 1 ?
desc._isinstance('sprims.uniformize', bool)

# use collision detection to avoid running non-colliding episodes ?
desc._isinstance('sprims.prefilter', bool)



    # Motor primitives
desc._branch('mprim')

# name of the motor primitive
desc._isinstance('mprim.name', str)

# the number of position (and possibly velocity) orders executed
desc._isinstance('mprim.motor_steps', numbers.Integral)

# defines when the simulation is finished
desc._isinstance('mprim.max_steps', numbers.Integral)

# uniformize motor orders dimension between 0 and 1 ?
desc._isinstance('mprim.uniformize', bool)

# how many basis for the dmp ?
desc._isinstance('mprim.n_basis', numbers.Integral)

# the maximum speed of the motors # FIXME units ?
desc._isinstance('mprim.max_speed', numbers.Real)

# when does the dmp trajectory end ?
desc._isinstance('mprim.end_time', numbers.Real)

# starting position of the stem
desc._isinstance('mprim.init_states', collections.Iterable)

# target position of the stem
desc._isinstance('mprim.target_states', collections.Iterable)

desc._describe('mprim.angle_ranges', instanceof=collections.Iterable,
               docstring='The range of the angles of the joints around the zero position the motor primitives bounds its values into')