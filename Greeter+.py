import time;

print ("\n################## Greeter ####################\n")

current_time = time.localtime() # localtime() shows time in a Tuple format
formatted_date = time.strftime("%d-%m-%Y", current_time) # strftime() formats time which are in tuple format. And here localtime() shows time in a Tuple format.
formatted_time = time.strftime("%H:%M:%S", current_time)

# Syntax: strftime(format, time)

print("Date:",formatted_date, end="  ")
print("Time:",formatted_time)


hour = time.strftime("%H", time.localtime()) # Only show hours.
hour = int(hour) # Typecasting to int because strftime() returns the formatted time in string.

if (hour>=6 and hour<12) :
    print("Hey, Good Morning (^ w ^ )");
elif (hour>=12 and hour<18) :
    print("Hey, Good Afternoon (^ w ^) ");
elif (hour>=18 and hour<22) :
    print("Hey, Good Evening ( ^ w ^) ");
else :
    print("Hey, Good Night (z w z )");

