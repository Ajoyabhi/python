def calculate(h, m):
    if (h < 0 or m < 0 or m > 60):
        print("wrong input")
    if (m == 60):
        h += 1
        m = 0
        if (h > 12):
            h = h - 12
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m
    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)
    if (angle < 0):
        angle = -angle
    return angle


n = int(input())
while (n > 0):
    h, m = map(int, input().split())
    print("angle", calculate(h, m))
    n -= 1