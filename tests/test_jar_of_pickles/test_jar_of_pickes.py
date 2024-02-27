import json

from pytest_bdd import scenario, given, when, then, parsers, scenarios


# Each scenario that you have in feature files have to be defined in Python:
# Option #1: The scenario below will tell pytest to run only "Spinning the lid should allow to open the jar of
#   pickles" scenario. It will ignore others, as it doesn't know they exist:
@scenario('jar_of_pickles.feature',
          'Spinning the lid should allow to open the jar of pickles')
def test_jar_of_pickles():
    pass


# Option #2: If you want to tell pytest to run all the scenarios in a feature file, you can do it this way:
scenarios("jar_of_pickles.feature")


# Option #3: You can also "attach" a regular python test to a scenario. Then you just say which test
#   you'd like to "attach" using the decorator (same as in option #1), but you don't need the step definitions:
@scenario('jar_of_pickles.feature',
          'Spinning the lid should allow to open the jar of pickles - duplicate with Pytest-like test')
def test_jar_of_pickles(pickles):
    print("Spinning the lid should allow to open the jar of pickles 3")
    for _ in range(2):
        pickles.append({"closed": True})
    pickles[0]["closed"] = False
    assert pickles[0]["closed"] == False
    assert pickles[1]["closed"] == True


# We don't use context here, but instead we use regular pytest fixtures (like "pickles" here, that come from
#   conftest.py "pickles" fixture):
@given(parsers.parse("user has {number:d} closed jar(s) of pickles"))
def step_definition(number, pickles):
    for _ in range(number):
        pickles.append({"closed": True})


# You can also specify target_fixture that will store step return value into a new fixture with given name.
#   Here we store "number - 1" into "active_jar_index" fixture and then use it step "user should be able to
#   take the lid off" below.
@given(parsers.parse("user grabs jar number {number:d}"), target_fixture="active_jar_index")
def step_definition(number):
    return number - 1


@when("user spins the lid")
def step_definition():
    pass


@when("the lid loosens up")
def step_definition():
    pass


@then("user should be able to take the lid off", target_fixture="pickles")
def step_definition(pickles, active_jar_index):
    pickles[active_jar_index]["closed"] = False
    return pickles


@then("user should be able to take the lids off all the jars", target_fixture="pickles")
def step_definition(pickles, active_jars):
    for jar in active_jars:
        pickles[jar]["closed"] = False
        return pickles


@then(parsers.parse('jar of pickles number {number:d} should be opened'))
def step_definition(number, pickles):
    assert pickles[number - 1]["closed"] == False


@then(parsers.parse('jar of pickles number {number:d} should be closed'))
def step_definition(number, pickles):
    assert pickles[number - 1]["closed"] == True


@when(parsers.parse('user grabs jars number {jars_list}'), target_fixture="active_jars")
def step_definition(jars_list, pickles):
    jars_list = json.loads(jars_list)
    for jar_number in jars_list:
        pickles[jar_number-1]["closed"] = False
    return jars_list


@then(parsers.parse('jars {jars_list} should be opened'))
def step_definition(jars_list, pickles):
    jars_list = json.loads(jars_list)
    for jar_number in jars_list:
        assert pickles[jar_number - 1]["closed"] == False
