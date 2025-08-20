import mlflow

def calculator(a, b, c, undefined):
    # Normal operations
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else None  # Avoid division by zero

    # Special undefined calculation
    if undefined == "undef":
        undef_result = a / c if c != 0 else "Error: division by zero"
    else:
        undef_result = None

    return addition, subtraction, multiplication, division, undef_result

if __name__ == "__main__":
    a, b, c, undefined = 5, 2, 0, "undef"

    with mlflow.start_run():
        add, sub, mul, div, undef_result = calculator(a, b, c, undefined)
        
        mlflow.log_param("a", a)
        mlflow.log_param("b", b)
        mlflow.log_param("c", c)
        mlflow.log_param("undefined_flag", undefined)
        
        print(f"Addition: {add}")
        print(f"Subtraction: {sub}")
        print(f"Multiplication: {mul}")
        print(f"Division: {div}")
        print(f"Undefined result: {undef_result}")
        
        mlflow.log_param("undefined_result", undef_result)


# Commands
# python experiment.py
# mlflow ui
