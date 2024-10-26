# Named Parameters

def divide(numerator, denominator):
    return numerator / denominator

answer = divide(denominator=2, numerator=10)
print(answer)

def long_function_name(
        name, age, height, weight, is_tall, is_short):
    pass

long_function_name(
    name="John",
    age=20,
    height=180,
    weight=70,
    is_tall=True,
    is_short=False
)

# *args

def add_all_numbers(*nums):
    total = 0
    for number in nums:
        total += number
    return total

answer = add_all_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(answer)

# **kwargs

def print_user_attributes(**attributes):
    for key, value in attributes.items():
        print(f"{key}: {str(value)}")

print_user_attributes(
    first_name="John",
    last_name="Doe",
    age=20,
    is_student=True,
    is_teacher=False
)