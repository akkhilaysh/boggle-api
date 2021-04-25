import datetime

class Trie:
    """
    Initialize and Create a trie. Any functions for a trie data structure like add, search, includes can be added here.
    """

    def __init__(self, words,  root='*'):
        self.root = root
        self.words = words
        self.trie = {}

    @property
    def trie(self):
        return self._trie

    @trie.setter
    def trie(self, dict):
        for word in self.words:
            t = dict
            for letter in word:
                if letter not in t:
                    t[letter] = {}
                t = t[letter]
            t[self.root] = None
        self._trie = dict



class Boggle:
    """
    Methods, properties needed to solve the problem/game.

    Inherit the solveBoggle() function to write your own solution.
    """

    def __init__(self, board, dictionary):
        self.board = board
        self.dictionary = dictionary

    def solveBoggle(self):
        """
        Solves Boggle using a configured board, dictionary of words by string it in a trie built using the Trie Class.

        Returns:
            1. List of the words used,
            2. List of valid words,
            3. Number of valid words,
            4. Total time taken to solve the game.
        """

        #Started Timing Algorithm
        t0 = datetime.datetime.now()

        N = len(self.board)
        M = len(self.board[0])

        trieObj = Trie(self.dictionary)

        output = set()
        for row in range(N):
            for col in range(M):
                if self.board[row][col] not in trieObj.trie:
                    continue
                self.dfs(self.board, row, col, "", trieObj.trie, output)

        return len(self.dictionary), len(output), list(output), (datetime.datetime.now() - t0).total_seconds()

    def dfs(self, board, row, col, word, trie, output):
        """
            Depth-First-Search into one element in the board based on its location on the board.
            This method is called recursively to traverse through every connected letter associated with board[row][col].
        """

        #Return if movement is not valid or allowed
        if row < 0 or col < 0 \
                or row >= len(board) \
                or col >= len(board[0]) \
                or board[row][col] == '' \
                or board[row][col] not in trie:
            return

        #Store the current letter in a temporary variable
        c = board[row][col]
        _word = word + c

        if '*' in trie[c]:
            if len(_word) > 2:
                output.add(_word)
            if len(trie[c]) == 1:
                #return if the next node is empty, search doesn't need to go further.
                return

        # Marking a visted location '' so we don't reconsider this letter in the same recursive stack.
        board[row][col] = ''

        #Recursively calling dfs for valid movements allowed in the game.
        self.dfs(board, row - 1, col, _word, trie[c], output)  # up
        self.dfs(board, row + 1, col, _word, trie[c], output)  # down
        self.dfs(board, row, col - 1, _word, trie[c], output)  # left
        self.dfs(board, row, col + 1, _word, trie[c], output)  # right

        self.dfs(board, row - 1, col - 1, _word, trie[c], output)  # top-left
        self.dfs(board, row - 1, col + 1, _word, trie[c], output)  # top-right
        self.dfs(board, row + 1, col - 1, _word, trie[c], output)  # bottom-left
        self.dfs(board, row + 1, col + 1, _word, trie[c], output)  # bottom-right

        #Restoring the letter back after the recursively going through each of its valid connections.
        board[row][col] = c