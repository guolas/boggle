# ------------------------------------------------------------------------------
class Node
  attr_accessor :value, :char, :left, :mid, :right
  def initialize
    @value = nil
    @char = nil
    @left = nil
    @mid = nil
    @right = nil
  end
  def to_s
    string = @char << "[" << value << "]"
    unless @left.nil?
      string = string << @left.char
    end
    string = string << ', '
    unless @mid.nil?
      string = string << @mid.char
    end
    string = string << ', '
    unless @right.nil?
      string = string << @right.char
    end
    string = string << "\n"
    return string
  end
end

# ------------------------------------------------------------------------------
class Trie
  attr_accessor :root
  def initialize
    @root = nil
  end
  def to_s
    return print_node(@root, '')
  end
  def print_node(node, string)
    if node.nil?
      return string
    end
    string = print_node(node.left, string)
    string = print_node(node.mid, string)
    string = print_node(node.right, string)
    return string
  end
  def put(value)
    @root = put_inner(@root, value, value, 0)
  end
  def put_inner(node, key, value, idx)
    char = key[idx]
    if node.nil?
      node = Node.new
      node.char = char
    end
    if char < node.char
      node.left = put_inner(node.left, key, value, idx)
    elsif char > node.char
      node.right = put_inner(node.right, key, value, idx)
    elsif idx < key.length - 1
      node.mid = put_inner(node.mid, key, value, idx + 1)
    else
      node.value = value
    end
    return node
  end
  def get(value)
    node = get_inner(@root, value, 0)
    if node.nil?
      return nil
    else
      return node.value
    end
  end
  def get_inner(node, key, idx)
    if node.nil?
      return nil
    end
    char = key[idx]
    if char < node.char
      return get_inner(node.left, key, idx)
    elsif char > node.char
      return get_inner(node.right, key, idx)
    elsif idx < key.length - 1
      return get_inner(node.mid, key, idx + 1)
    else
      return node
    end
  end
end

# ------------------------------------------------------------------------------
# Function to find a word, starting with a letter
def find_word(letters, mask, target_word, idx, adj_matrix)
  0.upto mask.length do |letter_idx|
    if (mask[letter_idx] == 1 and (letters[letter_idx] == target_word[idx]))
      if idx = target_word.length - 1
        return true
      else
        return find_word(letters, adj_matrix[letter_idx], target_word, idx + 1,
                         adj_matrix)
      end
    end
  end
  return false
end

# ------------------------------------------------------------------------------
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

if false
# ------------------------------------------------------------------------------
  # Check if a word is in the board
  word_to_check = 'alien'

  # Now use the function defined
  File.new('./4x4_words.txt', 'r').readlines.each do |word|
    mask = Array.new(16, 1)
    puts find_word(letters, mask, word, 0, adjacency_matrix)
  end
end

# ------------------------------------------------------------------------------
# Find in the board all possible words contained in a dictionary

# First read the contents from the dictionary, and build the Trie from it
trie = Trie.new
File.new('./word.list', 'r').readlines.each do |word|
# File.new('./small.words', 'r').readlines.each do |word|
  trie.put(word.strip)
end

aa = trie.get('alien')
if aa.nil?
  puts "nil!!!!"
else
  puts aa
end
