# src/main.py

import gym
import gym_super_mario_bros
from gym_super_mario_bros.actions import COMPLEX_MOVEMENT
from nes_py.wrappers import JoypadSpace
from pynput import keyboard

# Initialize the game environment
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, COMPLEX_MOVEMENT)

# Define action mappings for Super Mario Bros
actions = {
    'a': 6,  # Move left
    'w': 5,  # Jump
    'd': 1,  # Move right
    's': 10,  # Some other action (e.g., crouch or pause, depending on the action set)
}

# Create a set to keep track of active actions
active_actions = set()

def on_press(key):
    try:
        if key.char in actions:
            active_actions.add(key.char)  # Add action to active actions
    except AttributeError:
        pass

def on_release(key):
    try:
        if key.char in actions:
            active_actions.remove(key.char)  # Remove action from active actions
    except AttributeError:
        if key == keyboard.Key.esc:
            return False  # Stop listener

def get_current_action():
    """Get the current action based on active keys."""
    if not active_actions:
        return 0  # Default action (no action)
    # Return the last pressed action from the active actions set
    return actions[list(active_actions)[-1]]  # Get action corresponding to last pressed key

# Start the keyboard listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Game loop
done = True
while True:
    if done:
        state = env.reset()  # Reset the environment when the game is done
    action = get_current_action()  # Get the current action based on pressed keys
    state, reward, done, info = env.step(action)  # Execute the action
    env.render()  # Render the game screen
