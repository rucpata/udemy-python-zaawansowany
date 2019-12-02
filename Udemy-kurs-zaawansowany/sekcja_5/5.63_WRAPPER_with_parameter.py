import datetime
import functools
# wrapper - śledzenie pozostałych funkcji

#logFilePath = r'/Users/wlasciciel/Desktop/programowanie/udemy/python/python_zaawansowany/Udemy-kurs-zaawansowany/sekcja_5/function_log.txt'
def CreateFunctionWithWrapper_LogToFile(logFilePath):
   def CreateFunctionWithWrapper(func): #argumentem jest funkcja którą chce śledzić
        def func_with_wrapper(*args, **kwargs): #ma przjmować takie same argumenty jak funkcje które są śledzone
            file = open(logFilePath,"a") #otwarcie pliku
            file.write("-"*20 + "\n")
            file.write('Function "{}" started at {}'.format(func.__name__,datetime.datetime.now().isoformat()))
            file.write('Following arguments were used:')
            file.write(" ".join("{}".format(x) for x in args))
            file.write("\n")
            file.write(" ".join("{}={}".format(k,v) for (k,v) in kwargs.items()))
            file.write("\n")
            result = func(*args, **kwargs)
            file.write('Function returned {}'.format(result))
            file.close() #zamknięcie pliku
            return result
        return func_with_wrapper
   return CreateFunctionWithWrapper

@CreateFunctionWithWrapper_LogToFile (r'/Users/wlasciciel/Desktop/programowanie/udemy/python/python_zaawansowany/Udemy-kurs-zaawansowany/sekcja_5/change_salary_log.txt')
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print('Changing salary for {} to {} as bonus={}'.format(emp_name, new_salary, is_bonus))
    return new_salary

@CreateFunctionWithWrapper_LogToFile (r'/Users/wlasciciel/Desktop/programowanie/udemy/python/python_zaawansowany/Udemy-kurs-zaawansowany/sekcja_5/change_position_log.txt')
def ChangePosition(emp_name, new_position):
    print('CHANGING POSTION FOR {} TO {} '.format(emp_name, new_position))
    return new_position


print(ChangeSalary('Johnson', 20000, True))
print(ChangePosition('Johnson', 20000))

