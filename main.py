from core.state import AppState
from audio.detector import ShinyDetector
from vision.screen_match import ScreenMatcher
from core.controller import DetectorController
from gui.app import SoundDetectorGUI

if __name__ == "__main__":
    state = AppState()
    detector = ShinyDetector(state)
    matcher = ScreenMatcher()
    controller = DetectorController(state, detector, matcher)
    SoundDetectorGUI(state, controller)