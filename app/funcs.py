def counter(data):
    temp = data.b * data.b - 4 * data.a * data.c
    print(temp)
    print(4 ** 0.5)
    if temp < 0:
        return "Уравнение не имеет корней"
    elif temp == 0:
        return f"Корень уравнения x = {-(data.b / (2 * data.a))}"  # a -4 b28 c-49
    else:
        sqrt = (data.b * data.b - 4 * data.a * data.c) ** 0.5
        x1 = (-data.b + sqrt) / (2 * data.a)
        x2 = (-data.b - sqrt) / (2 * data.a)
        return f"Корни уравления x = {x1}, {x2}"  # a4 b5 c1
