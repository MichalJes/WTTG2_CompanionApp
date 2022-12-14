import math
import time
import os
import winsound


def clear(): return os.system('cls')


def time_calc(in_time, a):
    hour = math.floor(in_time/100)
    min = in_time % 100
    min = min+a
    if min > 60:
        min = min % 60
        hour += 1
    if hour > 12:
        hour = hour % 12
    return hour*100+min


def BEEP(iterations):
    while iterations > 0:
        winsound.Beep(2000, 200)
        time.sleep(0.2)
        iterations -= 1


def BEEPlong(iterations):
    while iterations > 0:
        winsound.Beep(2000, 800)
        time.sleep(0.1)
        iterations -= 1


def wait(CountTime):
    while CountTime > 0:
        time.sleep(1)
        print(CountTime)
        CountTime -= 1


def network_calc(ingame_t, network_time):
    end_time = time_calc(ingame_t, network_time)
    if end_time < 1000:
        end_time = str(0)+str(end_time)
    end_time_S = str(end_time)
    print("Start: " + str(ingame_t) + " End: " + end_time_S)
    wait(math.floor(((network_time-2)*60)/2))
    BEEP(2)
    print("! 2 min !")
    print("End time: " + str(end_time))
    wait(120)
    BEEP(3)
    BEEPlong(1)
    print("!!! Disconnect !!!")


def siec(ingame_time, network_number):
    match network_number:
        case 1:
            network_calc(ingame_time, 32)
        case 2:
            network_calc(ingame_time, 16)
        case 3:
            network_calc(ingame_time, 14)
        case 4:
            network_calc(ingame_time, 21)
        case 5:
            network_calc(ingame_time, 10)
        case _:
            print("!!! Error, wrong network !!!")
            time.sleep(2)
            clear()


while True:
    print("________________________________")
    print("1: TPLINK_8907_5G")
    print("2: DDW35363")
    print("3: TC8717T10")
    print("4: doody")
    print("5: FreeWifiNoVirus")
    print("________________________________")
    UserIn = list(map(int, input().split()))
    siec(UserIn[0], UserIn[1])
