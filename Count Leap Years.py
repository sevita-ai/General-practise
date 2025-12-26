def count_leap_years(start_year, end_year):
    count = 0
    for year in range (start_year,end_year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            count += 1
    return count
start_year = 2000
end_year = 2040
count = count_leap_years (start_year, end_year)
print(f"The no.of leap years present in between {start_year} and {end_year} are: {count}")
