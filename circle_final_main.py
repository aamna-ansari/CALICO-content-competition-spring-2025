def circle():
    T = int(input())
    for _ in range(T):
        N = int(input())
        x_values = []
        y_values = []
        for _ in range(N):
            x, y = map(float, input().split())
            x_values.append(x)
            y_values.append(y)
        min_x = min(x_values)
        max_x = max(x_values)
        min_y = min(y_values)
        max_y = max(y_values)
        width = max_x - min_x
        height = max_y - min_y
        area = width * height
        print(area)
# Call the function
circle()