def past(h, m, s):
    if not 0 <= h <= 23 or not 0 <= m <= 59 or not 0 <= s <= 59:
        raise ValueError("Invalid time format. Hours must be between 0 and 23, minutes and seconds must be between 0 and 59.")
    
    milliseconds = h * 3600 * 1000 + m * 60 * 1000 + s * 1000
    
    return milliseconds