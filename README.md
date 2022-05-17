# Google Admin Console - Find Duplicate Bulk Import Users

Use this Python script to compare two .csv files for matches

### About this script

When running a bulk import of users, at this time Google Admin Console does not do a check for duplicate email addresses.

What happens then is that if a new user is set up to have the same email address as an existing user, upon uploading the csv, the existing users' name, password, and other mapped data will be overwritten.

To check for duplicates, run this Python script using a .csv file of existing email addresses to get back the potential duplicates.
