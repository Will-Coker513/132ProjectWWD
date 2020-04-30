import smtplib

def Email(mess):
    
    server = smtplib.SMTP_SSL('smtp.zoho.com',port=465)

    message = mess

    smtpUser = "willcokeriv@gmail.com"
    smtpPass = "WDBelle091018@157"

    toAdd = str(raw_input("what email do you want to send to"))
    fromAdd = smtpUser

    subject = "Python Test"
    header = "To: " + toAdd + "\n" + "From: " + fromAdd + "\n" + "Subject: " + subject
    body = "{}".format(message)

    print header + "\n" + body

    s = smtplib.SMTP("smtp.gamil.com",port = 587)

    s.ehlo
    s.starttls()
    s.ehlo

    s.login(smtpUser, smtpPass)
    s.sendmail(fromAdd, toAdd, header + "\n\n" + body)

    s.quit()

