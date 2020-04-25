import note

if __name__ == "__main__":

    # Email
    my_note = note.NOTE()
    mail = my_note.Email(API_ID = "abc",
                         API_PASSWORD = "123")
    mail.recevier= "tester@gmail.com"
    mail.message = "hello"
    mail.print_all()