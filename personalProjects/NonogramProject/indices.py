#input two empty list into function
def arrangement(col_list, row_list, cellMAP):
    # how many cells are in a row/column
    count = 0

    # turn row and column list into list of list
    # each of the list inside will represent a certain
    # column or row

    for i in range(len(cellMAP)):
        col_list.append([])
        row_list.append([])

    # find how arrangements of cells in each column
    for col in range(len(cellMAP)):
        for row in range(len(cellMAP)):

            if cellMAP[row][col] == 1:
                # add to the count when a cell is present
                count += 1
                # what if that cell is the last in the column?
                if row == len(cellMAP) - 1:
                    # add count to list for column data
                    col_list[col].append(count)
                    # reset count for next column
                    count = 0

            # what if a streak of cells stops in column?
            elif cellMAP[row][col] == 0 and count >= 1:
                # add count to list for column data
                col_list[col].append(count)
                # reset for next set of cells in row
                count = 0

    # find arrangement for each row
    for x in range(len(cellMAP)):
        for y in range(len(cellMAP)):

            # add to the count when a cell is present
            if cellMAP[x][y] == 1:
                count += 1
                # what if that cell is the last in the row?
                if y == len(cellMAP) - 1:
                    # add count to list for row data
                    row_list[x].append(count)
                    # reset count for next row
                    count = 0

            # what that streak of cells stops in row?
            elif cellMAP[x][y] == 0 and count >= 1:
                # add count to list for row data
                row_list[x].append(count)
                # reset for next set of cells in row
                count = 0