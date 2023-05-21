init_code = """
if not "Car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Car'?")

Car = USER_GLOBAL['Car']

if not '__init__' in vars(Car):
    raise NotImplementedError("Where is '__init__' method?")

from inspect import signature

params = signature(Car.__init__).parameters
if not all((len(params) ==  3, 'self' in params, 'brand' in params, 'model' in params)):
    raise NotImplementedError("Check the number and names of '__init__' arguments of 'Car'")

if not "my_car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'my_car'?")

my_car = USER_GLOBAL['my_car']

if not isinstance(my_car, Car):
    raise TypeError("'my_car' should be an instance of Car class")

if my_car.brand != "" or my_car.model != "":
    raise Warning("'my_car' must have default values as 'brand' and 'model'")
    
if not "some_car1" in USER_GLOBAL:
    raise NotImplementedError("Where is 'some_car1'?")

some_car1 = USER_GLOBAL['some_car1']

if not isinstance(some_car1, Car):
    raise TypeError("'some_car1' should be an instance of 'Car' class")

if not hasattr(some_car1, "brand"):
    raise NotImplementedError("Where is 'brand' attribute of 'some_car1'?")
    
if not isinstance(some_car1.brand, str):
    raise TypeError("'brand' attribute of 'some_car1' should be of type 'str'")

if not hasattr(some_car1, "model"):
    raise NotImplementedError("Where is 'model' attribute of 'some_car1'?")

if not isinstance(some_car1.model, str):
    raise TypeError("'model' attribute of 'some_car1' should be of type 'str'")

if not "some_car2" in USER_GLOBAL:
    raise NotImplementedError("Where is 'some_car2'?")

some_car2 = USER_GLOBAL['some_car2']

if not isinstance(some_car2, Car):
    raise TypeError("'some_car2' should be an instance of 'Car' class")

if not hasattr(some_car2, "brand"):
    raise NotImplementedError("Where is 'brand' attribute of 'some_car2'?")
    
if not isinstance(some_car2.brand, str):
    raise TypeError("'brand' attribute of 'some_car2' should be of type 'str'")

if not hasattr(some_car2, "model"):
    raise NotImplementedError("Where is 'model' attribute of 'some_car2'?")

if not isinstance(some_car2.model, str):
    raise TypeError("'model' attribute of 'some_car2' should be of type 'str'")

if not hasattr(some_car1, "working_engine"):
    raise NotImplementedError("Where is 'working_engine' attribute of 'some_car1' object?")

if not isinstance(some_car1.working_engine, bool):
    raise TypeError("'working_engine' attribute should be of type 'bool'")

if not hasattr(some_car2, "working_engine"):
    raise NotImplementedError("Where is 'working_engine' attribute of 'some_car2' object?")

if not isinstance(some_car2.working_engine, bool):
    raise TypeError("'working_engine' attribute should be of type 'bool'")

if not 'start_engine' in vars(Car):
    raise NotImplementedError("Where is 'start_engine' method?")

params2 = signature(Car.start_engine).parameters
if not all((len(params2) ==  1, 'self' in params2)):
    raise NotImplementedError("Check 'start_engine' arguments")

if not 'stop_engine' in vars(Car):
    raise NotImplementedError("Where is 'stop_engine' method?")

params3 = signature(Car.stop_engine).parameters
if not all((len(params3) ==  1, 'self' in params3)):
    raise NotImplementedError("Check 'stop_engine' arguments")

if not some_car1.working_engine:
    raise Warning("'some_car1' has not been started: method is not implemented or method call absent")

if not some_car2.working_engine:
    raise Warning("'some_car2' has not been started: method is not implemented or method call absent")

if not "ElectricCar" in USER_GLOBAL:
    raise NotImplementedError("Where is 'ElectricCar'?")

ElectricCar = USER_GLOBAL['ElectricCar']

if not issubclass(ElectricCar, Car):
    raise TypeError("'ElectricCar' should be a child of 'Car' class")

if not '__init__' in vars(ElectricCar):
    raise NotImplementedError("Where is '__init__' method of 'ElectricCar'?")

params4 = signature(ElectricCar.__init__).parameters
if not all((len(params4) ==  4, 'self' in params4, 'brand' in params4, 'model' in params4, 'battery_capacity' in params4)):
    raise NotImplementedError("Check the number and names of '__init__' arguments of 'ElectricCar'")

if not "my_electric_car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'my_electric_car'?")

my_electric_car = USER_GLOBAL['my_electric_car']

if not isinstance(my_electric_car, ElectricCar):
    raise TypeError("'my_electric_car' should be an instance of 'ElectricCar' class")

if not hasattr(my_electric_car, "brand"):
    raise NotImplementedError("Where is 'brand' attribute of 'my_electric_car' object?")
    
if not isinstance(my_electric_car.brand, str):
    raise TypeError("'brand' attribute should be of type 'str'")

if not hasattr(my_electric_car, "model"):
    raise NotImplementedError("Where is 'model' attribute of 'my_electric_car' object?")

if not isinstance(my_electric_car.model, str):
    raise TypeError("'model' attribute should be of type 'str'")

if not hasattr(my_electric_car, 'battery_capacity'):
    raise NotImplementedError("Where is 'battery_capacity' attribute of 'my_electric_car' object?")

if not isinstance(my_electric_car.battery_capacity, int):
    raise TypeError("'battery_capacity' attribute should be of type 'int'")

if not hasattr(my_electric_car, "working_engine"):
    raise NotImplementedError("Where is 'working_engine' attribute of 'my_electric_car' object?")

if not isinstance(my_electric_car.working_engine, str):
    raise TypeError("'start_engine' or 'stop_engine' were not overridden or called")

if my_electric_car.working_engine != "Yes":
    raise Warning("'my_electric_car' has not been started")

if not "my_electric_car2" in USER_GLOBAL:
    raise NotImplementedError("Where is 'my_electric_car2'?")

my_electric_car2 = USER_GLOBAL['my_electric_car2']

if not isinstance(my_electric_car2, ElectricCar):
    raise TypeError("'my_electric_car2' should be an instance of 'ElectricCar' class")

if not hasattr(my_electric_car2, "brand"):
    raise NotImplementedError("Where is 'brand' attribute of 'my_electric_car2' object?")
    
if not isinstance(my_electric_car2.brand, str):
    raise TypeError("'brand' attribute should be of type 'str'")

if not hasattr(my_electric_car2, "model"):
    raise NotImplementedError("Where is 'model' attribute of 'my_electric_car2' object?")

if not isinstance(my_electric_car2.model, str):
    raise TypeError("'model' attribute should be of type 'str'")

if not hasattr(my_electric_car2, 'battery_capacity'):
    raise NotImplementedError("Where is 'battery_capacity' attribute of 'my_electric_car2' object?")

if not isinstance(my_electric_car2.battery_capacity, int):
    raise TypeError("'battery_capacity' attribute should be of type 'int'")

if not hasattr(my_electric_car2, "working_engine"):
    raise NotImplementedError("Where is 'working_engine' attribute of 'my_electric_car2' object?")

if not isinstance(my_electric_car2.working_engine, str):
    raise TypeError("'start_engine' or 'stop_engine' not overridden or called")

if my_electric_car2.working_engine != "No":
    raise Warning("'my_electric_car2' has not been stopped")

if not "my_electric_car3" in USER_GLOBAL:
    raise NotImplementedError("Where is 'my_electric_car3'?")

my_electric_car3 = USER_GLOBAL['my_electric_car3']

if not isinstance(my_electric_car3, ElectricCar):
    raise TypeError("'my_electric_car3' should be an instance of 'ElectricCar' class")

if not hasattr(my_electric_car3, "brand"):
    raise NotImplementedError("Where is 'brand' attribute of 'my_electric_car3' object?")
    
if not isinstance(my_electric_car3.brand, str):
    raise TypeError("'brand' attribute should be of type 'str'")

if not hasattr(my_electric_car3, "model"):
    raise NotImplementedError("Where is 'model' attribute of 'my_electric_car3' object?")

if not isinstance(my_electric_car3.model, str):
    raise TypeError("'model' attribute should be of type 'str'")

if not hasattr(my_electric_car3, 'battery_capacity'):
    raise NotImplementedError("Where is 'battery_capacity' attribute of 'my_electric_car3' object?")

if not isinstance(my_electric_car3.battery_capacity, int):
    raise TypeError("'battery_capacity' attribute should be of type 'int'")

if not hasattr(my_electric_car3, "working_engine"):
    raise NotImplementedError("Where is 'working_engine' attribute of 'my_electric_car3' object?")

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