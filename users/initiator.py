#####################################################################################
#initiator.py
#Authors: Revanth Pobala and Hussain Mucklai.
#This project is about the Testing of Lilac(Lightweight low latency anonymous chat)
#The initiator.py file acts as a initiator. It will initiate the connection. 
#It will search for a random user name and it will initiate the chat.
#When the connection is accepted by the other user, the listener sends a message
#When it receives the message it replies back.
#It will disconnect when enough messages has been exchanged.
######################################################################################
import os
import random
import hashlib
import time
import string
import datetime
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ErrorInResponseException
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchWindowException
from pyvirtualdisplay import Display


class Testing():
    def __init__(self):
        #display = Display(visible=0, size=(800, 600))
       # display.start()
        self.username = None
        self.add_text = "\n"
        self.browser = webdriver.Chrome()
        self.tried_users = []
        self.count = 0
        self.antha = 0
 
######################################################################################
#Function open_browser
#This function will insert the URL to the browser.
######################################################################################
 
        
    def open_browser(self):
        self.browser.get('http://localhost:8060')
        self.browser.set_window_size(1920, 720)
        
######################################################################################
#Function gen_random_message 
#@params charts: Number of letters to be sent as a message. The message length must be 
#with in 1 to 140 characters
######################################################################################
       
    def gen_random_message(self,charts):
        chars = "".join( [random.choice(string.letters) for i in xrange(charts)]) 
        return chars



######################################################################################
#Function open_log_file(self,record,case,username)
#@params record: The time at some action is performed.
#@params case: What action is performed.
#@params username : Who performed.
 ######################################################################################
    
    def open_log_file(self,record,case,username):
        open_file = open('./logs/conver.log','a')
        if case == 'username':
            to_write = username+" logged at: "+record +"\n"
            open_file.write(to_write) 
        if case == 'submit':
            to_write = username+" submitted the details at: "+record + "\n"  
            open_file.write(to_write)  
        if case == 'adding' :
            to_write = username+" added at: "+record + "\n"  
            open_file.write(to_write) 
        if case == 'selecting':
            open_file.write(self.add_text) 
            to_write = username+" selected for messaging at: "+record + "\n"  
            open_file.write(to_write)                   
        if case == 'message_time':
            to_write = username + "  replied at: " +record +"\n"
            open_file.write(to_write)
        if case == 'received_message':         
            to_write = username + "  received message at:  " +record +"\n"
            open_file.write(to_write)
        if case == 'disconnection':
            to_write = "Disconnection from the user at:  " +record + "\n"
            open_file.write(to_write)
######################################################################################
#Function write_time_logs(self,record,case,username)
#@params record: The time at some action is performed.
#@params case: What action is performed.
#@params username : Who performed the action.
 ######################################################################################
 
 
 
    def write_time_logs(self,record,case,username):
        
        #os.system('touch log'+times[:10]+'.txt')
        print case , record, username,"initiator final"
        open_listenerfile = open('./logs/sentlog.txt','a')
        print "case" ,case
        if case == 'message_sent':
            to_write = username + "," + record+"\n"
            open_listenerfile.write(to_write)        
        if case == 'message_receive':
            to_write = username + ","+record+"\n"
            open_listenerfile.write(to_write)

######################################################################################
#Function reading_into_array(self)
# This function will read the initiators from a file and it returns a random user
#name 
######################################################################################        
    def reading_into_array(self):
        
        users = []
        file_read = open('users.txt','rw')
        for i in file_read.readlines():
            users.append(i)
        rando_num = random.randint(0,(len(users)-1))
        return users[rando_num].strip()
###################################################################################### 
#Function choose_listeners(self)
# This function will read the listeners from a file and it returns a random user
#name
######################################################################################     
            
    def choose_listeners(self):
        users = []
        file_read = open('todefend.txt','rw')
        for i in file_read.readlines():
            users.append(i)
        rando_num = random.randint(0,(len(users)-1))
        return users[rando_num].strip()          
