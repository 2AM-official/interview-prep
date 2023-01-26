def count(date, numDays, hoilday):
    if numDays == 0:
        return date
    hoilday = sorted(hoilday)
    # find the first hoilday after the date
    def binary(hoilday, date):
        left, right = 0, len(hoilday)-1
        val = len(hoilday)-1
        while left <= right:
            mid = left+(right-left)//2
            if hoilday[mid] > date:
                right = mid-1
                val = min(val, right)
            elif hoilday[mid] < date:
                left = mid+1
            else:
                return mid
        return val
    startHoilday = binary(hoilday, date)
    weeks = numDays//7
    date += numDays
    date += weeks*2
    endHoilady = binary(hoilday, date)
    return count(date, endHoilady-startHoilday, hoilday)

    