file_out = open("quotes.txt", "w")
# w - write means remove all contents of the file if it exists and put in new contents below
# a - append means to add to existing file
# whether 'a' or 'w', if the file is not found, a new file will be created

file_out.write("I've missed more than 9000 shots in my career.\n"
               "I've lost almost 300 games.\n"
               "26 times, I've been trusted to take the game winning shot and missed.\n"
               "I've failed over and over and over again in my life.\n"
               "And that is why I succeed.\n\n"
               "Michael Jordan\n")

file_out.write("\nit doesn't matter if a cat is black or white,"
               "\nif it catches mice it's a good cat"
               "\n\n"
               "Deng Xiaoping\n")

number = 2
file_out.write(f"{number}")

file_out.close()
