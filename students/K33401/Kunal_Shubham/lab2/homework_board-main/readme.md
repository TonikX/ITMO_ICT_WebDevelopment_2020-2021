# Homework Board

## How to run (Linux)

Homework Board requires [Python3](https://python.org/) to run.

**Install Python**

```sh
$ sudo apt install python3
```

**Install Venv and create a virtual enviroment**

```sh
$ pip3 install venv
homework_board$ python3 -m venv env
```

**Activate the virtual enviroment**

```sh
homework_board$ source env/bin/activate 
```

**Install the dependecies**

```sh
(env) homework_board$ pip3 install -r requirements.txt
```

**Generate SECRET_KEY**

Generate a **SECRET_KEY** from **[this](https://djecrety.ir/)** website.

Create a **.env** file and paste your **SECRET_KEY**

```sh
(env) homework_board $ touch .env
(env) homework_board $ echo "SECRET_KEY=your_secret_key" >> .env
```

**Run migrations**

```sh
(env) homework_board $ python3 manage.py makemigrtions
(env) homework_board $ python3 manage.py migrate
```

**Run the Server**

```sh
(env) homework_board $ python3 manage.py runserver
```