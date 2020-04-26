import note

if __name__ == "__main__":

    # Email
    my_note = note.NOTE()
    mail = my_note.Email(API_ID = "YOUR_ID",
                         API_PASSWORD = "YOUR_PASSWORD")
    mail.recevier= "recevier_addr@gmail.com"
    #TODO : Intuitive message writing system
    mail.message = "Sending email with python should be very easy. \n setting up the environment is now very easy"
    mail.set_from = "eddie"
    mail.set_to = "you"
    mail.set_subject = "This is a test"
    mail.send_email()