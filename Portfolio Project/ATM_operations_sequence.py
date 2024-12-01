def main ():

    print("\n----------CSC505 Portfolio Project Python Script----------\n")
    print("Here are the sequence of steps for the interaction at the ATM as outlined in the UML diagrams for"
          "the CSC505 portfolio project.\nNote that in this script the object 'Bank Account Management System' "
          "is called 'Bank Server'\n")
    sequence_steps = {1: "ATM User --> ATM:  Inserts card", 2: "ATM --> ATM User: Prompt for PIN",
                      3: "ATM User --> ATM: Input PIN",
                      4: "ATM --> Bank Server: Verify Pin",
                      5: "Bank Server <--> ATM <--> ATM User: PIN VALIDATION CONTROL LOOP ----------------------\n"
                         "if PIN is valid: Request withdrawal amount\n"
                         "else if PIN is invalid and attempts < 3: "
                         "increment attempt counter and prompt user to try again,\n"
                         "else if PIN is invalid and attempt == 3: "
                         "eject card and end transaction.\n"
                        "------------------------------------------------------------------------------------------",
                      6: "ATM User --> ATM: Input withdrawal amount", 7: "ATM --> Bank Server: Submit transaction",
                      8: "Bank Server --> Bank Account: Request Balance",
                      9: "ATM User <-- ATM <-- Bank Server <--> Bank Account: FUND VALIDATION CONTROL LOOP ------\n"
                         "if funds are sufficient : Withdraw funds and release cash \n"
                         "else : Withdrawal failure message, notify customer and print balance\n"
                         "------------------------------------------------------------------------------------------",
                      10: "Bank Server --> Bank Account: Update Balance",
                      11: "ATM User <-- ATM <-- Bank Server <--> Bank Account: ZERO BALANCE CHECK CONTROL LOOP --\n"
                          "if balance > 0: finalize transaction, notify customer, and print remaining balance\n"
                          "else if balance == 0: finalize transaction, "
                          "close account, and notify customer of account closure\n"
                          "------------------------------------------------------------------------------------------",
                      12: "ATM --> ATM User: Eject Card"
                      }

    for key, value in sequence_steps.items():
        print(key, ":", value)
if __name__ == "__main__": main()