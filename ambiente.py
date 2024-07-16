from PIL import ImageGrab

def capture_screen():
    screen = ImageGrab.grab()
    return screen
