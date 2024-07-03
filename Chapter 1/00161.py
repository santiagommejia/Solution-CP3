MAX_SECONDS = 5 * 60 * 60

def allGreenBySecond(scenario, second):
    for light in scenario:
        isGreen = (second % (2*light)) < light - 5
        if not isGreen:
            return False
    return True

def getResult(scenario):
    currentSecond = scenario[0] * 2
    while currentSecond <= MAX_SECONDS:
        allGreen = allGreenBySecond(scenario, currentSecond)
        if allGreen:
            return currentSecond
        currentSecond += 1
    return currentSecond

def getFormattedResult(seconds):
    if seconds > MAX_SECONDS:
        return 'Signals fail to synchronise in 5 hours'
    else:
        hours = int(seconds/3600)
        hours = '0' + str(hours)
        seconds = seconds % 3600
        minutes = int(seconds/60)
        minutes = '0' + str(minutes) if minutes < 10 else str(minutes)
        seconds = seconds % 60
        sec = '0' + str(seconds) if seconds < 10 else str(seconds)
    return hours + ':' + minutes + ':' + sec


keepReading = True
lights = []
while keepReading:
    # line = map(int, raw_input().split())
    line = list(map(int, input().split()))
    if line == [0, 0, 0]:
        keepReading = False
    else:
        lights += line
scenario = []
for light in lights:
    if light != 0:
        scenario.append(light)
    else:
        scenario.sort()
        seconds = getResult(scenario)
        scenario = []
        formattedResult = getFormattedResult(seconds)
        print(formattedResult)
    