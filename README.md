# API: Solve Boggle
Solves Boggle by passing a board, dictionary of words using re-usable classes to setup the game and implement game logic. 


# Getting Started:

## Run using Docker

```bash
git clone https://github.com/akkhilaysh/boggle-api.git
```

```bash
cd boggle-api
```

```bash
docker image build -t boggle-api .
```

```bash
docker run -p 5000:5000 -d boggle-api
```


Go to http://127.0.0.1:5000/hello to get basic information on how to use the api. (Also available below)


## Running Locally

```bash
git clone https://github.com/akkhilaysh/boggle-api.git
```

```bash
cd boggle-api
```

```bash
pip install -r requirements.txt
```

```bash
python application.py
```

Go to http://127.0.0.1:5000/hello to get basic information on how to use the api. (Also available below)


## Usage

Send a GET request to /myboard/<int:size>/<string:board>

* Parameter Contraints
    * size: Size of the board should be between 3>size<11
    * board:
        *Only alphabets allowed
        *For a board of size {size}x{size} please enter { size x size } letters.

*Example: http://127.0.0.1:5000/myboard/4/itbeoncufubwsnap


## Authors

Akkhilaysh Shetty
