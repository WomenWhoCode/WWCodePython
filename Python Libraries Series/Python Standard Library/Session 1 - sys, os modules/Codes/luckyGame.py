import sys
random_items = {'numbers': [22,34,55,8,0,102,14,18,21,88],'colors':['black','red','eggplant','yellow','beige','magenta','turquoise','orange','indigo','olive']}

name = " ".join(sys.argv[1:])

print("Hello "+name)
print('Guess a number or a color to win! ')

for line in sys.stdin:
    current_line = line.strip('\n')

    if 'quit' == current_line:
        break
    if current_line.isnumeric() is True:
        if int(current_line) in random_items['numbers']:
            print('\n'+'!!!! You Win !!!!')
            break
        else:
            print('Try Again :('+'\n')
    else:
        current_line=current_line.lower()
        if current_line in random_items['colors']:
            print('\n'+'!!!! You Win !!!!')
            break
        else:
            print('Try Again :('+'\n')
 
sys.stdout.write('\n'+'Exiting Game....')
