try:
    grades = [6, 4, 7]
    print(grades[0])   # 6
    print(grades[-1])  # 7
    print(grades[3])
    print(grades[1])
except IndexError:
    print("problem with indexing")  # problem with indexing
print(grades[1])  # 4

try:
    print('hello' + 5)
except TypeError:
    print("problem with types")  # problem with types

try:
    print(100 / 0)
except ZeroDivisionError:
    print("problem with division by zero")  # problem with division by zero

try:
    result = some_function(user_input)
except ZeroDivisionError:
    print("problem with dividing by zero")
except Exception:  # IndexError, TypeError, ZeroDivisionError, NameError ...
    print("other problem")
except:
    print("yet another problem")  # KeyboardInterrupt (Ctrl-C)
    traceback.print_exc()  # prints last exception details
