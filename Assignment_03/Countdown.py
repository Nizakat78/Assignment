import time

def countdown_timer(seconds):
    """Function to start a countdown timer."""
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')  
        time.sleep(1) 
        seconds -= 1  
    
    print("00:00")  
    print("Time's up!")  

def main():
    
    minutes = int(input("Enter the time in minutes for countdown: "))
    seconds = minutes * 60  
    print(f"Starting countdown for {minutes} minutes.")
    
    countdown_timer(seconds)

if __name__ == "__main__":
    main()
