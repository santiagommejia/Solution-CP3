# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=514

keepReading = True
while keepReading:
    H, U, D, F = map(int, raw_input().split())
    climbingDeficit = float(float(U) * (float(F) / float(100)))
    if H is 0:
        keepReading = False
        break
    position = float(0)
    day = 0
    while True:
        dayClimbingDeficit = float(float(day) * climbingDeficit)
        dayClimbing = U - dayClimbingDeficit 
        position = position + dayClimbing if dayClimbing > 0 else position
        if position > H:
            print('success on day ' + str(day+1))
            break
        position -= D        
        if position < 0:
            print('failure on day ' + str(day+1))
            break
        day += 1
