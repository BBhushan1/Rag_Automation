def generate_code(function_name, parameters=None):

    if parameters:
        param_str = ", ".join([f'"{param}"' if isinstance(param, str) else str(param) for param in parameters])
        call_str = f"{function_name}({param_str})"
    else:
        call_str = f"{function_name}()"

    code_template = """
from automation_functions import {function_name}

def main():
    try:
        result = {call_str}
        if result is not None:
            print("{function_name} executed successfully. Result: " + str(result))
        else:
            print("{function_name} executed successfully.")
    except Exception as e:
        print(f"Error executing function: {{str(e)}}")

if __name__ == "__main__":
    main()
"""
    return code_template.format(function_name=function_name, call_str=call_str)