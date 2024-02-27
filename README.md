# BDD Course - python behave

### How to run tests
1. Create a `virtualenv` using PyCharm or in terminal (`virtualenv venv`).
2. Activate virtualenv. 
   - On Linux / MacOS: `. ./venv/bin/activate`
   - on Windows: `.\venv\Scripts\activate`
   - If you use PyCharm for running the tests, please open `File -> Settings -> Project: bdd-course-pytest-bdd -> 
   Python interpreter` and make sure that your virtualenv is selected. If not, click "add interpreter" -> 
   "add local interpreter", select "existing" and pick the one that you just created. Click "Apply".
3. Install the requirements for the project. Terminal: `pip install -r requirements.txt`. Or in PyCharm, go to 
   `requirements.txt file`, right-click on the editor space and select "Install all requirements";
4. Create test configuration:
   - create a JSON file that will contain tests configuration named `env_configuration.json` in the root (top) 
   folder of this project;
   - get the app url: ask the trainer to provide it ;)
   - put the following line into it: `{"app_url": "<app url>"}`
5. Now you can run the tests. 
   - To do that, in terminal: please open the terminal and run: `pytest`. 
   - To do that in PyCharm: please, open "Edit configruations..." on the right top corner of PyCharm, select Python
   Tests on the left menu, click "+" and select "pytest". That should do it :)

### How to create allure results

1. Install allure standalone using [these]([allure-report](allure-report)
[allure-results](allure-results)) steps. Please, note that you need Java
installed before you try installing allure standalone.
2. Open terminal.
3. Run `pip install requirements.txt` to make sure that `allure-pytest-bdd`
is installed.
4. Run tests with allure reports option: `pytest --alluredir allure-results`.
5. Generate allure report: `allure generate`.
6. Open allure report: `allure open`. You should see the report open in 
default browser.

_Note:_ when you're done, click Ctrl + C in the terminal to stop the process
to stop running allure process.

More info about allure can be found [here](https://allurereport.org/docs/how-it-works/)