import random
import hashlib
import time
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


semaphore = [False, None]

class Testing():
    
    
    def __init__(self):
        self.username = None
        self.add_text = "-----------------------------------------------------------------\n"
        self.browser = webdriver.Firefox()
        self.countin = 0
        self.counter = 0
        
        
    def open_browser(self):
        self.browser.get('http://localhost:8060')
        self.browser.set_window_size(1920, 720)

            
        
        
    def to_sleep(self,time):
        for i in range(0,time):
            time.sleep(1)
    
    def open_log_file(self,record,case,username):
        open_file = open('receivelog.txt','a')
        if case == 'username':
            to_write = username+" logged at "+record +"\n"
            open_file.write(self.add_text)
            open_file.write(to_write) 
            open_file.write(self.add_text)
        if case == 'submsit':
            to_write = username+" submitted the details at "+record + "\n"  
            open_file.write(to_write)  
        if case == 'message_time':
            to_write = username + "  replied at " +record +"\n"
            open_file.write(to_write)
            open_file.write(self.add_text)   
        if case == 'received_message':         
            to_write = username + "  received message  at  " +record +"\n"
            open_file.write(to_write)
            open_file.write(self.add_text)  
        if case == 'accepted_connection':
            to_write = username+"  accepted connection at  " +record+"\n"   
            open_file.write(self.add_text)  
            
        if case == 'disconnection':
            to_write = "  disconnection from the user at  " +record + "\n"
            open_file.write(to_write)
            open_file.write(self.add_text) 
            
            
    def reading_into_array(self):
        
        users = []
        file_read = open('todefend.txt','rw')
        for i in file_read.readlines():
            users.append(i)
        rando_num = random.randint(0,(len(users)-1))
        return users[rando_num].strip()
            
    def get_username(self,flag =1):
        self.username = Testing.reading_into_array().strip()
        self.username = self.username[0:12]
        if flag==1:
            username_ele = self.browser.find_element_by_id("username")
            username_ele.send_keys(self.username)
            record = time.time()
            record = str(record)
            Testing.open_log_file(record, 'username', self.username)
        return self.username

    
    def get_password(self):
        
        password = hashlib.md5(str(Testing.reading_into_array())).hexdigest()
        password_element = self.browser.find_element_by_id("password")
        password_element.send_keys(password)
        
    def check_private_ele(self):
        private_ele = self.browser.find_element_by_id('private')
        private_ele.click()
        return True
    
    def click_private_submit(self):

        submit_ele = self.browser.find_element_by_id("usernameButton")
        submit_ele.click()
        sub_record = str(time.time())
        Testing.open_log_file(sub_record,'submit', self.username)
        
    def accept_connection(self):
        
        wait = WebDriverWait(self.browser, 30)
        acceptnewpartner = wait.until(EC.element_to_be_clickable((By.ID,'accept_new_partner')))
        acceptnewpartner.click()

    def get_time_string(self):
        strtime = str(time.time())
        return strtime  
    
    def check_for_smp(self):
            smp_auth_button_verify = self.browser.find_element_by_id("smpAuthenticateButton")
            smp_auth_button = smp_auth_button_verify.is_displayed()
            
            if smp_auth_button:
                return True
            else:
                return False


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
                    accepted_rec = Testing.get_time_string()
                    Testing.open_log_file(accepted_rec, 'accepted_connection', self.username)
                    Testing.checking_for_msg()
                    return True
    
    def checking_time(self,flag):
        try:
            check_time = str(time.time())
            check_time = check_time[0:9]
            print check_time ,"cur time"
            prev_time = str(int(check_time)-2)
            print "prev time" , prev_time
            fut_time = str(int(check_time)+2) 
            print "future time" ,fut_time  
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
            print ele.is_displayed() , "first pace",flag
            message_text_ele_ver2 = self.browser.find_element_by_class_name("them")
            if ele.is_displayed() and message_text_ele_ver2.is_displayed():
                return True
            else:
                print "false from checking time"
                return False 


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
        
    
    def setTimer(self, Time):
        global semaphore
        semaphore[0] = True
        semaphore[1] = Time
        
    def isSemaphoreLocked (self, Time):
        global semaphore
        if semaphore[0]:
            if ( int(semaphore[1]) - int(Time) > 30 ):
                print "True by isSemaphoreLocked"
                return True
            else:
                print "True by isSemaphoreLocked"
                Testing.resetTimer()
                return False
        else:
            return False
        
    def resetTimer(self):
        global semaphore
        semaphore = [False, None]
        
    
                
    def checking_for_msg(self):
        
        time.sleep(1)
        if Testing.check_for_smp()== True:
            value1 = Testing.checking_time(1)
            print "value 1" , value1
            value2 = Testing.checking_time(2)
            print "value 2", value2
            value3  = Testing.checking_time(3)
            print "value 3",value3
            value = (value1 or value2  or value3)
            
            
            print value ," final value"

                
            if value == True:
                    print "trueee"
                    record = Testing.get_time_string()
                    Testing.open_log_file(record, 'received_message', self.username)
                    try:

                        Testing.send_message()
                        print "breaking from loop"
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
                print "came here"
                Testing.checking_for_msg() 


            Testing.checking_for_msg()                                                                                          
                                         

                
        else:
            print "outer failed struo"
            
            Testing.check_for_connection()                                                         
                            
        return  True
    
      

    def send_message(self):
        try:    
            chat_input_element = self.browser.find_element_by_id("chat_input")
            send_message = self.browser.find_element_by_id("sendMessage")

            chat_with_text = self.browser.find_element_by_id("chat_header")
            chat_with = str(chat_with_text.text).split(':')
            opposite_user = chat_with[1]
            
            
            
            message_array = ["hey","how are you","hello there","welcome lilac","i am good","what are you doing"]
            random_msg = random.randint(0,len(message_array)-1)
            msg_time = str(time.time())
            chat_input_element.send_keys(message_array[random_msg])
            time.sleep(2)
            send_message.click()
            Testing.open_log_file(msg_time, 'message_time', opposite_user)  
            
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
        
    def disconnect_user(self):
        end_conn = self.browser.find_element_by_id("endConversation")
        end_conn.click()
        record = Testing.get_time_string()
        Testing.open_log_file(record,'disconnection', self.username)

    def retrying(self):

        retry = self.browser.find_element_by_id("username_taken")
        if retry.is_displayed():
            return True
        else:
            return False
    
    def initiator(self):
        time.sleep(5)
        try:
            Testing.check_private_ele()
            Testing.get_password()
            Testing.get_username()


            Testing.click_private_submit()
            
            print Testing.retrying()
            while Testing.retrying() == False:
                self.counter = self.counter +1
                print self.counter  
                print self.username               
                time.sleep(3)
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
        
        
        
        
        
        
        
        
        
        
        