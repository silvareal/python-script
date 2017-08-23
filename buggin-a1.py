def get_minutes(seconds):
    """(number) -> number
    minutes is the number of minutes since midnight

    precondition: minutes >=60

    >>>get_minutes(3600)
    0
    >>>get_hours(3700)
    1

    """
    hours = seconds % 3600
    minute = hours // 60
    return minute



def get_seconds(seconds):
    """(number) -> number
    seconds is the number of seconds since midnight

    precondition: seconds >=1

    >>>get_seconds(3600)
    0
    >>>get_seconds(3620)
    20
    
    """
    hours = seconds % 3600
    minute = hours % 60
    seconds = minute
    return seconds

get_seconds(2)
