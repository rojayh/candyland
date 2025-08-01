def lowest_result(position, my_list):
    result = -1
    for element in my_list:
        if element > position:
            result = element
            break
    return result


class Board:

    red =    [1, 7,  14, 21, 27, 33, 39, 46, 52, 58, 64, 71, 77, 83, 89, 96,  103, 109, 115, 121, 127, 133, 134]
    purple = [2, 8,  15, 22, 28, 34, 40, 47, 53, 59, 65, 72, 78, 84, 90, 97,  104, 110, 116, 122, 128, 134]
    yellow = [3, 10, 16, 23, 29, 35, 41, 48, 54, 60, 66, 73, 79, 85, 91, 98,  105, 111, 117, 123, 129, 134]
    blue =   [4, 11, 17, 24, 30, 36, 43, 49, 55, 61, 67, 74, 80, 86, 93, 99,  106, 112, 118, 124, 130, 134]
    orange = [5, 12, 18, 25, 31, 37, 44, 50, 56, 62, 68, 75, 81, 87, 94, 100, 107, 113, 119, 125, 131, 134]
    green =  [6, 13, 19, 26, 32, 38, 45, 51, 57, 63, 70, 76, 82, 88, 95, 101, 108, 114, 120, 126, 132, 134]
    licorice = [47, 76, 89]
    plum = 9
    peppermint = 20
    gumdrop = 42
    peanut = 69 #nice
    lollipop = 92
    snowflake = 102

    def move(self, current_pos, color):
        match color:
            case "red":
                pos = lowest_result(current_pos, self.red)
            case "oran":
                pos = lowest_result(current_pos, self.orange)
            case "yell":
                pos = lowest_result(current_pos, self.yellow)
            case "gree":
                pos = lowest_result(current_pos, self.green)
            case "blue":
                pos = lowest_result(current_pos, self.blue)
            case "purp":
                pos = lowest_result(current_pos, self.purple)
            case "dred":
                temp = lowest_result(current_pos, self.red)
                if temp == 134:
                    pos = temp
                else:
                    pos = lowest_result(temp, self.red)

            case "doran":
                temp = lowest_result(current_pos, self.orange)
                if temp == 134:
                    pos = temp
                else:
                    pos = lowest_result(temp, self.orange)
            case "dyell":
                temp = lowest_result(current_pos, self.yellow)
                if temp == 134:
                    pos = temp
                else:
                    pos = lowest_result(temp, self.yellow)
            case "dgree":
                temp = lowest_result(current_pos, self.green)
                if temp == 134:
                    pos = temp
                else:
                    pos = lowest_result(temp, self.green)
            case "dblue":
                temp = lowest_result(current_pos, self.blue)
                if temp == 134:
                    pos = temp
                else:
                    pos = lowest_result(temp, self.blue)
            case "dpurp":
                temp = lowest_result(current_pos, self.purple)
                if temp == 134:
                    pos = temp
                else:
                    pos = lowest_result(temp, self.purple)
            case "peppermint":
                pos = self.peppermint
            case "gumdrop":
                pos = self.gumdrop
            case "peanut":
                pos = self.peanut
            case "lollipop":
                pos = self.lollipop
            case "snowflake":
                pos = self.snowflake
            case "plum":
                pos = self.plum
            case _:
                pos = -1

        # handle shortcuts
        # 5 -> 59
        # 35 -> 46
        if pos == 5:
            pos = 59
        elif pos == 35:
            pos = 46

        return pos
