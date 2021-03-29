import numpy as num
import json
import statistics as stat
import sys 

#####CLASS START HERE#####
class Data:

    def info(self,list0):
        """in this function return the information that you put in the number list"""
        
        std = num.std(list0)
        mean = num.mean(list0)
        median = num.median(list0)
        information =  f"standard deviation: {std}\nmean: {mean}\nmedian: {median}\n" 
        return information
        
    def store(self,list0):
        """this function dump the number data information"""
        filename = 'info_storage.json'
        with open(filename, 'w') as f:
            stored = json.dump(list0,f)

    def load(self):
        """this function load the data dumped in the json file"""
        filename = 'info_storage.json'
        with open(filename) as f:
           l_data = json.load(f)
           return l_data 

#####CLASS ENDS HERE#####


i = Data()
#this are intructions of how to work with the program
####################################################################################################################################
print('\nthis code give you the information of the following things:')
print('Standard Deviation:\nMean:\nMedian:\n')
print('only answer with "y", "n", and "q" for quit\n')
print('if you want to print your latest number data information type "y"\nif u want to create a new number data type "c" for create')
#####################################################################################################################################
#the main code starts here.
words = ['y','Y','n','N','q','Q','c','C']

while True:

    #####################################################################
    print('\n\t### MENU ###\n')
    print('type "q" to quit at any moment\n')
    print('would you like to print your latest saved data ?(y/n)')
    #####################################################################

    #this is the main while loop block where you give directions to the computer
    #this whle loop is created for directions

    ### directions start here ###
    user = input('\ntype here: ')
    #this is the first nested if statement
    if user == "y" or user == 'Y' in words:
        #this are the secondary directions of the the code
        #here are three nested if statements, it might be a little confusing on this part for beguinners
        stored = i.load()
        print(stored)
        print('would you like to print the information of your data?\n')
        user = input('\ntype here: ')

        if user == "y" or user == 'Y' in words:
            print('ok\n')
            print(i.info(stored))
            sys._clear_type_cache()
            continue    

        elif user == 'n' or user == 'N' in words:
            print('\nok')
            print('would you like to go to the MENU(y/n)?\n')
            print('type "n" to quit\n')
            user = input('\ntype here: ')

            if user == "y" or user == 'Y' in words:
                print('\nok')
                continue
            elif user == 'n' or user == 'N' in words:
                print('ok \nquiting...')
                break
            elif user == "":
                continue

        elif user == "":
            continue
        elif user not in words:
            print(f'{user} is not in the list of commands')
            continue
        elif user == 'q' or user == 'Q' in words:
            print('quiting...')
            break

    elif user == "n" or user == 'N' in words:
        print('\nok\n')
        print('would you like to create a new data?(y/n)\n')
        user = input('\ntype here: ')

        if user == "y" or user == 'Y' in words:
            print('ok\n')
            pass
        elif user == 'n' or user == 'N' in words:
            print('ok')
            continue
        elif user == "":
            continue
        elif user not in words:
            print(f'{user} is not in the list of commands')
            continue
        elif user == 'q' or user == 'Q' in words:
            print('quiting...')
            break


    elif user == "":
        continue
    elif user not in words:
        print(f'{user} is not in the list of commands')
        continue
    elif user == 'c' or user == 'C' in words:
        print('creating space for you to type your new number data...')
        print('success\n')
        pass
    elif user == 'q' or user == 'Q' in words:
        print('quiting...')
        break
    ### directions ends here ###

    while True:
        ###SECOND WHILE LOOP STARTS HERE###
        #second main code#
        #this while loop is where magic happens, this while loop it's like the center of everything
        print('you can start typing your number data')

        #on this part we use "map" to split the numbers into intigers and float numbers

        #starts here
        try:
            number = input('type here: ')
            num_slp = number.split()
            slp_map = map(float,num_slp)
            list_object = list(slp_map)
            data_list = i.info(list_object)
        except:
            print(f"{number} is not a intigers or a float number")
            continue
        #ends here

        #this are intructions (again) to save, print, or quit.
        print('would you like print the information?(y/n)')
        ###SECONDARY DIRECTIONS START HERE###
        user = input('\ntype here: ')
        if user == 'y' or user == 'Y' in words:
            print('\nprinting the information...\n ')
            print(data_list)
            print('\nsuccess!')
            print('\nwould you like to save the number data?')
            ##########################################################
            user = input('\ntype here: ')
            if user == 'y' or user == 'Y' in words:
                i.store(list_object)
                print('the number data is saved.')
                break

            elif user == 'n' or user == 'N' in words:
                print('ok')
                break

            elif user not in words:
                print(f'{user} is not in the list of commands')
                continue
            ############################################################

        elif user not in words:
            print(f'{user} is not in the list of commands')
            continue

        elif user == "n" or user == 'N' in words:
            print('ok')
            print('\nwould you like to save the number data?')
        ###SECONDARY DIRECTIONS ENDS HERE###
            #####################################################
            user = input('\ntype here: ')
            if user == 'y' or user == 'Y' in words:
                i.store(list_object)
                print('the number data is saved.')
                break
            elif user == 'n' or user == 'N' in words:
                print('ok')
                break
            elif user not in words:
               print(f'{user} is not in the list of commands')
               continue
            #######################################################
        ###SECOND WHILE LOOP ENDS HERE###