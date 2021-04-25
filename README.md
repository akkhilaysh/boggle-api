# API: Solve Boggle
Solves Boggle by passing a board, dictionary of words using re-usable classes to setup the game and implement game logic. 


## Run using Docker

```bash
git clone https://github.com/akkhilaysh/boggle-api.git
```

```bash
docker image build -t boggle-api .
```

```bash
docker run -p 5000:5000 -d boggle-api
```

* Go to http://127.0.0.1:5000/hello to get basic information on how to use the api. (Also available below)


## Running Locally

```bash
git clone https://github.com/akkhilaysh/boggle-api.git
```

```bash
pip install -r requirements.txt
```

```bash
python application.py
```

## Usage

Send a GET request to /myboard/<int:size>/<string:board>

* Parameter Contraints
    * size: Size of the board should be between 3>size<11
    * board:
        *Only alphabets allowed
        *For a board of size {size}x{size} please enter { size x size } letters.


## Authors

ex. Akkhilaysh Shetty