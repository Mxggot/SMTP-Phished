#!/usr/bin/env python3

##################################################################
# Imports
##################################################################
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL as SMTP
import smtplib
import sys
import os
import time

##################################################################
# Colors
##################################################################
colors = {
    "clear": "\033[m",
    "white": "\033[1;30m",
    "red": "\033[1;31m",
    "green": "\033[1;32m",
    "yellow": "\033[1;33m",
    "blue": "\033[1;34m",
    "magenta": "\033[1;35m",
    "cyan": "\033[1;36m",
    "gray": "\033[1;34m",
}
##################################################################
# Classes and Functions
##################################################################
def clear_screen():
    if 'linux' in sys.platform:
        os.system('clear')
    elif 'win' in sys.platform:
        os.system('cls')

def help_message():
    clear_screen()
    print(f'''{colors['green']}

                  _____  _     _     _              _ 
                 |  __ \| |   (_)   | |            | |
                 | |__) | |__  _ ___| |__   ___  __| |  
                 |  ___/| '_ \| / __| '_ \ / _ \/ _` |
                 | |    | | | | \__ \ | | |  __/ (_| |
                 |_|    |_| |_|_|___/_| |_|\___|\__,_|{colors['green']}
                                                             @..@
                                                            (----)
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ( >__< )
                                                           ^^ ~~ ^^{colors['blue']}
                          _    _      _ 
                         | |  | |    | |      
                         | |__| | ___| |_ __  
                         |  __  |/ _ \ | '_ \ 
                         | |  | |  __/ | |_) |
                         |_|  |_|\___|_| .__/ 
                                       | |    
                                       |_|    

           {colors['clear']}            
When utilizing this script, ensure you follow these guidelines for smooth operation:

* Email content should be stored in a {colors['red']}txt{colors['clear']} file and specified with its full path. However, the content must conform to {colors['yellow']}HTML{colors['clear']} standards.

* If you select "Multiple Targets," remember to provide the path to the list of recipients. This list should be stored in a {colors['red']}txt{colors['clear']} file, with email addresses separated by {colors['yellow']}';' (semicolon){colors['clear']}.

* During SMTP server setup, don't forget to include the connection port. For example: {colors['blue']}mail.smtpserver.com{colors['yellow']}:{colors['red']}587{colors['clear']}.
''')

def warning_message():
    clear_screen()
    print(f'''{colors['red']}
       
                   
                  _____  _     _     _              _ 
                 |  __ \| |   (_)   | |            | |
                 | |__) | |__  _ ___| |__   ___  __| |
                 |  ___/| '_ \| / __| '_ \ / _ \/ _` |
                 | |    | | | | \__ \ | | |  __/ (_| |
                 |_|    |_| |_|_|___/_| |_|\___|\__,_|
                 
.______________________________________________________|_._._._._._._._._._.
 \_____________________________________________________|_#_#_#_#_#_#_#_#_#_|
                                                       l                                                   
                            _           _     _   _ 
                      /\   | |         | |   | | | |
                     /  \  | | ___ _ __| |_  | | | |
                    / /\ \ | |/ _ \ '__| __| | | | |
                   / ____ \| |  __/ |  | |_  |_| |_|
                  /_/    \_\_|\___|_|   \__| (_) (_)
                                   

    <><><><><><><><><><><><><><><ALERT!><><><><><><><><><><><><><><><>
    ! This tool is intended solely for educational and awareness     !
    ! purposes about the dangers of phishing. Using this tool in     !
    ! unauthorized environments or for malicious activities is       !
    ! strictly prohibited.                                           !
    !                                                                !
    <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    !                                                                !     
    ! By running this tool, you agree to use it ethically and        !
    ! responsibly. We are not responsible for any misuse or illegal  ! 
    ! use of this tool. Be sure to obtain proper consent before      !
    ! conducting awareness tests.                                    ! 
    <><><><><><><><><><><><><><><ALERT!><><><><><><><><><><><><><><><>

    ''')

    consent = input(f'''{colors['blue']}Do you agree? ({colors['green']}yes{colors['clear']} or{colors['red']} no{colors['blue']})>{colors['clear']}''')

    if consent == 'yes':
        print(f'''{colors['yellow']}Loading...{colors['clear']}''')
        time.sleep(1)
        pass
    else:
        sys.exit()

def main_menu():
    clear_screen()
    print(f'''{colors['green']}                                                             
,-.----.                                                                   
\    /  \    ,---,                          ,---,                          
|   :    \ ,--.' |      ,--,              ,--.' |                    ,---, 
|   |  .\ :|  |  :    ,--.'|              |  |  :                  ,---.'| 
.   :  |: |:  :  :    |  |,      .--.--.  :  :  :                  |   | : 
|   |   \ ::  |  |,--.`--'_     /  /    ' :  |  |,--.   ,---.      |   | | 
|   : .   /|  :  '   |,' ,'|   |  :  /`./ |  :  '   |  /     \   ,--.__| | 
;   | |`-' |  |   /' :'  | |   |  :  ;_   |  |   /' : /    /  | /   ,'   | 
|   | ;    '  :  | | ||  | :    \  \    `.'  :  | | |.    ' / |.   '  /  | 
:   ' |    |  |  ' | :'  : |__   `----.   \  |  ' | :'   ;   /|'   ; |:  | 
:   : :    |  :  :_:,'|  | '.'| /  /`--'  /  :  :_:,''   |  / ||   | '/  ' 
|   | :    |  | ,'    ;  :    ;'--'.     /|  | ,'    |   :    ||   :    :| 
`---'.|    `--''      |  ,   /   `--'---' `--''       \   \  /  \   \  /   
  `---`                ---`-'                          `----'    `----'    
{colors['blue']}
                                      
 _          _____                 _   
| |_ _ _   |     |_ _ ___ ___ ___| |_ 
| . | | |  | | | |_'_| . | . | . |  _|
|___|_  |  |_|_|_|_,_|_  |_  |___|_|  
    |___|            |___|___|        


{colors['cyan']}Link: https://github.com/Mxggot{colors['clear']}

Select from the menu:
    1) Single Target
    2) Multiple Targets
    3) Help{colors['red']}
   99) Exit
''')