###################################################################################### 
#Function get_username(flag =1)
#@params flag If the flag is set to 1 then it will login to the site with the selected 
#username
######################################################################################             
            
    def get_username(self,flag =1):
        self.username = Testing.reading_into_array().strip()
        self.username = self.username[0:12]
        if flag==1:
            try:
                username_ele = self.browser.find_element_by_id("username")
                username_ele.send_keys(self.username)
                record = Testing.get_date_time()
                Testing.open_log_file(record, 'username', self.username)
            except NoSuchElementException:
                print "reached here"
                Testing.get_password(flag=1)

        return self.username
######################################################################################
#Function get_password(self)
#it will login to the site with the random password
######################################################################################
    
    def get_password(self):
        
        password = hashlib.md5(str(Testing.reading_into_array())).hexdigest()
        password_element = self.browser.find_element_by_id("password")
        password_element.send_keys(password)

######################################################################################
#Function check_private_ele(self)
#This function will undo the private chat(username will be registered with the presen-
#ce server)
######################################################################################

        
    def check_private_ele(self):
        private_ele = self.browser.find_element_by_xpath('//*[@id="username_form"]/div[2]/div/label/span')
        private_ele.click()
        
#####################################################################################
#Function click_private_submit
#This function will submit the creds that are being input
######################################################################################      
        
    def click_private_submit(self):

        submit_ele = self.browser.find_element_by_id("usernameButton")
        submit_ele.click()
        sub_record = Testing.get_date_time()
        Testing.open_log_file(sub_record,'submit', self.username)
    
######################################################################################
#Function find_contacts
#This function will find the contacts 
######################################################################################    
    def find_contacts(self):
        time.sleep(5)
        contacts = []
        file_re = open('todefend.txt','r')
        for user in file_re.readlines():
            user = user[0:12].strip()
            contacts.append(user)
        for row_user in contacts:
            Testing.add_contact(row_user)
        #print contacts ,"All contacts" 
######################################################################################  
#Function add_contact
#This function will add the contact to the contact list
######################################################################################          

    def add_contact(self,row_user):
        print "Adding user", row_user 

        row_user = row_user.strip()
        contact_element = self.browser.find_element_by_id("partner_username")
        contact_element.send_keys(row_user)
        create_contact = self.browser.find_element_by_id("partnerButton")
        create_contact.click()
        add_contact_time = Testing.get_date_time()
        Testing.open_log_file(add_contact_time,'adding', row_user)
        contact_element.clear()
    
######################################################################################  
#Function start_chat
#This function will select the random username and it will initiate the chat
######################################################################################      
    
    def start_chat(self):
        
        try:
            random_username = Testing.choose_listeners().strip()
            random_username = str(random_username[0:12]).strip()
            random_chat_id = self.browser.find_element_by_name(random_username)
            print "chatting with \t",random_username
            if random_chat_id.is_enabled() and random_chat_id.is_displayed():
                random_chat_id.click()
                random_user_sel_time = Testing.get_date_time()
                Testing.open_log_file(random_user_sel_time, 'selecting', random_username)
            else:
                Testing.make_chat()
        except NoSuchElementException:
            print "NoSuchElementException"
            Testing.make_chat()
        except StaleElementReferenceException:
            print "StaleElementReferenceException"
            Testing.make_chat()  
        except ElementNotSelectableException:
            print "ElementNotSelectableException"
            Testing.make_chat()
        except ElementNotVisibleException:
            print "ElementNotVisibleException"
            Testing.initiate_connection()
            self.browser.close()
        except InvalidElementStateException:
            print "InvalidElementStateException"
            Testing.make_chat()
        except NoSuchAttributeException:
            print "NoSuchAttributeException"
            Testing.make_chat()
        except TimeoutException:
            Testing.make_chat()
        except WebDriverException:
            Testing.make_chat()
        except NoSuchWindowException:
            Testing.main()         
                                                
######################################################################################  
#Function start_smp
#This function will initiate the Socialist Millionaire Protocol

######################################################################################      
    
    def start_smp(self):
        
        smp_element = self.browser.find_element_by_id("smpAuthenticateButtonIcon")
        smp_element.click()
        enter_passcode = self.browser.find_element_by_id("passcode")
        enter_passcode.send_keys("Hey this is a Test")
        submit_smp = self.browser.find_element_by_id("smpButton")
        submit_smp.click()
  
