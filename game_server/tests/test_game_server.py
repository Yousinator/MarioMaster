# tests/test_game_server.py

import pytest
import gym
import gym_super_mario_bros
from gym_super_mario_bros.actions import COMPLEX_MOVEMENT
from nes_py.wrappers import JoypadSpace

def test_game_server_initialization():
    env = gym_super_mario_bros.make('SuperMarioBros-v0')
    env = JoypadSpace(env, COMPLEX_MOVEMENT)
    assert env is not None

def test_game_server_step():
    env = gym_super_mario_bros.make('SuperMarioBros-v0')
    env = JoypadSpace(env, COMPLEX_MOVEMENT)
    env.reset()
    state, reward, done, info = env.step(env.action_space.sample())
    assert state is not None
    assert isinstance(reward, float)
    assert isinstance(done, bool)
    assert isinstance(info, dict)

def test_environment():
    env = gym_super_mario_bros.make('SuperMarioBros-v0')
    env = JoypadSpace(env, COMPLEX_MOVEMENT)
    state = env.reset()
    assert state is not None

    action = 0  # Default action
    state, reward, done, info = env.step(action)
    assert state is not None
    assert reward is not None
    assert done is False  # The game should not be done immediately