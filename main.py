from time_1 import *

def main():
    # create a time object named t1 thats hour is 2, minute is 30, and seconds are 5.=
    t1 = time(2,30,.5)
    
    # create a time object named t2 thats hour is 12, minute is 25, and seconds are 42.
    t2 = time(12,25,42)
    
    # create a time object named t3 thats hour is 1, minute is 20, and seconds are 22.
    t3 = time(1,20,22)
    
    # create a time object named t4 thats hour is 11, minute is 45, and seconds are 50.
    t4 = time(11,45,50)
    
    # create a time object named t5 thats hour is 3, minute is 25, and seconds are 25.
    t5 = time(3,25,25)

    # display a string representation of t1
    print(t1)
    
    # display a string representation of t2
    print(t2)
    
    # display a string representation of t3
    print(t3)
    
    # display a string representation of t4
    print(t4)
    
    # display a string representation of t5
    print(t5)

    # display the result of testing if t1 is equal to t5
    print(f'is t1 equal to t5: {t1.__eq__(t5)}')

    # use getter and setter methods to make t1 the same time
    # object as t5

    print(f't1: {t1}')


    t1.setHour(t5.getHour())
    t1.setMinute(t5.getMinute())
    t1.setSecond(t5.getSecond())

    print(f't1: {t1}')
    print(f't5: {t5}')
   
    # display the result of testing if t1 is equal to t5
    print(t1.__eq__(t5))

    # get the times of t1, t2, t3, t4, and t5
    print(f'T1: {t1.getTime()}')
    print(f'T2: {t2.getTime()}')
    print(f'T3: {t3.getTime()}')
    print(f'T4: {t4.getTime()}')
    print(f'T5: {t5.getTime()}')


    # and store them in a list named times

    times = [t1.getTime(),t2.getTime(),t3.getTime(),t4.getTime(),t5.getTime()]

    # display the times list
    print(times)

    # sort the times list starting at index position 1 and ending at index position 3
    time.sort(times, 1, 3)

    # display the times list
    print(f'Sorted Time: {times}')

    # sort the times list starting at index position 0 and ending at index position 4
    time.sort(times, 0, 4)

    # display the times list
    print(f'Sorted Time: {times}')

    # search for t2's time in the times list starting at index position 0 and ending at index 
    # position 4
    print(f't2 is at index: {time.search(times,0,4,t2.getTime())}')


    # search for t3's time in the times list starting at index position 0 and ending at index 
    # position 4
    print(f't3 is at index: {time.search(times, 0, 4, t3.getTime())}')

    # search for t2's time in the times list starting at index position 1 and ending at index 
    # position 3
    print(f't2 is at index starting from index 1 and ending at index 3: {time.search(times, 0, 3, t2.getTime())}')

    # search for t3's time in the times list starting at index position 1 and ending at index 
    # position 3
    print(f't3 is at index starting from index 1 and starting at index 3: {time.search(times, 1, 3, t3.getTime())}')


    # ValueErrors:
    t1.setMinute(99)
    t1.setHour(None)
    t1.setSecond(None)


main()