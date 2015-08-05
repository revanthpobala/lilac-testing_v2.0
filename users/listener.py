#####################################################################################
#listener.py
#Authors: Revanth Pobala and Hussain Mucklai.
#This project is about the Testing of Lilac(Lightweight low latency anonymous chat)
#The listener.py file acts as a listener. It will listen for the connection. 
#It will accept the connection and waits for the message
##When it receives the message it replies back till the connection is disconnected
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
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display


semaphore = [False, None]

class Testing():
    
    
    def __init__(self):
        #display = Display(visible=0, size=(1920, 720))
        #display.start()
        self.username = None
        self.add_text = ""
        self.browser = webdriver.Chrome()
        self.countin = 0
        self.counter = 0
        self.antha = 0
        self.count = 0

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
#@params username : Who performed the action.
 ###################################################################################### 
     
    def open_log_file(self,record,case,username):
        open_file = open('/home/revanth/Projects/workspace/Lilac_Testing/src/users/logs/converlis.log','a')
        if case == 'username':
            to_write = username+" logged at "+record +"\n"
            open_file.write(to_write)
        if case == 'submit':
            to_write = username+" submitted the details at "+record + "\n"  
            open_file.write(to_write)  
        if case == 'message_time':
            to_write = username + "  messaged to " +record +"\n"
            open_file.write(to_write)
        if case == 'received_message':         
            to_write = username + "  received message  at  " +record +"\n"
            open_file.write(to_write)
        if case == 'accepted_connection':
            to_write = username+"  accepted connection at  " +record+"\n" 
            open_file.write(to_write)  
        if case == 'disconnection':
            to_write = "disconnection from the user at  " +record + "\n"
            open_file.write(to_write)

######################################################################################
#Function write_time_logs(self,record,case,username)
#@params record: The time at some action is performed.
#@params case: What action is performed.
#@params username : Who performed.
 ######################################################################################
 
 
 
    def write_time_logs(self,record,case,username):
        
        print case , record, username,"here finak"
        open_listenerfile = open('./logs/listenerlog.txt','a')
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
            username_ele = self.browser.find_element_by_id("username")
            username_ele.send_keys(self.username)
            record = Testing.get_date_time()
            Testing.open_log_file(record, 'username', self.username)
        return self.username

######################################################################################
#Function get_password(self)
#it will login to the site with the random password
######################################################################################
    
    def get_password(self):
        
        password = hashlib.md5(str(Testing.reading_into_array())).hexdigest()
        password_element = self.browser.find_element_by_name("password")
        password_element.send_keys(password)
        


######################################################################################
#Function check_private_ele(self)
#This function will undo the private chat(username will be registered with the presen-
#ce server)
######################################################################################
        
    def check_private_ele(self):
        private_ele = self.browser.find_element_by_xpath('//*[@id="username_form"]/div[2]/div/label/span')
        private_ele.click() 
        #return True

#####################################################################################
#Function click_private_submit
#This function will submit the creds that are being input.
######################################################################################
    
    def click_private_submit(self):

        submit_ele = self.browser.find_element_by_id("usernameButton")
        #print submit_ele.is_displayed(),"printting submitin"
        submit_ele.click() 
        sub_record = Testing.get_date_time()
        Testing.open_log_file(sub_record,'submit', self.username)
        
######################################################################################
#Function accept_connection
#This function will accept the connection once a request appears.
###################################################################################### 
        
    def accept_connection(self):
        
        wait = WebDriverWait(self.browser, 30)
        acceptnewpartner = wait.until(EC.element_to_be_clickable((By.ID,'accept_new_partner')))
        acceptnewpartner.click()

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
        date_return = str(datetime.datetime.now())
        return date_return
 
 
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
#Function check_for_connection
#This function will check for the connection.
######################################################################################

    def check_for_connection(self):
        
        while 1:
            element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "accept_new_partner"))
            )
            chat_input_element = self.browser.find_element_by_id("chat_input")
            check_this = chat_input_element.is_displayed() 
            condition = element.is_displayed()
            if condition or check_this :
                if condition: 
                    element.click()
                    accepted_rec = Testing.get_date_time()
                    Testing.open_log_file(accepted_rec, 'accepted_connection', self.username)
                    Testing.checking_for_msg()
                    return True

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
            prev_time = str(int(check_time)-2)
            #print "prev time" , prev_time
            fut_time = str(int(check_time)+2) 
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
            value2 = Testing.checking_time(2)
            value3  = Testing.checking_time(3)
            value = (value1 or value2  or value3)
            if value == True:
                    record = Testing.get_date_time()
                    Testing.open_log_file(record, 'received_message', self.username)
                    try:
                        
                        Testing.send_message()
                        print "sent the message"
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
                    except RuntimeError:
                        Testing.main()  

            elif value == False:
                if Testing.check_for_smp()== False:
                    print "couldn't find the element so coming here"
                    Testing.check_for_connection()
                    
                elif Testing.check_for_smp()== True:
                    Testing.checking_for_msg()     

            Testing.checking_for_msg()                                                                                          
                                         

                
        else:
            print " Meth decomposed check again !!!!"
            
            Testing.check_for_connection()                                                         
                            
        return  True
    
