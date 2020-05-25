import note

if __name__ == "__main__":
    from config import API_ID
    from config import API_PASSWORD
    # Email
    my_note = note.NOTE()
    mail = my_note.Email(API_ID, API_PASSWORD)
    mail.recevier= "receiver_addr@gmail.com"
    #TODO : Intuitive message writing system
    mail.message = "Sending email with python should be very easy. \n setting up the environment is now very easy"
    mail.set_from = "ME"
    mail.set_to = "YOU"
    mail.set_subject = "This is a test"
    mail.send_email()
