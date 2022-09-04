import re
class StringCalculator:
    def add(self, numbers):
        try:
            # if string is Empty
            if numbers == "":
                return 0
            else:
                # odd even count flag set for sum of odd and even indices
                odd = None
                even = None
                # initial flag set for Normal cases
                initialFlag = None
                # new delimiter list which will be provided by string
                newdelim = []
                # condition for different delimiter and sum of odd and even indices
                if '//' in numbers:
                    # if start with // then user provide new delimiter
                    if numbers.startswith('//'):
                        firstNindex = numbers.index("\n")
                        newdelimDummy = numbers[2:firstNindex]
                        # To check if length of delimiter is greater then one or not
                        if len(newdelimDummy) > 1:
                            # remove sqare brackets[] from new deimiter
                            newdelim.append(numbers[3:firstNindex - 1])
                            numbers = numbers[firstNindex + 1:]
                            num_list = re.split(f",|\n|{newdelim[0]}", numbers)
                        else:
                            newdelim.append(numbers[2])
                            numbers = numbers[4:]
                            num_list = re.split(f",|\n|{newdelim[0]}", numbers)
                    # goes in else when string contain "//" but not start with "//" then calculate odd or even indices sum
                    else:
                        flag = int(numbers[0])
                        numbers = numbers[3:]
                        if flag == 0:
                            odd = True
                        else:
                            even = True
                        num_list = re.split(",|\n", numbers)
                # if string not contain "//" then goes in else condition
                else:
                    num_list = re.split(",|\n", numbers)
                total = 0
                # set initial flag true if odd indices sum have to calculate
                if odd == True:
                    initialFlag = True
                # set initial flag false if even indices sum have to calculate
                elif even == True:
                    initialFlag = False
                # iterate string
                for num in num_list:
                    # if odd or even indices sum not needed to calculate
                    if initialFlag is None:
                        # if character is alphabet then convert into it's corresponding number
                        if num.isalpha():
                            total = total + (ord(num.lower()) - 96)
                        else:
                            # if number is negative then throw exception
                            if int(num) < 0:
                                L = [int(i) for i in num_list if not i.isalpha() and int(i) < 0]
                                raise Exception(f"Negatives not allowed {L}")
                            # if number is greater then 1000 then ignore it
                            if int(num) > 1000:
                                continue
                            total = total + int(num)
                    # odd or even indices sum calculate
                    elif initialFlag == True:
                        initialFlag = False
                        # if character is alphabet then convert into it's corresponding number
                        if num.isalpha():
                            total = total + (ord(num.lower()) - 96)
                        else:
                            # if number is negative then throw exception
                            if int(num) < 0:
                                L = [int(i) for i in num_list if not i.isalpha() and int(i) < 0]
                                raise Exception(f"Negatives not allowed - {L}")
                            # if number is greater then 1000 then ignore it
                            if int(num) >= 1000:
                                continue
                            total = total + int(num)
                    else:
                        initialFlag = True
                return total
        except Exception as e:
            return e
            
obj = StringCalculator()
UserInput=input("Enter Your String")
print(obj.add(UserInput))
