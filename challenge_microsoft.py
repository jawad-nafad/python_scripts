def main():
    user_input=input("Would you like to continue? ")
    if(user_input=="n") or (user_input=="no") :
        print("Exiting!!")
    elif(user_input=="y" or (user_input=="yes")):
        print("Continuing ... \nComplete!")
    else:
        print("Please try again and respond with yes or no.")
        main()

main()