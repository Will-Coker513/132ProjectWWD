
import smtplib

def Email(message):

    smtpUser = "132raspberrypi@gmail.com"
    smtpPass = "Wc132Rpi8"

    toAdd = "wcc015@latech.edu"
    fromAdd = smtpUser

    subject = "Randomly Generated Code for Lock"
    header = "To: " + toAdd + "\n" + "From: " + fromAdd + "\n" + "Subject: " + subject
    body = str(message)

    print header + "\n" + body

    s = smtplib.SMTP("smtp.gmail.com",587)

    s.ehlo()
    s.starttls()

    s.login(smtpUser, smtpPass)
    s.sendmail(fromAdd, toAdd, header + "\n\n" + body)

    s.quit()
