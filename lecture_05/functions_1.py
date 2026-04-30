
# greet_friend() is the function name
# name is the parameter
# return None
def greet_friend(name):
    print(f"Hi there {name}! How are you? Are you free tonight? Let's have a drink!")

# main() will always be the first function to call.
# call / invoke / execute
# - def means define function
# - main is the function name
# - () is the parameter list. In this case it is empty.
def main():    # always end with :
    print("------------------")
    print("My first function!")
    print("------------------")
    greet_friend("Bee")         # "Bee" is the argument to the function
    greet_friend("Lily")        # "Lily" is the argument to the function
    greet_friend("Ah Tan")
    greet_friend("Ah Ngeow")
    greet_friend("Ahmad")

main()  # call the main() function