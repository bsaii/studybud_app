# studybud_app
This app was built on the idea of discord where a user can create a room for converstions and have other users join.


### How to run the app locally.
1. You have to set up a python virtual environment.
  > Here's how to do so
  > - Run `py venv .venv` or `py venv <specified_name>` in your terminal to create a python virtual environment.
  > - Run `.venv/scripts/activate` or `<specified_name/directory>/scripts/activate` to activate your virtual environment.
  > - To deactivate your virtual environment, you can do so by running `deactivate` in your terminal.

2. Now run `pip install -r requirements.txt` in your termianl to install dependencies in the requirements file.
3. (optional) Create a superuser by running `py manage.py createsuperuser` and follow the steps.
4. Finally, run the local server using `py manage.py runserver`.
