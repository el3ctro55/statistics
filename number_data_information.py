import numpy as num
import json
import statistics as stat

#####CLASS START HERE#####
class Storage_r:
    

    def store(self,object):
        """this function dump the number data information"""
        filename = 'storage_Room.json'
        with open(filename, 'w') as f:
            stored = json.dump(object,f)

    def load(self):
        """this function load the data dumped in the json file"""
        filename = 'storage_Room.json'
        with open(filename) as f:
           l_data = json.load(f)
           return l_data 


    

#####CLASS ENDS HERE#####

def modes(mode):
    if mode == modesList[0]:
        
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
        a = Data()
        #INTRO & STRUCTIONS#
        print('\n\tThis give you the follwings terms:\n')
        print('Standard Deviation:\nMean:\nMedian:')
        print('\nonly answer with "(y/n)"')
        print('type "c" to create a new data list')
        #ends here#

        words = ['y','Y','n','N','q','Q','c','C']
        while True:
            
            print('type "q" to quit at any moment')
            print('\nwould you like to print your latest saved data information?(y/n)\n')
            
            #this is the main while loop block where you give directions to the computer
            #this whle loop is created for directions

            ### directions start here ###
            user = input('type here: ')

            if user == "y" or user == 'Y' in words:

                stored = a.load()
                print(stored)
                print('would you like to create a new number data?(y/n)\ntype "n" if you want to quit')
                user = input()

                if user == "y" or user == 'Y' in words:
                    print('ok')
                    pass
                elif user == 'n' or user == 'N' in words:
                    print('ok \nquiting...')
                    break

            elif user == "n" or user == 'N' in words:
                print('ok')
                break

            elif user == "":
                continue

            elif user not in words:
                print(f'{user} is not in the list of commands')
                continue

            elif user == 'c' or user == 'C' in words:
                print('\ncreating space for you to type your new number data...')
                print('success!\n')
                pass

            elif user == 'q' or user == 'Q' in words:
                print('quiting...')
                break

            while True:

                ###SECOND WHILE LOOP STARTS HERE###
                #second main code#
                #this while loop is where magic happens, this while loop it's like the center of everything
                print('\nyou can start typing your number data\n')

                #on this part we use "map" to split the numbers into intigers and float numbers

                #starts here
                try:
                    number = input('\ntype here: ')
                    num_slp = number.split()
                    slp_map = map(float,num_slp)
                    list_object = list(slp_map)
                    data_list = a.info(list_object)
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
                    print('\nwould you like to save the number data?(y/n)')
                    ##########################################################
                    user = input('\ntype here: ')
                    if user == 'y' or user == 'Y' in words:
                        a.store(list_object)
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
                    print('\nwould you like to save the number data?(y/n)')
                ###SECONDARY DIRECTIONS ENDS HERE###
                    #####################################################
                    user = input('\ntype here: ')
                    if user == 'y' or user == 'Y' in words:
                        a.store(list_object)
                        print('the number data is saved.')
                        break
                    elif user == 'n' or user == 'N' in words:
                        print('ok')
                        break
                    elif user not in words:
                       print(f'{user} is not in the list of commands')
                       continue
                    elif user == '':
                       continue

    elif mode == modesList[1]:
        print('\ncoming soon\n')
    
    

s = Storage_r()
##########################################################
#the main code starts here.
words = ['y','Y','n','N','q','Q','c','C','m','M','s','S','1','2','3']
modesList = ['statistics','histogram']
modeStorage = {modesList[0]: s.load()}
while True:

    #####################################################################
    print('\n\t### MENU ###\n')
    print('\nselect mode by typing "m" and selecting a mode')
    print('type "q" to quit at any moment\n')
    #####################################################################

    #this is the main while loop block where you give directions to the computer
    #this whle loop is created for directions

    ### directions start here ###
    user = input('\ntype here: ')
     
    if user == "m" or user == 'M' in words:
        print(f'\n\t*** MODES MENU ***\n')
        print(f'\n1. {modesList[0]}\n')
        print(f'\n2. {modesList[1]}\n')
        user = input('\ntype here: ')
        if user == '1':
            print(f'\nselecting {modesList[0]} mode\n')
            modes(modesList[0])
            

        elif user == '2':
            modes(modesList[1])
        elif user == "":
            continue
        elif user not in words:
            print(f'{user} is not in the list of commands')
            continue 

    elif user == "":
        continue
    elif user not in words:
        print(f'{user} is not in the list of commands')
        continue 
    elif user == 'q' or user == 'Q' in words:
        print('quiting...')
        break
    ### directions ends here ###

    