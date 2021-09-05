import sys
random_items = {'numbers': [22,34,55,8,0,102,14,18,21,88],'colors':['black','red','eggplant','yellow','beige','magenta','turquoise','orange','indigo','olive']}

name = " ".join(sys.argv[1:])

print("Hello "+name)
print('Guess a number or a color to win! ')

counter = 0

for line in sys.stdin:
    current_line = line.strip('\n')
    current_line=current_line.lower()

    if 'quit' == current_line:
        break
    elif current_line.isnumeric() is True:
        if int(current_line) in random_items['numbers']:
            print('\n'+'!!!! You Win !!!!')
            break
        else:
            counter = counter + 1
            print('Try Again :('+'\n')
    else:
        if current_line in random_items['colors']:
            print('\n'+'!!!! You Win !!!!')
            break
        else:
            counter = counter + 1
            print('Try Again :('+'\n')
    
    if counter==5:
        sys.exit("You're out of chances. Better Luck next time!")
 
sys.stdout.write('\n'+'Exiting Game....')