######################################################################################  
#Function check_for_smp
#This function will check for the SMP button. If the button is present then it will 
#return True else it will return False.
######################################################################################    
    
    def check_for_smp(self):
            smp_auth_button_verify = self.browser.find_element_by_id("smpAuthenticateButton")
            smp_auth_button = smp_auth_button_verify.is_displayed()
            
            if smp_auth_button:
                return True
            else:
                return False

######################################################################################  
#Function get_time_string
#This function will return the epoch time
######################################################################################      



    def get_time_string(self):
        strtime = str(time.time())
        return strtime

######################################################################################  
#Function get_date_time
#This function will return the date and time in readable format
######################################################################################   
     
    def get_date_time(self):
        return str(datetime.datetime.now())

######################################################################################
#Function disconnect_user
#This function will disconnect the user
######################################################################################  

    def disconnect_user(self):
        end_conn = self.browser.find_element_by_id("endConversation")
        end_conn.click()
        record = Testing.get_date_time()
        Testing.open_log_file(record,'disconnection', self.username)
  
######################################################################################
#Function checking_time
#@param flag: If the flag = 1 then it will return the element for the previous time
#If the flag = 2 then it will return  the element for the current time
#if the flag = 3 then it will return the element for the future time
######################################################################################
        
    def checking_time(self,flag):
        try:
            check_time = str(time.time())
            check_time = check_time[0:9]
            #print check_time ,"cur time"
            prev_time = str(int(check_time)-1)
            #print "prev time" , prev_time
            fut_time = str(int(check_time)+1) 
           # print "future time" ,fut_time  
            if flag == 1:
                samayam = prev_time
            elif flag == 2:
                samayam = check_time
            elif flag == 3:
                samayam = fut_time
            else:
                Testing.check_for_connection()
            print "checking at" , samayam
            ele = self.browser.find_element_by_name(samayam)
            if ele.is_displayed():
                self.antha +=1
                if self.antha == 1:
                    message_receive = hashlib.md5(str(ele.text)).hexdigest()
                    record = Testing.get_time_string()
                    print message_receive
                    Testing.write_time_logs(record, "message_receive", message_receive)
                    self.antha = 0
                    
            print ele.is_displayed() , "first pace",flag
            message_text_ele_ver2 = self.browser.find_element_by_class_name("them")
            if ele.is_displayed() and message_text_ele_ver2.is_displayed():
                return True
            else:
                print "false from checking time"
                return False 

        
        except ReferenceError:
            self.browser.quit()
        except StaleElementReferenceException:
            print "failed 2"
            return False            
        except NoSuchElementException:
            print "failed 1"
            return False 
        except ElementNotSelectableException:
            print "failed 3"
            return False 
        except ElementNotVisibleException:
            print "failed 4"
            return False                         
        except InvalidElementStateException:
            return False 
        except NoSuchAttributeException:
            return False 
        except TimeoutException:
            return False 
        except WebDriverException:
            return False 
        except RuntimeError:
            Testing.main()
######################################################################################
#Function  checking_for_msg
#This function will always check for the message. When a message appears then it will
#reply to the message
######################################################################################
    def checking_for_msg(self):
        
        time.sleep(1)
        if Testing.check_for_smp()== True:
            value1 = Testing.checking_time(1)
            #print "value 1" , value1
            value2 = Testing.checking_time(2)
           # print "value 2", value2
            value3  = Testing.checking_time(3)
           # print "value 3",value3
            value = (value1 or value2  or value3)
            
            
           # print value ," final value"

                
            if value == True:
                    print "message received and replying"
                    record = Testing.get_date_time()
                    Testing.open_log_file(record, 'received_message', self.username)
                    
                    try:
                        
                        Testing.send_message()
                        
                        print "sent message"
                    except NoSuchElementException:
                        Testing.check_for_connection()
                    except StaleElementReferenceException:
                        Testing.check_for_connection()  
                    except ElementNotSelectableException:
                        Testing.check_for_connection()
                    except ElementNotVisibleException:
                        Testing.check_for_connection()  
                    except InvalidElementStateException:
                        Testing.check_for_connection()
                    except NoSuchAttributeException:
                        Testing.check_for_connection()
                    except TimeoutException:
                        Testing.check_for_connection()
                    except WebDriverException:
                        Testing.check_for_connection()
                    except NoSuchWindowException:
                        Testing.main()          
                    except RuntimeError:
                        Testing.main()  

            elif value == False:
                if Testing.check_for_smp()== False:
                    print "couldn't find the element so coming here"
                    Testing.make_chat()
                    
                elif Testing.check_for_smp()== True:
                    Testing.checking_for_msg()                          
                

            Testing.checking_for_msg()                                                                                          
                                         

                
        else:
            print "abort mission and start a new connection"
            
            Testing.start_chat()                                                         
                            
        return  True
    
