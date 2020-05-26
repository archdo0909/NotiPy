# Notipy

## How to use pyPager's email system
---

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

Send email

    mail.send_email()

## How to use pyPager with Line
---

Get Line Notify Token

1. Access to https://notify-bot.line.me/doc/en/
2. Login with Line Account
3. Go to Mypage
4. Generate Access Token

Set your Line Token in config.py

```python
# Line Token
LINE_API_ID = "{Your Line Account}"
LINE_API_PASSWORD = "{Your Token}"

```

Create Note object :

    my_note = note.NOTE()

Select Line and set messages: 

```python
line = my_note.Line(LINE_API_ID, LINE_API_PASSWORD)

line.message = "Model Training Finished!"
```


