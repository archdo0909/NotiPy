# email-to-me

## How to use Email system

Create Note object :

    my_note = note.NOTE()

Select Email :

    mail = my_note.Email(YOUR_EMAIL_ID, YOUR_EMAIL_PASSWORD)

Set recevier's mail address, addressee, sender :

    mail.recevier = "receiver_addr@gmail.com"
    mail.message = MESSAGE
    mail.set_from = ME
    mail.set_to = YOU
    mail.set_subject = SUBJECT


