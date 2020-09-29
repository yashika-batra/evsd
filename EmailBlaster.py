import csv
import smtplib
import ssl

file = input("Enter a file path: ")

# send email
port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    sender_email = "emails.evsd@gmail.com"
    subject = "Registration Forms"
    server.login(sender_email, password)

    # Open and read CSV file, send an email!
    with open(file) as CSVfile:
        readCSV = csv.reader(CSVfile, delimiter=',')
        next(readCSV)
        email1s = []
        email2s = []
        names = []
        comments = []
        for row in readCSV:  # For each entry
            email1 = row[2]  # Change this as necessary
            email1s.append(email1)
            # print(email1) # for testing
            email2 = row[3]  # Change this as necessary
            email2s.append(email2)
            # print(email2) # for testing
            name = row[1]  # Change this as necessary
            names.append(name)
            # print(name) # for testing
            comment = row[5]  # Change this as necessary
            comments.append(comment)
            # print(comment) # for testing

            message = "REGISTRATION FORMS\n" \
                      "Hello {name1}, \n" \
                      "We have received and looked over your registration form! \n" \
                      "Please take note of the following comments! \n\n" \
                      "If necessary, fix your waiver packet, and resubmit your forms to the following " \
                      "link: https://forms.gle/zRGQPJ3YzutEGyou9. \n" \
                      "Comments: {comment1}".format(name1=name, comment1=comment)
            # print(message) # for testing

            server.sendmail(sender_email, email1, message, subject)  # Send to personal email
            server.sendmail(sender_email, email2, message, subject)  # Send to student email
