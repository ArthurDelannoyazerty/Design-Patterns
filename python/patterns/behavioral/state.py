from __future__ import annotations
import abc

# ---------------------------------------------------------------------------- #
#                                Abstract Class                                #
# ---------------------------------------------------------------------------- #
class State(abc.ABC):
    def __init__(self, player: AudioPlayer = None):
       self.player = player

    def set_player(self, player: AudioPlayer):
        self.player = player

    @property
    def name(self):
        return self.__class__.__name__

    @abc.abstractmethod
    def on_play(self): pass

    @abc.abstractmethod
    def on_pause(self): pass

    @abc.abstractmethod
    def on_stop(self): pass


# ---------------------------------------------------------------------------- #
#                                Concrete Class                                #
# ---------------------------------------------------------------------------- #

# ---------------------------------- States ---------------------------------- #
class StoppedState(State):
    def on_play(self):
        print("Starting playback...")
        self.player.change_state(PlayingState(self.player))

    def on_pause(self):
        print("Cannot pause. Player is stopped.") # Invalid action in this state

    def on_stop(self):
        print("Already stopped.") # Invalid action in this state


class PlayingState(State):
    def on_play(self):
        print("Already playing.") # Invalid action

    def on_pause(self):
        print("Pausing playback.")
        self.player.change_state(PausedState(self.player))

    def on_stop(self):
        print("Stopping playback.")
        self.player.change_state(StoppedState(self.player))


class PausedState(State):
    def on_play(self):
        print("Resuming playback.")
        self.player.change_state(PlayingState(self.player))

    def on_pause(self):
        print("Already paused.") # Invalid action

    def on_stop(self):
        print("Stopping playback from paused state.")
        self.player.change_state(StoppedState(self.player))


# ------------------------------- Context Class ------------------------------ #
class AudioPlayer:
    def __init__(self, initial_state:State):
        self._state = initial_state
        initial_state.set_player(self)
        print(f"Player is initially: {self._state.name}")

    def change_state(self, new_state: State):
        self._state = new_state
        print(f"Player changed state to: {self._state.name}")

    def click_play(self):
        self._state.on_play()

    def click_pause(self):
        self._state.on_pause()

    def click_stop(self):
        self._state.on_stop()


# ---------------------------------------------------------------------------- #
#                                  Main/Client                                 #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    initial_state = StoppedState()
    player = AudioPlayer(initial_state)
    print("-" * 20)

    # Simulate a typical user session
    player.click_play()
    player.click_pause()
    player.click_play()
    player.click_stop()

    print("-" * 20)
    
    # Simulate invalid actions
    player.click_pause()  # Tries to pause when stopped
    player.click_stop()   # Tries to stop when already stopped


# ---------------------------------- Output ---------------------------------- #

# Player is initially: StoppedState
# --------------------
# Starting playback...
# Player changed state to: PlayingState
# Pausing playback.
# Player changed state to: PausedState 
# Resuming playback.
# Player changed state to: PlayingState
# Stopping playback.
# Player changed state to: StoppedState
# --------------------
# Cannot pause. Player is stopped.
# Already stopped.