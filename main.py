hand = 0

def on_gesture_shake():
    global hand
    hand = randint(1, 3)
    if hand == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
        music.play(music.string_playable("- - - - - - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
    elif hand == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