######################################################################################
#Function send_message
#This function will send the message. The message length is of the range 1 to 140 chars
######################################################################################      

    def send_message(self):
        try:    
            chat_input_element = self.browser.find_element_by_id("chat_input")
            send_message = self.browser.find_element_by_id("sendMessage")
            chat_with_text = self.browser.find_element_by_id("chat_header")
            if chat_with_text.is_displayed():
                chat_with = str(chat_with_text.text).split(':')
                opposite_user = chat_with[1]
                charts = random.randint(1,140)
                random_message = Testing.gen_random_message(charts)
                msg_time = str(time.time())
                chat_input_element.send_keys(random_message)
                time.sleep(2)
                self.count = self.count+1
                send_message.click()
                random_message = hashlib.md5(str(random_message)).hexdigest()
                Testing.write_time_logs(msg_time,"message_sent",random_message)
                msg_time = Testing.get_date_time()
                Testing.open_log_file(msg_time, 'message_time', opposite_user)  
                rand_disc = random.randint(1,4)
                
                if self.count > rand_disc:
                    print "enough of  messaging, i am disconnecting"
                    Testing.disconnect_user()
                    self.count = 0 
                    Testing.check_for_connection()
                    
                
                
                
        except NoSuchElementException:
            Testing.check_for_connection()
        except StaleElementReferenceException:
            Testing.check_for_connection()  
        except ElementNotSelectableException:
            Testing.check_for_connection()
        except ElementNotVisibleException:
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
        except RuntimeError:          
            Testing.main()                                                                                            
 

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
#function retrying
#This function will return True if the element is displayed
######################################################################################

    def retrying(self):

        retry = self.browser.find_element_by_id("username_taken")
        if retry.is_displayed():
            return True
        else:
            return False
 
 
######################################################################################
#function initiator
#This function will enter the credentials to the system.
###################################################################################### 
    
    def initiator(self):
        time.sleep(5)
        try:
            Testing.get_username()
            print "username entered is: \t", self.username
            Testing.get_password()
            #print "entered password"
            Testing.check_private_ele()
            #print "private checkbox selected"
            Testing.click_private_submit()
            print Testing.retrying() , "duplicate "
            while Testing.retrying() == False:
                self.counter = self.counter +1
                print self.counter
                time.sleep(2)
                if self.counter > 4:
                    Testing.main()
                while Testing.retrying() == True:
                    private_ele = self.browser.find_element_by_id('private') 
                    if private_ele.is_selected():
                        Testing.get_password()
                        Testing.get_username()
                        Testing.click_private_submit()  
                        break 
                break                 
            while Testing.retrying() == True:
                private_ele = self.browser.find_element_by_id('private') 
                if private_ele.is_selected():               
                    Testing.get_password()
                    Testing.get_username()
                    Testing.click_private_submit()  
                    break

              
        except NoSuchElementException:
            print "NoSuchElementException"
            Testing.initiator()
        except StaleElementReferenceException:
            print "StaleElementReferenceException"
            Testing.initiator()  
        except ElementNotSelectableException:
            print "ElementNotSelectableException"
            Testing.initiator()
        except ElementNotVisibleException:
            print "ElementNotVisibleException"
            Testing.initiator() 
        except InvalidElementStateException:
            print "InvalidElementStateException"
            Testing.initiator()
        except NoSuchAttributeException:
            print "NoSuchAttributeException"
            Testing.initiator()
        except TimeoutException:
            Testing.initiator()
        except WebDriverException:
            Testing.initiator()         
        except RuntimeError:
            print "Run time error"
            Testing.main()                                                     



    def receive_connection(self):
        Testing.open_browser()
        Testing.initiator()
        Testing.check_for_connection()
        

        
        
             
    def main(self):
        Testing.receive_connection()
        
        
Testing = Testing()
Testing.main()       
        
        
        
        
        
        
        
        
        
        
        