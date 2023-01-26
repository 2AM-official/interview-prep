class Board:
    def __init__(self, board) -> None:
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        
    def next_move(self, player):
        res = []
        nxt_pos = [[player, 1], [player, -1]]
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == player:
                    for pos in nxt_pos:
                        nxt_row = row + pos[0]
                        nxt_col = col + pos[1]
                        if not self.is_in_board(nxt_row, nxt_col) or self.board[nxt_row][nxt_col] != 0:
                            continue
                        res.append([row, col, nxt_row, nxt_col])
        return res

    def is_in_board(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return True
        else:
            return False

def assert_next_move(test_case_name, actual, expected):
    assert len(actual) == len(expected) and sorted(actual) == sorted(expected), \
        "Test case {}: Expecting: {}, but got: {}".format(test_case_name, expected, actual)

board = Board([[1,1,1,1],[0,0,0,0],[-1,-1,-1,1]])
assert_next_move("test player1", board.next_move(1), [[0,0,1,1],[0,1,1,0],[0,1,1,2],[0,2,1,1],[0,2,1,3],[0,3,1,2]])
print('Succeeded')

