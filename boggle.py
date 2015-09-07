from trie import Trie

class Boggle:
    """
    Class that handles the API of the game, essentially, creating the board,
    checking the presence of the 
    """
    def __init__(self, file_name, board_side = 4):
        """
        Constructor of the board, it takes as parameter the size of the side of
        the board, and the file name where the letters are stored
        """
        self.letters = self.get_letters(file_name)
        self.board_side = board_side
        self.number_letters = board_side * board_side
        self.adjacency_matrix = self.get_adjacency_matrix(board_side)

    def __str__(self):
        description = ""

    def get_adjacency_matrix(self, board_side):
        """
        get_adjacency_matrix(board_side): returns the adjacency matrix which
                indicates which positions of the board are accessible from
                another position. The numbering of the positions starts at the
                top left corner
                and it proceeds left and down, for example for a 4x4 board

                        1    2    3    4
                        5    6    7    8
                        9   10   11   12
                       13   14   15   16

        board_side: the size of a side of the board. A value of 4 represents a
                4x4 board, a 5 represents a 5x5 board, and so on.

        Note for the future me!!
        Luckily, some day I will make this a bit more flexible, right now it
        just ignores the parameter and returns a 4x4 board
        """ 
        adjacency_matrix = [
            [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]
            ]
        return adjacency_matrix

    def find_word(self, target_word):
        mask = [True for ii in self.letters]
        unused = [True for ii in self.letters]
        return self.find_word_inner(unused, mask, target_word, 0)

    def find_word_inner(self, unused, mask, target_word, idx):
        for letter_idx in range(self.number_letters):
            if (mask[letter_idx] and unused[letter_idx] and
                    self.letters[letter_idx] == target_word[idx]):
                if idx == len(target_word) - 1:
                    return True
                else:
                    unused[letter_idx] = False
                    return self.find_word_inner(unused,
                            self.adjacency_matrix[letter_idx],
                            target_word, idx + 1)

    """
    def find_word(self, letters, unused, mask, target_word, idx, adj_matrix):

    0.upto mask.length do |letter_idx|
        if (mask[letter_idx] and
                unused[letter_idx] and
                (letters[letter_idx] == target_word[idx]))
            if idx == target_word.length - 1
                return true
            else
                unused[letter_idx] = false
                return find_word(letters, unused, adj_matrix[letter_idx],
                                                 target_word, idx + 1, adj_matrix)
            end
        end
    end
    return false
    """

    def get_letters(self, file_name):
        """
        get_letters(file_name): Read the letters that form the board, contained
        in the file with name file_name.
        """
        with open(file_name, 'r') as f:
            letters = []
            for line in f:
                letters.extend(line.strip().split(','))
        return letters

    def find_all_words(self):
        return
