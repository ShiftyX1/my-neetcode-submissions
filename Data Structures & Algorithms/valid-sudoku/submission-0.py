class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                b_index = (r//3)*3 + c//3
                if value in rows[r] or value in columns[c] or value in boxes[b_index]:
                    return False
                rows[r].add(value)
                columns[c].add(value)
                boxes[b_index].add(value)
        return True