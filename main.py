import note

if __name__ == "__main__":

    # Email
    from config import EMAIL_API_ID
    from config import EMAIL_API_PASSWORD

    my_note = note.NOTE()
    mail = my_note.Email(EMAIL_API_ID, EMAIL_API_PASSWORD)
    mail.recevier= "receiver_addr@gmail.com"
    #TODO : Intuitive message writing system
    mail.message = "Sending email with python should be very easy. \n setting up the environment is now very easy"
    mail.set_from = "ME"
    mail.set_to = "YOU"
    mail.set_subject = "This is a test"
    mail.send_email()
    

    # LINE
    from config import LINE_API_ID
    from config import LINE_API_PASSWORD

    my_note = note.NOTE()
    line = my_note.Line(LINE_API_ID, LINE_API_PASSWORD)
    line.message = "Model Training done!" 
    line.image = "~/pic/photo.png"
    line.send_message()


    # TELEGRAM
    from config import TELEGRAM_API_ID
    from config import TELEGRAM_API_PASSWORD

    my_note = note.NOTE()
    tel = my_note.Telegram(TELEGRAM_API_ID, TELEGRAM_API_PASSWORD)
    tel.message = "Model Training Done!"
    #tel.image = "~/pic/photo.png"
    tel.send_message()