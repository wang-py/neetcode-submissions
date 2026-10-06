class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_count = 0
        row_unique = 0
        col_count = 0
        col_unique = 0
        block_count = 0
        block_unique = 0
        for i in range(9):
            row_num = [x for x in board[i] if x != "."]
            row_count += len(row_num)
            row_unique += len(set(row_num))
            col = {}
            col_num = []
            block = {}
            block_num = []
            start_row = 3 * int(i / 3)
            start_col = 3 * int(i % 3)
            for j in range(9):
                if board[j][i] != ".":
                    col_num.append(board[j][i])
                    col[board[j][i]] = (j, i)
                cur_block_num = board[start_row + int(j / 3)][start_col + j % 3]
                if cur_block_num != ".":
                    block_num.append(cur_block_num)
                    block[cur_block_num] = (start_row + int(j / 3), start_col + j % 3)
            # print(f"the block is: {block}")
            block_count += len(block_num)
            block_unique += len(block.keys())
            col_count += len(col_num)
            col_unique += len(col.keys())
        
        if col_count != col_unique or row_count != row_unique or block_count != block_unique:
            return False
        
        return True