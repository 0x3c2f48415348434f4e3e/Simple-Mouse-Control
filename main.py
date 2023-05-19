from pynput import mouse
import time
get_controller = mouse.Controller()
get_button = mouse.Button

while(True):
    #print("\nCurrent position:", get_controller.position)
    get_controller.click(get_button.right,1)
    get_controller.click(get_button.left,1)
    get_controller.move(100,10)
    time.sleep(1)