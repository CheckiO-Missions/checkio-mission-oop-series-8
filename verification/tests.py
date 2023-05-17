init_code = """
if not "Car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Car'?")

Car = USER_GLOBAL['Car']

if not '__init__' in vars(Car):
    raise NotImplementedError("Where is '__init__' method?")

from inspect import signature

params = signature(Car.__init__).parameters
if not all((len(params) ==  3, 'self' in params, 'brand' in params, 'model' in params)):
    raise NotImplementedError("Check '__init__' arguments")

if not 'drive' in vars(Car):
    raise NotImplementedError("Where is 'drive' method?")

params2 = signature(Car.drive).parameters
if not all((len(params2) ==  2, 'self' in params2, 'distance' in params2)):
    raise NotImplementedError("Check 'drive' arguments")

if not "yet_another_car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'yet_another_car'?")

yet_another_car = USER_GLOBAL['yet_another_car']

if not isinstance(yet_another_car, Car):
    raise TypeError("'yet_another_car' should be an instance of 'Car' class")

if not hasattr(yet_another_car, "brand"):
    raise NotImplementedError("Where is 'brand' attribute of 'yet_another_car' object?")
    
if not isinstance(yet_another_car.brand, str):
    raise TypeError("'brand' attribute should be of type 'str'")

if not hasattr(yet_another_car, "model"):
    raise NotImplementedError("Where is 'model' attribute of 'yet_another_car' object?")

if not isinstance(yet_another_car.model, str):
    raise TypeError("'model' attribute should be of type 'str'")

if not hasattr(yet_another_car, "is_used"):
    raise NotImplementedError("Where is 'is_used' attribute of 'yet_another_car' object?")

if not isinstance(yet_another_car.is_used, bool):
    raise TypeError("'is_used' attribute should be of type 'bool'")

if not yet_another_car.is_used:
    raise Warning("drive some km's with 'yet_another_car'")
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}

TESTS = {
    "First": [
        prepare_test(middle_code='''''',
                     test="",
                     answer="")]}