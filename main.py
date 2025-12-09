def on_button_pressed_a():
    global hand
    hand = hand + 1
    if hand > 3:
        hand = 1
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global handCPU
    handCPU = randint(1, 3)
    if handCPU == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif handCPU == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    global handCPU
    handCPU = randint(1, 3)
    basic.show_string("CPU")
    if handCPU == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif handCPU == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
    basic.show_string("Tu")
    if hand == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif hand == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
    if hand == 1:
        if handCPU == 2:
            basic.show_string("LOSE")
        elif handCPU == 3:
            basic.show_string("Guanyes")
        else:
            basic.show_string("empat")
    elif hand == 2:
        if handCPU == 1:
            basic.show_string("gunayes")
        elif handCPU == 3:
            basic.show_string("perds")
        else:
            basic.show_string("empat")
    elif handCPU == 1:
        basic.show_string("perds")
    elif handCPU == 2:
        basic.show_string("guanyes")
    else:
        basic.show_string("empat")
input.on_button_pressed(Button.B, on_button_pressed_b)

handCPU = 0
hand = 0
hand = 0
basic.show_string("Inici")

def on_forever():
    pass
basic.forever(on_forever)
