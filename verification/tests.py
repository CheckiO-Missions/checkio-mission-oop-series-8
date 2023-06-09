init_code = """
if not "Car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Car' class?")

Car = USER_GLOBAL['Car']

if not "my_car" in USER_GLOBAL:
    raise NotImplementedError("Dude, where is 'my_car'?")

my_car = USER_GLOBAL['my_car']

if not isinstance(my_car, Car):
    raise TypeError("'my_car' should be an instance of 'Car' class")


if not hasattr(Car, "wheels"):
    raise AttributeError("Where is 'wheels' attribute of 'Car' class?")

if not hasattr(Car, "doors"):
    raise AttributeError("Where is 'doors' attribute of 'Car' class?")

if Car.wheels != "four":
    raise ValueError("'wheels' attribute should be equal 'four'")
    
if Car.doors != 4:
    raise ValueError("'doors' attribute should be equal 4")


if not '__init__' in vars(Car):
    raise NotImplementedError("Where is '__init__' method of 'Car' class?")

from inspect import signature

params = signature(Car.__init__).parameters
if not all((len(params) ==  3, 'self' in params, 'brand' in params, 'model' in params)):
    raise NotImplementedError("Check the number and names of '__init__' arguments")

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

if some_car1.brand != "Ford":
    raise ValueError("Value of 'some_car1' 'brand' must be 'Ford'")

if not hasattr(some_car1, "model"):
    raise NotImplementedError("Where is 'model' attribute of 'some_car1'?")

if not isinstance(some_car1.model, str):
    raise TypeError("'model' attribute of 'some_car1' should be of type 'str'")

if some_car1.model != "Mustang":
    raise ValueError("Value of 'some_car1' 'model' must be 'Mustang'")

if not "some_car2" in USER_GLOBAL:
    raise NotImplementedError("Where is 'some_car2'?")

some_car2 = USER_GLOBAL['some_car2']

if not isinstance(some_car2, Car):
    raise TypeError("'some_car2' should be an instance of 'Car' class")

if not hasattr(some_car2, "brand"):
    raise NotImplementedError("Where is 'brand' attribute of 'some_car2'?")
    
if not isinstance(some_car2.brand, str):
    raise TypeError("'brand' attribute of 'some_car2' should be of type 'str'")

if some_car2.brand != "":
    raise ValueError("Value of 'some_car2' 'brand' must remains default")

if not hasattr(some_car2, "model"):
    raise NotImplementedError("Where is 'model' attribute of 'some_car2'?")

if not isinstance(some_car2.model, str):
    raise TypeError("'model' attribute of 'some_car2' should be of type 'str'")

if some_car2.model != "Camaro":
    raise ValueError("Value of 'some_car2' 'model' must be 'Camaro'")


if not hasattr(Car, "working_engine"):
    raise AttributeError("Where is 'working_engine' attribute of 'Car' class?") 

if Car.working_engine != False:
    raise ValueError("'working_engine' attribute must have value 'False'")

if not 'start_engine' in vars(Car):
    raise NotImplementedError("Where is 'start_engine' method?")

params2 = signature(Car.start_engine).parameters
if not all((len(params2) ==  1, 'self' in params2)):
    raise NotImplementedError("'start_engine' argument(s) incorrect")

if not 'stop_engine' in vars(Car):
    raise NotImplementedError("Where is 'stop_engine' method?")

params3 = signature(Car.stop_engine).parameters
if not all((len(params3) ==  1, 'self' in params3)):
    raise NotImplementedError("'stop_engine' argument(s) incorrect")

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
    raise TypeError("'start_engine' was not overridden or called for 'my_electric_car'")

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
    raise TypeError("'start_engine' was not called for 'my_electric_car2'")

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

params5 = signature(Car.drive).parameters
if not all((len(params5) ==  2, 'self' in params5, 'distance' in params5)):
    raise NotImplementedError("Check number and names of 'drive' arguments")
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
        prepare_test(middle_code='''test_car = Car()''',
                     test="test_car.working_engine",
                     answer=False,
                     show_code="test_car = Car()"),
        prepare_test(middle_code='''import contextlib, io
with contextlib.redirect_stdout(io.StringIO()) as stdout:
    (test_car := Car()).start_engine()''',
                     test="test_car.working_engine, stdout.getvalue()",
                     answer=[True, "Engine has started\n"],
                     show_code="(test_car := Car()).start_engine()"),
        prepare_test(middle_code='''with contextlib.redirect_stdout(io.StringIO()) as stdout:
    (test_car := Car()).start_engine()
    test_car.stop_engine()''',
                     test="test_car.working_engine, stdout.getvalue()",
                     answer=[False, "Engine has started\nEngine has stopped\n"],
                     show_code='''(test_car := Car()).start_engine()
    test_car.stop_engine()'''),
        
        prepare_test(middle_code='''test_car = ElectricCar(30)''',
                     test="test_car.working_engine",
                     answer=False,
                     show_code="test_car = ElectricCar(30)"),
        prepare_test(middle_code='''with contextlib.redirect_stdout(io.StringIO()) as stdout:
    (test_car := ElectricCar(30)).start_engine()''',
                     test="test_car.working_engine, stdout.getvalue()",
                     answer=["Yes", "Electric motor has started\n"],
                     show_code="(test_car := ElectricCar(30)).start_engine()"),
        prepare_test(middle_code='''with contextlib.redirect_stdout(io.StringIO()) as stdout:
    (test_car := ElectricCar(30)).start_engine()
    test_car.stop_engine()''',
                     test="test_car.working_engine, stdout.getvalue()",
                     answer=["No", "Electric motor has started\nElectric motor has stopped\n"],
                     show_code='''(test_car := ElectricCar(30)).start_engine()
    test_car.stop_engine()'''),
#         prepare_test(middle_code='''import inspect''',
#                      test="'super().__init__' in inspect.getsource(ElectricCar.__init__)",
#                      answer=True,
#                      show_code=""),
        prepare_test(middle_code="Cars = Car(), ElectricCar(10), ElectricCar(20), Car(), ElectricCar(25), Car()",
                     test='''"".join(Cars[ind].drive(dist) for ind, dist in enumerate(("", 10, "", 15, 12, ""))''',
                     answer='''Wrong 'distance' value type\n
Driven 10 km on electric motor\n
Wrong 'distance' value type\n
Driven 15 km\n
Driven 12 km on electric motor\n
Wrong 'distance' value type\n''',
                     show_code="")
]}
