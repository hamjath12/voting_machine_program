import mysql.connector
import datetime
import smtplib


def candidate():
    candidates = {
        "1": {"name": "Vasu", "party": "DMK"},
        "2": {"name": "M.Shanmugam", "party": "ADMK"},
        "3": {"name": "P.Chidambaram", "party": "INC"},
        "4": {"name": "R.Dharmar", "party": "AIADMK"},
        "5": {"name": "Vaiko", "party": "BJP"}
    }
    
    print("---candidate-name-list---")
    for num, details in candidates.items():
        print(f"no:{num} candidate_name: {details['name']} katchi_name:{details['party']}")
        
    user = input("user enter for you vote:")
    if user in candidates:
        candidate_name = candidates[user]['name']
        party = candidates[user]['party']
        times = datetime.datetime.now()
        
        # Log the vote
        with open("vote.txt", "a") as f:
            log_entry = f"your vote for {party}. candidate name is '{candidate_name}' {times}\n"
            f.write(log_entry)
            print(log_entry)
            f.write("your successfully voted\n")
            print("your successfully voted")
        
        # Update the database
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345",
                database="election_db"
            )
            mycursor = mydb.cursor()
            update_sql = "UPDATE candidate SET votes = votes + 1 WHERE candidate_id = %s"
            mycursor.execute(update_sql, (user,))
            mydb.commit()
            print("Vote updated in database successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            mycursor.close()
            mydb.close()

def email_sent():
    try:
        
        user_mail = input("Enter your e-mail: ")
        receiver_mail = "mohammedhamjath12@gmail.com"

        message = "Subject: Vote Confirmation\n\nYour vote has been successfully counted."

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        s.login("mohammedhamjath12@gmail.com", "nlat yfor hpny kxcw")  # Replace with the correct password

        s.sendmail(user_mail, receiver_mail, message)
        s.quit()  

        print("Mail sent successfully")

    except smtplib.SMTPAuthenticationError:
        print("mail not sent !!!")
candidate()
email_sent()









