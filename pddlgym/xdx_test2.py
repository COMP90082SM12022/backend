import pddlgym
from pddlgym_planners.fd import FD

# See `pddl/sokoban.pddl` and `pddl/sokoban/problem3.pddl`.
env = pddlgym.make("PDDLEnvSokoban-v0")
env.fix_problem_index(2)
obs, debug_info = env.reset()
planner = FD()
plan = planner(env.domain, obs)
for act in plan:
    print("Obs:", obs)
    print("Act:", act)
    obs, reward, done, info = env.step(act)
print("Final obs, reward, done:", obs, reward, done)
