def main():

    # dictionary used for KV pair functionality
    actors = {
        "Citizen": "An external user of the PHTRS system.\n"
                   "Citizens are able to login to the system and alert the city of potholes",
        "Public Works Employees": "Internal users of the PHTRS system\n"
                                  "Public Works Employees generate work orders based on priority reports"
    }
    use_cases = {"System Login": "Allows users to authenticate to the system\n"
                                 "Separate roles for citizens and citizen employees",
                 "Pothole Alert Form": "Citizen interacts with this form to alert city of potholes",
                 "Damage Report": "Extends functionality of Pothole Alert Form\n"
                                  "Citizens can optionally report damage to their property from the alert form",
                 "Query Pothole Database": "Public Works Employees can query the Pothole Database to view reports",
                 "View Pothole Status": "This is included in Query Pothole Database for internal users\n"
                                        "For external users this is presented as an online CSV report",
                 "Generate Work Order": " Extends functionality of Query Pothole Database\n"
                                        "Public Works employees can generate work orders from query results"
                 }
    # Format and print Actors and Descriptions for actors{}
    print("---ACTORS---")
    for actor, description in actors.items():
        print("Actor: {}\nDescription: {}\n".format(actor, description))
    # Format and print Use Cases and Descriptions for use_cases{}
    print("---USE CASES---")
    for use_case, description in use_cases.items():
        print("Use Case : {}\nDescription: {}\n".format(use_case, description))



if __name__ == "__main__": main()