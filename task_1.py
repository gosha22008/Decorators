from datetime import datetime
import os
path = os.getcwd()

# 1.Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции,
# аргументы, с которыми вызвалась и возвращаемое значение.
def decorator(old_function):

    def new_function(*args, **kwargs):
        date_time = str(datetime.now()).split(' ')
        name_function = old_function.__name__
        params = [args, kwargs]
        result = old_function(*args, **kwargs)
        dict = {}
        dict['Имя функции'] = [name_function]
        dict['Дата'] = [date_time[0]]
        dict['Время'] = [date_time[1]]
        dict['Аргументы'] = [params]
        dict['Результат'] = [result]
        with open('file_log', 'a', encoding='utf-8') as file:
            file.write(str(dict)+'\n')

        return result

    return new_function

# 2.Написать декоратор из п.1, но с параметром – путь к логам.
def param_decorator(path_log):

    def my_decorator(old_function):

        def new_function(*args, **kwargs):
            date_time = str(datetime.now()).split(' ')
            name_function = old_function.__name__
            params = [args, kwargs]
            result = old_function(*args, **kwargs)
            dict = {}
            dict['Имя функции'] = [name_function]
            dict['Дата'] = [date_time[0]]
            dict['Время'] = [date_time[1]]
            dict['Аргументы'] = [params]
            dict['Результат'] = [result]
            with open(path_log + '\\file_log', 'a', encoding='utf-8') as file:
                file.writelines(str(dict)+'\n')

            return result

        return new_function

    return my_decorator


my_decorator = param_decorator(path)


@decorator
def my_function():
    return('Старая функция')


my_function()

