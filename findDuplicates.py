import csv

# Set list equal to new email addresses you'd like to check for duplicates
newEmails = ["example1@test.com", "example2@test.com", "example3@test.com"]

# Set a local path to your .csv list of existing email addresses.
pathway = "/existing_users.csv"

with open(pathway, newline='') as f:
    reader = csv.reader(f)
    for row in enumerate(reader):
        # row becomes a tuple with format [i, emailAddress]
        # set current emailAddress to oldEmail variable
        oldEmail = row[1]
        # Save the emailAddress string as its own variable
        oldEmailString = oldEmail[0]
        # run a search for any matches in newEmails list
        for newRow in newEmails:
            if oldEmailString == newRow:
                # Print out matches
                print(newRow)
