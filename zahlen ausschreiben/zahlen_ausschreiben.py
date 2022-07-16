#import triple_sort
#numbers in words to -> 10 ^27
#its easy to develope this mini app
#to get larger numeric amounts in words you have to just add the values to the tuples(num_large and num_large_eine)
#This mini app is developed by Mohammad Ali Gurkani
#The ast module helps Python applications to process trees of the Python abstract syntax grammar. 
from ast import Num
#triple_sort: this class sortes the enterd number in 3 members groups
#its a simulation of money formating: 9,245,326 
from triple_sort import TripleFormat
#constant variables
one_digit_numbers = {'0':'null','1':'eins','2' :'zwei','3':'drei','4':'vier','5':'fünf','6':'sechs','7':'sieben','8':'acht','9':'neun'}
numbers_dict = {'1':'ein','2' :'zwei','3':'drei','4':'vier','5':'fünf','6':'sechs','7':'sieben','8':'acht','9':'neun','10':'zehn',
    '11':'elf','12':'zwölf','13':'deizehn','14':'vierzehn','15':'fünfzehn','16':'sechzehn','17':'siebzehn','18':'achtzehn','19':'neunzehn',
    '20':'zwanzig','30':'dreißig','40':'vierzig','50':'fünfzig','60':'sechzig','70':'siebzig','80':'achtzig','90':'neunzig'}
num_large_eine = ('einhundert','eintausend','eine Million','eine Milliarde','eine Billion','eine Billiarde','eine Trillion','eine Trilliarde','eine Quadrillion','eine Quadrilliarde')
num_large = ('hundert','tausend','Millionen','Milliarden','Billionen','Billiarden','Trillionen','Trilliarden','Quadrillionen','Quadrilliarden')
eins = 'eins'
hundert = 'hundert'
#these variables is used to switch between values in order to check if the sent
# value to the function three_digit, the last three digits are
maindigits_len = 1
is_end_digit = True

def tree_digits(tree_digit_num = ''):
    first_digit = ''
    second_digit = ''
    third_digit = ''
    inwords = ''
    tree_digit_num = str(int(tree_digit_num))
    if maindigits_len == 1:
        first_digit = tree_digit_num
        inwords = one_digit_numbers[first_digit]
    elif len(tree_digit_num) == 1 and maindigits_len != 1 and  is_end_digit:
        if tree_digit_num == '0':
            inwords = ''
        elif tree_digit_num == '1':
            inwords = eins
        else:
            inwords = numbers_dict[tree_digit_num]
    elif len(tree_digit_num) == 2:
        first_digit = tree_digit_num[0]
        second_digit = tree_digit_num[1]
        if int(tree_digit_num)<=20 or second_digit == '0':
            inwords = numbers_dict[tree_digit_num]
        else:
            inwords = numbers_dict [second_digit] + 'und' + numbers_dict[first_digit+'0']
    elif len(tree_digit_num) == 3:
        first_digit = tree_digit_num[0]
        second_digit = tree_digit_num[1]
        third_digit = tree_digit_num[2]
        if second_digit == '0' and third_digit == '0' :
            inwords = numbers_dict[first_digit] + hundert
        elif second_digit == '0' and is_end_digit:
            inwords = one_digit_numbers[first_digit]+ hundert + one_digit_numbers[third_digit]
        elif second_digit == '0' and is_end_digit == False:
            if third_digit == '0':
                inwords = one_digit_numbers[first_digit]+ hundert
            else:
                inwords = one_digit_numbers[first_digit]+ hundert + numbers_dict[third_digit]
        else:
            twodigit = second_digit + third_digit
            if int(twodigit)<=20 or third_digit == '0':
                inwords_local = numbers_dict[twodigit]
            else:
                inwords_local = numbers_dict [third_digit] + 'und' + numbers_dict[second_digit+'0']
            inwords = numbers_dict[first_digit] + hundert + inwords_local            
    return inwords

#this function can return any number in words (10^27)
#its easy to develope this mini app
#to get larger numeric amounts in words you have to just add the values to the tuples(num_large and num_large_eine) 
def all_digits(input_num = ''):
    input_num = str(int(input_num.strip()))
    inwords = ''
    global is_end_digit
    if int(input_num) < 1000:
        is_end_digit = True
        inwords = tree_digits(input_num)
    else:
        obj_format = TripleFormat(input_num)
        input_num_formated = obj_format.triple_format(input_num)
        #maindigits_len = len(input_num)
        #is_end_digit = False
        index_num = 0
        select_large = len(input_num_formated)-1
        for lst_element in input_num_formated:
            if index_num == len(input_num_formated)-1:
                is_end_digit = False
                inwords = inwords + tree_digits(lst_element)
            else:
                first_element = input_num_formated[index_num]
                if int(first_element) == 1:
                    if select_large == 1:
                        inwords = inwords + num_large_eine[select_large]
                    else:
                        inwords = inwords + num_large_eine[select_large] + ' '
                else:
                    is_end_digit = False
                    if int(first_element) != 0:
                        if select_large == 1:
                            inwords = inwords + tree_digits(lst_element) + num_large[select_large]
                        else:
                            inwords = inwords + tree_digits(lst_element) + ' ' + num_large[select_large] + ' '
                select_large -= 1
                index_num += 1
    return inwords.strip()


def main():
    global maindigits_len 
    while True:
        input_num = input('Please enter a number to write it down in words(to exit enter "exit"): ').strip()
        if input_num.lower() == 'exit':
            print('Done!!!')
            break
        elif not input_num.isnumeric():
            print('Please enter a numeric value!!!')
            print('######################################')
            pass
        input_num = str(int(input_num))
        if len(input_num)>29:
            print('More than maximum(10^27)!!!!!')
            print('######################################')
            pass
        maindigits_len = len(input_num)
        print(all_digits(input_num))


    

main()
