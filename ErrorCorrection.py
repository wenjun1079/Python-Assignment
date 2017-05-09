# Wenjun Wang
#check whether the input is 12 bit and binary digits
def checkValid(s):
        if len(s) != 12:
                print("Error: Input string is not 12 digits long.")
                return False
        else:
                for v in s:
                        if v != '0' and v!= '1':
                                print("Error: Non-binary digits appears.")
                                return False
                        else:
                                return True
                        
#calculate c1,c2,c4,c8
def calculateC(s):
        #count 1's
        c = s.count('1')#cite https://zhidao.baidu.com/question/134478679455114805.html
        if c % 2 == 0 :
                c = 0
        else :
                c = 1
        return c

#if c1,c2,c4,c8 is mismatch, add value to sum
def calculateSum(c1,c2,c4,c8):
        sum = 0
        if c1 != int(s[0]):
                sum += 1
        if c2 != int(s[1]):
                sum += 2
        if c4 != int(s[3]):
                sum += 4
        if c8 != int(s[7]):
                sum += 8
        return sum

#correct wrong value
def changeD(d):
        if d == '0':
                d = '1'
        else:
                d = '0'
        return d

#according to sum, correct wrong bit and get correct 8 data bits   
def checkSum(sum, s):
        data = s
        if sum == 0:
                print("Great! No errors occurred.")
        if sum > 12:
                print("Sorry, there are more than two errors.")
        else:
                for var in range(1,12):
                        if sum == var:
                                print("bit", var, "in the transferred 12 bits is wrong.")
                                data = s[:var-1] + changeD(s[var-1]) + s[var:]
        correctS = data[2] + data[4:7] + data[8: ]
        return correctS
        
                


#main code
var = 1
while var == 1:
        s = input("Please enter a 12-bits string(press 'q' to quit): ") #input a string

        if s == 'q':
                print('Goodbye!')
                break

#check input string is valid
        if not checkValid(s) :
                print("Valid input")
                continue

#Calculate c1,c2,c4,c8               
        s1 = s[2:11:2]
        s2 = s[2] + s[5] + s[6] + s[9] + s[10]
        s4 = s[4] + s[5] + s[6] + s[11]
        s8 = s[8: ]
        c1 = calculateC(s1)
        c2 = calculateC(s2)
        c4 = calculateC(s4)
        c8 = calculateC(s8)

#Claculate sum
        sum = calculateSum(c1,c2,c4,c8)

#get correct 8 bits data
        correctS = checkSum(sum, s)
        print("Correct 8 data bits is: ",correctS)

