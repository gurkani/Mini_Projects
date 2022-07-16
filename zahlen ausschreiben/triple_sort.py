#this class sortes the enterd number in 3 member groups
#its a simulation of money formating: 9,245,326
class TripleFormat:
    def __init__(self,txt_num = ''):
        self.txt_num = txt_num
        self.digit_len = len(self.makeit_start_with_nonezero(txt_num))

    #this function deletes spaces at the beginning and at the end of entered number
    #and deletes 0 at the neginning of the entered number
    def makeit_start_with_nonezero(self,txt_num = '' ):
        txt_num = txt_num.strip()
        final_value = str(int(txt_num))
        return final_value

    #text format function in 3 members group and return a list
    def triple_format(self,txt_num = ''):
        txt_group = ''
        txt_num = self.makeit_start_with_nonezero(txt_num)
        digit_len = len(txt_num)
        num_formated = []
        if digit_len <= 3:
            num_formated.append(txt_num)
        elif 4 <= digit_len:
            #this part determines how to sort the entery
            if (digit_len % 3) == 0:
                for digit in txt_num:
                    txt_group += digit
                    if len(txt_group) == 3:
                        num_formated.append(txt_group)
                        txt_group = ''
                        #indx += 1
            else:
                if (digit_len % 3 ) == 1:
                    txt_group = txt_num[0]
                    num_formated.append(txt_group)
                    txt_group = ''
                    for digit in txt_num[1:]:
                        txt_group += digit
                        if len(txt_group) == 3:
                            num_formated.append(txt_group)
                            txt_group = ''
                #we can use else too, 
                elif (digit_len % 3 ) == 2:
                    txt_group = txt_num[0:2]
                    num_formated.append(txt_group)
                    txt_group = ''
                    for digit in txt_num[2:]:
                        txt_group += digit
                        if len(txt_group) == 3:
                            num_formated.append(txt_group)
                            txt_group = ''
        return num_formated