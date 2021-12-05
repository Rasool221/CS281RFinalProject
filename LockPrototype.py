# Rasool Abbas & Sadam Farah
# CS281R UMKC 2021

fsmDiagram = {
    "0": {
        "a": "12",
        "b": "2",
        "alarm": "0",
        "locked": "1"
    },
    "2": {
        "a": "4",
        "b": "12",
        "alarm": "0",
        "locked": "1"
    },
    "4": {
        "a": "4",
        "b": "12",
        "alarm": "0",
        "locked": "1"
    },
    "6": {
        "a": "12",
        "b": "8",
        "alarm": "0",
        "locked": "1"
    },
    "8": {
        "a": "12",
        "b": "10",
        "alarm": "0",
        "locked": "1"
    },
    "10": {
        "a": "11",
        "b": "12",
        "alarm": "0",
        "locked": "1"
    },
    "11": {
        "a": "11",
        "b": "12",
        "alarm": "0",
        "locked": "0"
    },
    "10": {
        "a": "0",
        "b": "0",
        "alarm": "0",
        "locked": "1"
    },
    "12": {
        "a": "12",
        "b": "14",
        "alarm": "1",
        "locked": "1"
    },
    "14": {
        "a": "12",
        "b": "16",
        "alarm": "1",
        "locked": "1"
    },
    "16": {
        "a": "12",
        "b": "0",
        "alarm": "1",
        "locked": "1"
    }
}


class Lock:
    stateNum = -1
    
    alarm = ""
    locked = ""

    def __init__(self, _stateNum):
        self.stateNum = _stateNum
        self.alarm = fsmDiagram[str(self.stateNum)]["alarm"]
        self.locked = fsmDiagram[str(self.stateNum)]["locked"]

    def getNextState(self, input):
        currentState = fsmDiagram[str(self.stateNum)]
        return int(currentState[input])

    def getStatus(self):
        return "Locked: {}, Alarm: {}, State: {}".format(
            self.locked,
            self.alarm,
            self.stateNum
        )

    def processInput(self, input):
        self.stateNum = self.getNextState(input)
        self.alarm = fsmDiagram[str(self.stateNum)]["alarm"]
        self.locked = fsmDiagram[str(self.stateNum)]["locked"]


if __name__ == "__main__":
    l = Lock(0)

    while True:
        print(l.getStatus() + "\n")
        print("Please enter input (a or b): ", end="")
        
        btn = input().lower()

        while (not(btn == "a" or btn == "b")):
            print("Please enter correct input (a or b): ", end="")
            btn = input().lower()

        l.processInput(btn)

