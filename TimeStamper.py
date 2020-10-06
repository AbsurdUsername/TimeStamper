import time
from datetime import date

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 


print('___          ___  __  ___             __   ___  __  ')
print(' |  |  |\/| |__  /__`  |   /\   |\/| |__) |__  |__) ')
print(' |  |  |  | |___ .__/  |  /~~\  |  | |    |___ |  \ ')
print('\n')
                                                    


date = date.today()
today = date.strftime("%d_%m_%Y")

subj = input('File name >> ')
namefile = subj + '_' + str(today) + '.txt'

ctrlString = input('Press enter to start >>')
timeStart = time.time()


while (ctrlString != 'stop' and ctrlString != 'Stop' and ctrlString != 'STOP'):
    print('Press enter or any key to timestamp, write \'stop\' to end')
    ctrlString = input('>>')

    if (ctrlString != 'stop' and ctrlString != 'Stop' and ctrlString != 'STOP'):

        timeLap = time.time()
        lap = timeLap - timeStart
        lap = convert(lap)
        print('Timestamp saved: ', lap)

        file = open(namefile, "a")
        file.write('Timestamp: ')
        file.write(str(lap))
        file.write('\n')
        file.close()


timeEnd = time.time()
total = timeEnd - timeStart
total = convert(total)
print('Total time: ', total)

file = open(namefile, "a")
file.write('Total time: ')
file.write(str(total))
file.write('\n')
file.write('\n')
file.close()