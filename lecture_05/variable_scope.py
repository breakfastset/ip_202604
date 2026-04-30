superstar = "BTS"   # Global variable

def find_local_star():
    local_star = "Steven Lim"     # Local variable
    print("Inside find_local_star(): ")
    print(f"    local_star: {local_star}")
    print(f"    superstar: {superstar}")

def main():
    print(f"Global: {superstar}")
    find_local_star()
    # print(f"Local star from find_local_star(): {local_star}: ")
    print("End of program.")

main()

# Global variables are accessible everywhere
# Local variables are accessible only within the function
# Rule of thumb:
# 1. Use as little global variables as possible, if possible NONE
# 2. Use local variables most of the time or all of the time