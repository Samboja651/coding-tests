size = input("") # 9 27
col_size, row_size = size.split(" ")
col_size, row_size = int(col_size), int(row_size)

def mat_pattern(col_size, row_size):
    pattern1 = "-"
    pattern2 = ".|."
    message = "WELCOME"


    col_mid_point = col_size // 2 +1
    first_half = ""
    for column in range(1, col_size + 1):
        if column == col_mid_point:
            print(message.center(row_size, "-"))
        if column < col_mid_point:
            print(pattern2.center(row_size, "-"))
            pattern2 += ".|..|."
        if column > col_mid_point:
            pattern2 = pattern2[6:]
            print(pattern2.center(row_size, "-"))
    return

mat_pattern(col_size, row_size)