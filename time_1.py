class time:
    """The time class stores general information about a time.
    """    
    def __init__(self, hour: int, minute: int, second: int):
        """Constructs a time object having the specified hour, minute, and second, 
        and universal time in the format HH:MM:SS.

        :ivar __hour: hour of this time object
        :ivar __minute: minute of this time object
        :ivar __second: second of this time object
        :ivar __time: universal time of this time object in the format HH:MM:SS

        Args:
            hour (int): specified hour
            minute (int): specified minute
            second (int): specified second

        Raises:
            ValueError: indicates specified hour is less than 0 or greater than 24
            ValueError: indicates specified minute is less than 0 or greater than 60
            ValueError: indicates specified second is less than 0 or greater than 60
        """        

        
        try:
            if hour < 0 or hour > 24:
                raise ValueError("specified hour is less than 0 or greater than 24")
            elif minute < 0 or minute > 60:
                raise ValueError("specified minute is less than 0 or greater than 60")
            elif second < 0 or second > 60:
                raise ValueError("specified second is less than 0 or greater than 60")

        finally:
            self.hour = hour
            self.minute = minute   
            self.second = second    


    def getHour(self):
        """Returns the hour of the calling time object.

        Returns:
            int: hour of the calling time object
        """ 
        return self.hour
    
    def setHour(self, hour: int):
        """Sets the hour of the calling time object to the specified hour and
        recomputes the universal time of the calling time object.

        Args:
            hour (int): specified hour

        Raises:
            ValueError: indicates specified hour is less than 0 or greater than 24
        """        
        self.hour = hour

    def getMinute(self):
        """Returns the minute of the calling time object.

        Returns:
            int: minute of the calling time object
        """ 
        return self.minute
    
    def setMinute(self, minute: int):
        """Sets the minute of the calling time object to the specified minute and
        recomputes the universal time of the calling time object.

        Args:
            minute (int): specified minute

        Raises:
            ValueError: indicates specified minute is less than 0 or greater than 60
        """
        self.minute = minute

    def getSecond(self):
        """Returns the second of the calling time object.

        Returns:
            int: second of the calling time object
        """
        return self.second
    
    def setSecond(self, second: int):
        """Sets the second of the calling time object to the specified second and
        recomputes the universal time of the calling time object.

        Args:
            second (int): specified second

        Raises:
            ValueError: indicates specified second is less than 0 or greater than 60
        """
        self.second = second

    def getTime(self):
        """Returns the universal time of the calling time object.

        Returns:
            str: universal time of the calling time object
        """
        return f"{self.hour}:{self.minute}:{self.second}"
    
    def __str__(self):
        """Returns string representation of the calling time object.

        Returns:
            str: string representation of the calling time object
        """       
        return f"second={self.second}minute={self.minute}hour={self.hour}"
    
    def __eq__(self, other):
        """Tests if the calling time object is equal to the specified object.

        Args:
            other: the specified object

        Returns:
            Boolean: True if the calling time object is equal to the specified
            object, else False
        """
        if isinstance(other, time):
            if self.second == other.second and self.minute == other.minute and self.hour == other.hour:
                return True
            else:   
                return False
        else: 
            return False
    
    @staticmethod
    def sort(data, first: int, last: int):
        """Sorts a list from smallest to largest using the insertion sort
        algorithm bypassing the elements to the left of first and to the
        right of last.

        Args:
            data: list to sort
            first (int): list index at which the sort will begin
            last (int): list index at which the sort will end
        """     
        for i in range(first + 1, last + 1):
            key_item = data[i]
            j = i - 1
            while j >= first and key_item < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key_item



    @staticmethod
    def search (a, first: int, last: int, target: int):
        """Searches part of a sorted list for a specified target starting at a[first]
        and ending at a[last].

        Args:
            a (list): the list to search
            first (string): the list index at which the search will start
            last (string): the list index at which the search will end
            target (string): the element to search for

        Returns:
            int: If target appears in the list, index of the, element 
            that contains target; else -1.
        """
        while first <= last:
            mid = (first + last) // 2
            if a[mid] == target:
                return mid
            elif a[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
        return -1
        