######################################################################################
#Function send_message
#This function will send the message. It will call the disconnect function after 
#certain messages are exchanged
######################################################################################
     
    
    
    
    def send_message(self):
        try:   
            chat_input_element = self.browser.find_element_by_id("chat_input")
            send_message = self.browser.find_element_by_id("sendMessage")
            chat_with_text = self.browser.find_element_by_id("chat_header")
            chat_with = str(chat_with_text.text).split(':')
            opposite_user = chat_with[1]
            charts = random.randint(1,140)
            random_message = Testing.gen_random_message(charts)
            msg_time = str(time.time())
            chat_input_element.send_keys(random_message)
            print "sending the message :" , random_message 
            time.sleep(2)
            self.count = self.count+1
            send_message.click()
            random_message = hashlib.md5(str(random_message)).hexdigest()
            Testing.write_time_logs(msg_time,"message_sent",random_message)
            msgtime = Testing.get_date_time()
            Testing.open_log_file(msgtime, 'message_time', opposite_user)
            rand_disc = random.randint(1,3)
            if self.count > rand_disc:
                print self.count
                print "enough of  messaging, i am disconnecting"
                Testing.disconnect_user()
                self.count = 0 
                Testing.make_chat()
 
                
                          
        except NoSuchElementException:
            Testing.make_chat()
        except StaleElementReferenceException:
            Testing.make_chat()  
        except ElementNotSelectableException:
            Testing.make_chat()
        except ElementNotVisibleException:
            Testing.make_chat()                              
        except ElementNotVisibleException:
            Testing.make_chat() 
        except InvalidElementStateException:
            Testing.make_chat()
        except NoSuchAttributeException:
            Testing.make_chat()
        except TimeoutException:
            Testing.make_chat()
        except WebDriverException:
            Testing.make_chat()  
        except NoSuchWindowException:
            Testing.main()       
        except RuntimeError:
            Testing.main() 

######################################################################################
#Function make_chat
#This function will initiate the chat. If the connection is not accepted till 30 sec
#it will search for the another user.
######################################################################################                                               

    def make_chat(self):
        counter = 0
        while 1:
            time.sleep(1)
            if Testing.check_for_smp() == False:
                counter = counter +1
                print counter
                if counter > 60 and  Testing.check_for_smp() == False:
                    Testing.start_chat()
                    counter = 0
            elif Testing.check_for_smp()== True:
                Testing.send_message()
                Testing.checking_for_msg()
 

    
        
    def initiate_connection(self):
        Testing.open_browser()
        Testing.initiator()
        Testing.make_chat()
       
    def initiator(self):
        time.sleep(10)
        try:
            Testing.check_private_ele()
            print "private element checked"
            Testing.get_password()
            print "password submitted"
            Testing.get_username()
            print "user name " , self.username
            Testing.click_private_submit()
            print "submitted data"
            Testing.find_contacts()
            
        except NoSuchElementException:
            Testing.initiator()
        except StaleElementReferenceException:
            Testing.initiator()  
        except ElementNotSelectableException:
            Testing.initiator()
        except ElementNotVisibleException:
            Testing.initiator()                             
        except ElementNotVisibleException:
            Testing.initiator() 
        except InvalidElementStateException:
            Testing.initiator()
        except NoSuchAttributeException:
            Testing.initiator()
        except TimeoutException:
            Testing.initiator()
        except WebDriverException:
            Testing.initiator()   
        except NoSuchWindowException:
            Testing.main()
        
        
           
    def main(self):
            Testing.initiate_connection()
    
           
Testing = Testing()

Testing.main()
