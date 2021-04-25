try:
    from flask import Flask
    from flask_restful import Resource, Api

    from game.setup import SetupBoard, SetupDictionary
    from game.logic import Trie, Boggle
    import datetime

except Exception as e:
    print(f'Some of the modules are missing {e}')

app = Flask(__name__)
api = Api(app)

class MyBoggleBoard(Resource):
    """
    Gets an string and integer required to solve boggle.

    Uses class objects from game.setup and game.logic to safely setup the board and supplemented dictionary and solve boggle.

    Returns
        1. Total Number of words used in the dictionary
        2. Number of words found
        3. Time taken (seconds) to solve the probelm
        4. Board entered by the user,
        5. List of valid words from the dictionary that solve the game,
    """


    def get(self, board, size):

        # Set-up the board using the SetupBoard class by passing a string of the board and size of the board.
        b = SetupBoard(board, size)

        # Default Dictionary used: https://github.com/dwyl/english-words
        # Pass a .txt file
        w = SetupDictionary()

        # Create a new Boggle game using the Boggle class
        game = Boggle(b.processed_board(), w.words)

        # Calling solveBoggle offered by the Boggle class
        total_words, num_of_words_found, output_list, time_taken = game.solveBoggle()

        return {
                'totalWords': total_words,
                "numOfWordsFound": num_of_words_found,
                'timeTaken': time_taken,
                'yourBoard': b.processed_board(),
                'outputList': output_list,
                }


class Hello(Resource):
    """
    Returns some quick information on how to use the web service and some constraints.
    """


    def get(self):
        return {
            'usage': 'Send a GET request to /myboard/<int:size>/<string:board>. Example: http://127.0.0.1:5000/myboard/4/itbeoncufubwsnap',
            'contraints': [
                {
                    'size': 'Size of the board should be between 3>size<11',
                    'board':
                        [
                            'Only alphabets allowed',
                            'For a board of size {size}x{size} please enter { size x size } letters.',
                        ]
                }
            ],
        }

api.add_resource(MyBoggleBoard, '/myboard/<int:size>/<string:board>')
api.add_resource(Hello, '/hello')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
