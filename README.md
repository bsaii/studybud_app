# studybud_app
This app was built on the idea of discord where a user can create a room for converstions and have other users join.


### How to run the app locally.
1. You have to set up a python virtual environment.
  > Here's how to do so
  > - Run `py -m venv .venv` or `py -m venv <specified_name>` in your terminal to create a python virtual environment.
  > - Run `.venv/scripts/activate` or `<specified_name/directory>/scripts/activate` to activate your virtual environment.
  > - To deactivate your virtual environment, you can do so by running `deactivate` in your terminal.

2. Now run `pip install -r requirements.txt` in your termianl to install dependencies in the requirements file.
3. (optional) Create a superuser by running `py manage.py createsuperuser` and follow the steps.
4. Finally, run the local server using `py manage.py runserver`.


## Resources

### Create a virtual environment
To create a virtual environment, use the following command, where ".venv" is the name of the environment folder:
```
# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
python3 -m venv .venv

# Windows
# You can also use py -3 -m venv .venv
python -m venv .venv
```

> Tip: When you're ready to deploy the application to other computers, you can create a `requirements.txt` file with the command `pip freeze > requirements.txt` (`pip3` on macOS/Linux). The requirements file describes the packages you've installed in your virtual environment. With only this file, you or other developers can restore those packages using `pip install -r requirements.txt` (or, again, `pip3` on macOS/Linux). By using a requirements file, you need not commit the virtual environment itself to source control.

**Other Resources**
- [Django Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-django)
- [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)
- [Flask Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask)
