# ip-3
Integrated project - African Leadership College


[Brief description of the application]

## Installation

Make sure you have python3 installed with venv. If you don't have [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/), you can install it with:

```bash
python3 -m pip install --user virtualenv
```

Clone the repository:

```bash
git clone https://github.com/Emmastro/tatu-ip-group3.git
```

Cd on the root folder of the project

Make a .env file and make any random set of characters your secret key. The .env file can contain (as an example):
```bash
SECRET_KEY=123
```


Create the virtual environment with
```bash
make create_environment
```

Then, you can activate it with:
```bash
source env/bin/activate
```

And install dependencies with:
```bash
make install
```
With all dependencies installed, you can check other quick make commands from the Makefile.

Apply migrations using the following command:
```bash
 python manage.py migrate
```

To run the django server, use the command:
```bash
python manage.py runserver
```

You can the go to your browser and type: http://127.0.0.1:8000/

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contributors


## License

