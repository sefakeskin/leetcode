class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        length=len(digits)
        two="abc"
        three="def"
        four="ghi"
        five="jkl"
        six="mno"
        seven="pqrs"
        eigth="tuv"
        nine="wxyz"

        newDigits=[]
        for i in range(length):
            match digits[i]:
                case "2":
                    newDigits.append(two)
                case "3":
                    newDigits.append(three)
                case "4":
                    newDigits.append(four)
                case "5":
                    newDigits.append(five)
                case "6":
                    newDigits.append(six)
                case "7":
                    newDigits.append(seven)
                case "8":
                    newDigits.append(eigth)
                case "9":
                    newDigits.append(nine)
            
        #print(newDigits)
        
        combinations=[]
        match length:
            case 0:
                return combinations
            case 1:
                for i in range(len(newDigits[0])):
                    combinations.append(newDigits[0][i])
                return combinations
            case 2:
                for i in range(len(newDigits[0])):
                    for j in range(len(newDigits[1])):
                        combinations.append(newDigits[0][i]+newDigits[1][j])
                return combinations        
            case 3:
                for i in range(len(newDigits[0])):
                    for j in range(len(newDigits[1])):
                        for k in range(len(newDigits[2])):
                            combinations.append(newDigits[0][i]+newDigits[1][j]+newDigits[2][k])
                return combinations
            case 4:
                for i in range(len(newDigits[0])):
                    for j in range(len(newDigits[1])):
                        for k in range(len(newDigits[2])):
                            for l in range(len(newDigits[3])):
                                combinations.append(newDigits[0][i]+newDigits[1][j]+newDigits[2][k]+newDigits[3][l])            
                return combinations     
                                                                    