def send_email(victim_email, fake_sender, title_email, path_body_email, smtp_server, smtp_login, smtp_password):
    print(f'''{colors['blue']}Sending phishing email to {victim_email}, please wait...{colors['clear']}''')
    try:
        if fake_sender == None:
            fake_sender = victim_email
        else:
            pass

        with open(path_body_email, 'rb') as file:
            file = file.read()
            body_email = file.decode()

        msg = MIMEMultipart()
        msg['Subject'] = title_email
        msg['From'] = fake_sender
        msg['To'] = victim_email

        body_email = MIMEText(body_email, 'html', 'utf-8')
        msg.attach(body_email)

        smtp = smtplib.SMTP(smtp_server)
        smtp.starttls()

        smtp.login(smtp_login, smtp_password)
        smtp.sendmail(smtp_login, victim_email, msg.as_string())
        print(f'''{colors['green']}Phishing email sent successfully to {victim_email}!{colors['clear']}''')
    except:
        print(f'''{colors['red']}Failed to send phishing email to {victim_email}!{colors['clear']}''')

##################################################################
# Main / Principal
##################################################################
if __name__ == "__main__":
    warning_message()

    #####################
    # Main LOOP
    #####################
    while True:
        while True:
            try:
                main_menu()
                entry = int(input(f'''{colors['yellow']}select> {colors['clear']}'''))
                break
            except:
                pass
        while True:
            match entry:
                case 1: # Single Target
                    victim_email = input(f'''{colors['yellow']}victim email> {colors['clear']}''')
                    fake_sender = input(f'''{colors['yellow']}sender email ({colors['red']}fake{colors['yellow']})> {colors['clear']}''')
                    title_email = input(f'''{colors['yellow']}email subject> {colors['clear']}''')
                    path_body_email = input(f'''{colors['yellow']}message path ({colors['red']}.txt{colors['yellow']})> {colors['clear']}''')
                    smtp_server = input(f'''{colors['yellow']}SMTP server ({colors['red']}e.g. mail.server.com:587{colors['cyan']})> {colors['clear']}''')
                    smtp_login = input(f'''{colors['yellow']}SMTP login> {colors['clear']}''')
                    smtp_password = input(f'''{colors['yellow']}SMTP password> {colors['clear']}''')

                    send_email(victim_email, fake_sender, title_email, path_body_email, smtp_server, smtp_login, smtp_password)
                    print(f'''{colors['yellow']}Returning to the main menu in 10 seconds!{colors['clear']}''')
                    time.sleep(10)
                    break
                case 2: # Multiple Targets
                    path_emails = input(f'''{colors['yellow']}email list ({colors['red']}.txt{colors['yellow']})> {colors['clear']}''')

                    with open(path_emails, 'r') as file:
                        file = file.read()
                        emails = file.replace('\n', '').split(';')

                    fake_sender = input(f'''{colors['yellow']}sender email ({colors['red']}fake{colors['yellow']})> {colors['clear']}''')
                    title_email = input(f'''{colors['yellow']}email subject> {colors['clear']}''')
                    path_body_email = input(f'''{colors['yellow']}message path ({colors['red']}.txt{colors['yellow']})> {colors['clear']}''')
                    smtp_server = input(f'''{colors['yellow']}SMTP server ({colors['red']}e.g. mail.server.com:587{colors['yellow']})> {colors['clear']}''')
                    smtp_login = input(f'''{colors['yellow']}SMTP login> {colors['clear']}''')
                    smtp_password = input(f'''{colors['yellow']}SMTP password> {colors['clear']}''')

                    for email in emails:
                        send_email(email, fake_sender, title_email, path_body_email, smtp_server, smtp_login, smtp_password)

                    print(f'''{colors['yellow']}Returning to the main menu in 10 seconds!{colors['clear']}''')
                    time.sleep(10)
                    break

                case 3: # Help
                    while True:
                        help_message()
                        entry = input(f'''{colors['yellow']}Go back to the Main Menu? (yes)> {colors['clear']}''')
                        if entry == 'yes':
                            break
                        else:
                            pass
                    break

                case 99: # Exit
                    print(f'''{colors['clear']}
Leaving already? Aw, now you owe me a coffee! Help keep my coding sessions fueled
by donating. Thank youu! 

>> >> >> {colors['yellow']}https://paypal.me/rainierteoxon7?country.x=PH&locale.x=en_US{colors['clear']} << << <<
''')
                    sys.exit()
