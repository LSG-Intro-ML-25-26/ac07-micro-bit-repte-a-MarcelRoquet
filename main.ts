input.onButtonPressed(Button.A, function () {
    hand = hand + 1
    if (hand > 3) {
        hand = 1
    }
    if (hand == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (hand == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
input.onGesture(Gesture.Shake, function () {
    handCPU = randint(1, 3)
    if (handCPU == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (handCPU == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
input.onButtonPressed(Button.B, function () {
    handCPU = randint(1, 3)
    basic.showString("CPU")
    if (handCPU == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (handCPU == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    basic.showString("Tu")
    if (hand == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (hand == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    if (hand == 1) {
        if (handCPU == 2) {
            basic.showString("LOSE")
        } else if (handCPU == 3) {
            basic.showString("Guanyes")
        } else {
            basic.showString("empat")
        }
    } else if (hand == 2) {
        if (handCPU == 1) {
            basic.showString("gunayes")
        } else if (handCPU == 3) {
            basic.showString("perds")
        } else {
            basic.showString("empat")
        }
    } else if (handCPU == 1) {
        basic.showString("perds")
    } else if (handCPU == 2) {
        basic.showString("guanyes")
    } else {
        basic.showString("empat")
    }
})
let handCPU = 0
let hand = 0
hand = 0
basic.showString("Inici")
basic.forever(function () {
	
})
