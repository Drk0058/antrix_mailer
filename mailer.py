import smtplib 
import pandas as pd  
#list of email_id to send the mail 
# li = ["dk2k147@gmail.com""divinesh_11813057@nitkkr.ac.in"] 
    
# for dest in li: 
#     s = smtplib.SMTP('smtp.gmail.com', 587) 
#     s.starttls() 
#     s.login("randint99", "randfloat99") 
#     message = "chal gaya python ka program smtp se"
#     s.sendmail("randint99@gmail.com", dest, message) 
#     s.quit() 

data = pd.read_excel("C:\\Users\DELL\Desktop\code\python\\antrix mailer\AstroHunt (Responses) (1).xlsx")
#data = pd.read_excel("C:\\Users\DELL\Desktop\code\python\\antrix mailer\\test.xlsx")
mail_list = []
unames = []
psswrd = []

for x in data.itertuples():
    unames.append(x[3])
    psswrd.append(x[4])
    mail_list.append(str(x[2]))

#print(mail_list)

for (dest,p,u) in zip(mail_list,psswrd,unames): 
    print("mailing to "+str(u))
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("noreply.astrohunt@gmail.com", "antrixroxx@kewll") 
    message = "Astrohunt login details .... [Team Name]- " + str(u) + " [password] -" +str(p)
    #message = "You've successfully  registered for astrohunt, login credentials will be sent soon..."
    s.sendmail("noreply.astrohunt@gmail.com", dest, message) 
    s.quit()
