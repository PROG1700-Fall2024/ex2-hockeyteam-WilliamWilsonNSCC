# LAB 2 - HOCKEY TEAM
#Write a program that will ask the user to enter the name of a hockey team, how many wins the team has and 
# how many losses #the team has.

#The program should calculate and display a single string output containing the team name, it's win-loss 
# ratio and the win #percentage formatted to 4 decimal places.

#Ex: The Calgary Flames have 10 wins and 5 losses, with a win percentage of 0.6667.

#Purpose/Concepts: Input and output to screen, string concatentation, string formatting, datatype casting, 
# simple math operations

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #obtaining user input for hockey team, wins and losses
    hockeyTeam = input("Enter the name of your favorite team: ");
    wins = input("How many wins do they have? ");
    losses = input("How many games have they lost? ");
    
    #calculating the win/loss ratio 
    winlossRatio = int(wins) / (int(wins) + int(losses));


    #printing the results to the user of their teams wins, losses, and ratio
    print("The {0} have {1} wins and {2} losses with a {3:.4} win precentage.".format(hockeyTeam, wins, losses, winlossRatio));


    # YOUR CODE ENDS HERE

main()