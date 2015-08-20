# This matrix is fixed for the boggle board, so no need to do fancy things with
# it.
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
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0]]

# Read the board from a file and place the letters in the corresponding order
# according to their position in the board:
#           1  2  3  4
#           5  6  7  8
#           9 10 11 12
#          13 14 15 16
letters = []
File.new('./4x4_board.txt', 'r').readlines.each do |line|
  letters.concat(line.strip.split(','))
end

# Check if a word is in the board
word_to_check = 'alien'

# Function to find a word, starting with a letter
def find_word(letters, mask, target_word, idx, adj_matrix)
  0.upto mask.length do |letter_idx|
    if (mask[letter_idx] == 1 and (letters[letter_idx] == target_word[idx]))
      if idx = target_word.length - 1
        return true
      else
        return find_word(letters, adj_matrix[letter_idx], target_word, idx + 1, adj_matrix)
      end
    end
  end
  return false
end

# Now use the function defined
File.new('./4x4_words.txt', 'r').readlines.each do |word|
  mask = Array.new(16, 1)
  puts find_word(letters, mask, word, 0, adjacency_matrix)
end
