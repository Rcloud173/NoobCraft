# def multiply(num:int) ->None:
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")

# if __name__ == "__main__":
#     num = 2
#     multiply(num)

def multiply(num:int) -> list[int]:
    result = []
    for i in range(1,11):
        result.append(num * i)
    return result



