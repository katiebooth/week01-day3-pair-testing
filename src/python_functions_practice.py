def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(string):
    return len(string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(string1, string2):
    return int(string1) + int(string2)


month_dict = {
        1: ["January", "Jan"],
        2: ["February", "Feb"],
        3: ["March", "Mar"],
        4: ["April", "Apr"],
        5: ["May", "May"],
        6: ["June", "Jun"],
        7: ["July", "Jul"],
        8: ["August", "Aug"],
        9: ["September", "Sep"],
        10: ["October", "Oct"],
        11: ["November", "Oct"],
        12: ["December", "Dec"],
    }

def number_to_full_month_name(month_number):
    return month_dict[month_number] [0]
# def number_to_short_month_name(month_number):
#     month_short_dict = {
#         1: "Jan",
#         2: "Feb",
#         3: "Mar",
#         4: "Apr",
#         5: "May",
#         6: "Jun",
#         7: "Jul",
#         8: "Aug",
#         9: "Sep",
#         10: "Oct",
#         11: "Nov",
#         12: "Dece",
#     }
#     return month_short_dict[month_number]
def number_to_short_month_name(month_number):
    return month_dict[month_number] [1]
def cube_volume(side_length):
    return side_length ** 3

def string_reverse(string):
    return string [::-1]

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9