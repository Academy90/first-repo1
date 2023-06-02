result = []

def divider(a, b):
    if a < b:
        raise ValueError("a менше за b")
    if b > 100:
        raise IndexError("b більше за 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError as ve:
        print("ValueError - сталася!:", ve)
    except IndexError as ie:
        print("IndexError - сталася!:", ie)
    except Exception as e:
        print("ПОМИЛКА!:", e)

print(result)