import datetime
import functools
# wrapper - śledzenie pozostałych funkcji

def CreateFunctionWithWrapper(func): #argumentem jest funkcja którą chce śledzić
    def func_with_wrapper(*args, **kwargs): #ma przjmować takie same argumenty jak funkcje które są śledzone
        print('Function "{}" started at {}'.format(func.__name__,datetime.datetime.now().isoformat()))
        print('Following arguments were used:')
        print(args, kwargs)
        result = func(*args, **kwargs)
        print('Function returned {}'.format(result))
        return result
    return func_with_wrapper

@CreateFunctionWithWrapper
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print('Changing salary for {} to {} as bonus={}'.format(emp_name, new_salary, is_bonus))
    return new_salary

print(ChangeSalary('Johnson', 20000, True))

#ChangeSalary= CreateFunctionWithWrapper(ChangeSalary)

print(ChangeSalary('Johnson', 20000, is_bonus=True))

