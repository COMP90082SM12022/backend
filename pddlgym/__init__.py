"""Gym environment registration"""

#from . import tests

import matplotlib
# matplotlib.use("Agg")
from pddlgym.rendering import *
from gym.envs.registration import register
import gym

import os

# Save users from having to separately import gym
def make(*args, **kwargs):
    return gym.make(*args, **kwargs)

def register_pddl_env(name, is_test_env, other_args):
    dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pddl")
    domain_file = os.path.join(dir_path, "{}.pddl".format(name.lower()))
    gym_name = name.capitalize()
    problem_dirname = name.lower()
    if is_test_env:
        gym_name += 'Test'
        problem_dirname += '_test'
    problem_dir = os.path.join(dir_path, problem_dirname)
    try:
        print(gym_name)
        print("HereHereHereHereHereHereHereHere")
        register(
            id='PDDLEnv{}-v0'.format(gym_name),
            entry_point='pddlgym.core:PDDLEnv',
            kwargs=dict({'domain_file' : domain_file, 'problem_dir' : problem_dir,
                         **other_args}),
        )
    except Exception as e:
        print("testtest")
        print(e)
for env_name, kwargs in [
        ("tsp", {'operators_as_actions': True, 'dynamic_action_space': True}),
        ("xdxsokoban", {'operators_as_actions': True, 'dynamic_action_space': True})
]:
    print(env_name)
    other_args = {
        "raise_error_on_invalid_action": False,
    }
    kwargs.update(other_args)
    for is_test in [False, True]:
        register_pddl_env(env_name, is_test, kwargs)
    print("regitered!")

# Custom environments
for level in range(1, 8):
    register(
        id=f'SearchAndRescueLevel{level}-v0',
        entry_point=f'pddlgym.custom.searchandrescue:SearchAndRescueEnv',
        kwargs={'level' : level, 'test' : False, 'render_version' : 'slow'},
    )
    register(
        id=f'SearchAndRescueLevel{level}Test-v0',
        entry_point=f'pddlgym.custom.searchandrescue:SearchAndRescueEnv',
        kwargs={'level' : level, 'test' : True, 'render_version' : 'slow'},
    )
    register(
        id=f'PDDLSearchAndRescueLevel{level}-v0',
        entry_point=f'pddlgym.custom.searchandrescue:PDDLSearchAndRescueEnv',
        kwargs={'level' : level, 'test' : False, 'render_version' : 'slow'},
    )
    register(
        id=f'PDDLSearchAndRescueLevel{level}Test-v0',
        entry_point=f'pddlgym.custom.searchandrescue:PDDLSearchAndRescueEnv',
        kwargs={'level' : level, 'test' : True, 'render_version' : 'slow'},
    )

register(
    id='SmallPOSARRadius1-v0',
    entry_point='pddlgym.custom.searchandrescue:SmallPOSARRadius1Env',
)

register(
    id='SmallPOSARRadius0-v0',
    entry_point='pddlgym.custom.searchandrescue:SmallPOSARRadius0Env',
)

register(
    id='POSARRadius1-v0',
    entry_point='pddlgym.custom.searchandrescue:POSARRadius1Env',
)

register(
    id='POSARRadius1Xray-v0',
    entry_point='pddlgym.custom.searchandrescue:POSARRadius1XrayEnv',
)

register(
    id='POSARRadius0-v0',
    entry_point='pddlgym.custom.searchandrescue:POSARRadius0Env',
)

register(
    id='POSARRadius0Xray-v0',
    entry_point='pddlgym.custom.searchandrescue:POSARRadius0XrayEnv',
)


register(
    id='SmallMyopicPOSAR-v0',
    entry_point='pddlgym.custom.searchandrescue:SmallMyopicPOSAREnv',
)

register(
    id='TinyMyopicPOSAR-v0',
    entry_point='pddlgym.custom.searchandrescue:TinyMyopicPOSAREnv',
)


# Ignore certain files for pdoc documentation generation.
__pdoc__ = {'downward_translate': False, 'procedural_generation': False}

