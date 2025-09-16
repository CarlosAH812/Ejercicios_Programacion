seconds = int(input("Enter the time in seconds: "))

if seconds < 600:
    print("The entered seconds are less than 10 minutes.")
    print(f"You need {600 - seconds} more seconds to reach 10 minutes.")
elif seconds > 600:
    print("The entered seconds are greater than 10 minutes.")
    print(f"You exceeded by {seconds - 600} seconds.")
else:
    print("The entered seconds are exactly equal to 10 minutes.")