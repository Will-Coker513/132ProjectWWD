
import smtplib

smtpUser = input("What's your email")
smtpPass = input("What is your password") 

toAdd = input("What email do you want to send to?")
fromAdd = smtpUser

subject = "Python Test"
header = "To: " + toAdd + "\n" + "From: " + fromAdd + "\n" + "Subject: " + subject
body = "From within a python script"

print header + "\n" + body

s = smtplib.SMTP("smtp.gmail.com",587)

s.ehlo()
s.starttls()

s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, header + "\n\n" + body)

s.quit()
