from flask_restful import abort

class SetupBoard:
    """
    Set-up the board by passing a string of the board and size of the board

    Validation for size: Size of the board should be between 3>size<11
    Validation for the board:
                Only alphabets
                Dependant on size.
                For a board of size {size}x{size} please enter { size x size } letters.

    """


    def __init__(self, board, size):
        self.board = board
        self.size = size

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, b):
        if not b.isalpha():
            abort(400, description=f'400 Bad request - Board should only contain alphabets.')
        self._board = b.lower()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, s):
        if len(self.board) >= 4 and len(self.board) <= 10:
            abort(400, description=f'400 Bad request  - Size of the board should be between 3>size<11')

        if len(self.board) != s*s:
            abort(400, description=f'400 Bad request  - For a board of size {s}x{s},'
                                   f'please enter {s*s} letters.')
        self._size = s

    def processed_board(self):
        return self.create_n_chunks(self.board, self.size)

    def create_n_chunks(self, l, n):
        return list(list(list(l)[i:i + n] for i in range(0, len(l), n)))


class SetupDictionary:
    """
    Set-up Dictionary vy passing a txt file with a list of valid words:

    Default Dictionary used: https://github.com/dwyl/english-words

    File info: words_alpha.txt contains only [[:alpha:]] words (words that only have letters, no numbers or symbols).

    Words property that contains a list of all the words extracted from the dictionary passed to it at object creation.
    """


    def __init__(self, filePath='meta/words_alpha.txt'):
        self.filePath = filePath
        self.words = []

    @property
    def filePath(self):
        return self._filePath

    @filePath.setter
    def filePath(self, f):
        if not f.lower().endswith('.txt'):
            abort(400, description=f'400 Bad request - Dictionary only accepts .txt files')
        self._filePath = f.lower()

    @property
    def words(self):
        return self._words

    @words.setter
    def words(self, w):
        for word in open(self.filePath).readlines():
            word = word.strip()
            if len(word) > 2:
                w.append(word)
        self._words = w
