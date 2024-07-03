# problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2502

# L = int(raw_input())
L = int(input())
while L is not 0:
    # bends = [str(x) for x in raw_input().split()]
    bends = [str(x) for x in input().split()]
    point = '+x'
    for bend in bends:
        if bend != 'No':
            bendDirection = bend[0]
            bendAxis = bend[1]
            pointDirection = point[0]
            pointAxis = point[1]
            if point == '+x':
                point = bend
            elif point == '-x':
                direction = '-' if bendDirection is '+' else '+'
                point = direction + bendAxis 
            elif pointAxis is 'y' and bendAxis is 'z': # any y and any z = any y
                point = point
            elif pointAxis is 'z' and bendAxis is 'y': # any z and any y = any z
                point = point
            elif pointAxis is 'y' and bendAxis is 'y':
                if pointDirection is '+': 
                    direction = '-' if bendDirection is '+' else '+'
                    point = direction + 'x' 
                elif pointDirection is '-': 
                    point = bendDirection + 'x' 
            elif pointAxis is 'z' and bendAxis is 'z':
                if pointDirection is '+': 
                    direction = '-' if bendDirection is '+' else '+'
                    point = direction + 'x' 
                elif pointDirection is '-': 
                    point = bendDirection + 'x' 
    print(point)
    # L = int(raw_input())
    L = int(input())