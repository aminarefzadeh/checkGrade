#
#    <driver> or <element> .find_element_by_id
#                           find_element_by_name
#                           find_element_by_xpath
#                           find_element_by_link_text
#                           find_element_by_partial_link_text
#                           find_element_by_tag_name
#                           find_element_by_class_name
#                           find_element_by_css_selector
#
# for element we can add '.' in first of xpath to find inner element
# in xpath / means emmidate child but // means deep child
# * means all element fg. "html/*"

#this function can use with "elements" instead "element" to return list

#<element>.get_attribute("title")
#<element>.text
 
#switch_to_frame(id or name or index or element)
#switch_to_default_content()    #to return to main page

#there is same function to switch window and popup window



import time
import threading
import getpass

alarm_thread_object = None

def alarm():
	class alarm_thread():
		def __init__(self):
			import pyglet
			self.pyglet = pyglet	
			def play_alarm():
				player = pyglet.media.Player()
				for i in range(0,20):		
					sound = pyglet.media.load('/home/amin/Desktop/Entekhab/Test.ogg')	
					player.queue(sound)
				player.play()
				pyglet.app.run()

			music = threading.Thread(target=play_alarm)
			music.daemon = True
			self.music = music
		def start(self):
			self.music.start()
		def stop(self):
			self.pyglet.app.exit()

	def func():
		music = alarm_thread()
		music.start()
		time.sleep(45)
		music.stop()

	global alarm_thread_object

	if alarm_thread_object == None or not alarm_thread_object.is_alive() :
		alarm_thread_object = threading.Thread(target=func)
		alarm_thread_object.daemon = True
		alarm_thread_object.start()
	

#course_list format ==>  {'course code':[(course num,Boolean)]),}
# False is for alarm when some course gonna be full
# True is alarm when course is empty 

def Bot(username,password,term):
	from selenium import webdriver
	driver=webdriver.Firefox()
	baseurl="https://auth4.ut.ac.ir:8443/cas/login?service=https://ems1.ut.ac.ir/forms/casauthenticateuser/casmu.aspx?ut=1%26CSURL=https://auth4.ut.ac.ir:8443/cas/logout?service$https://ems.ut.ac.ir/"
	driver.get(baseurl)
	#sleeping
	time.sleep(15)
	driver.find_element_by_xpath('//*[@id="usename-field"]').send_keys(username)
	driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
	driver.find_element_by_xpath('//*[@id="login-btn"]').click()
	#we login to ems :))
	time.sleep(30)
	print("hhhhh");
	frame=driver.find_element_by_xpath('//*[@id="Faci2"]')
	driver.switch_to_frame(frame)
	frame=driver.find_element_by_xpath('/html/frameset/frameset/frame[2]')
	driver.switch_to_frame(frame)
	frame=driver.find_element_by_xpath('/html/frameset/frame[3]')
	driver.switch_to_frame(frame)
	driver.find_element_by_xpath('//*[@id="mendiv"]/table/tbody/tr[5]/td[1]/nobr').click()
	#driver.find_element_by_xpath('//*[@id="mendiv"]/table/tbody/tr[5]/td[1]/nobr').click()
	print("helloooo");
	time.sleep(15)
	driver.switch_to_default_content()
	frame=driver.find_element_by_xpath('//*[@id="Faci3"]')
	driver.switch_to_frame(frame)
	frame=driver.find_element_by_xpath('/html/frameset/frameset/frame[2]')
	driver.switch_to_frame(frame)
	frame=driver.find_element_by_xpath('/html/frameset/frame[3]')
	driver.switch_to_frame(frame)
	driver.find_element_by_xpath('//*[@id="T01"]/tbody/tr[%d]/td[3]'%(term+1)).click()
	time.sleep(15)
	driver.switch_to_default_content()
	frame=driver.find_element_by_xpath('//*[@id="Faci3"]')
	driver.switch_to_frame(frame)
	frame=driver.find_element_by_xpath('/html/frameset/frameset/frame[2]')
	driver.switch_to_frame(frame)
	frame=driver.find_element_by_xpath('/html/frameset/frame[3]')
	driver.switch_to_frame(frame)
	frame=driver.find_element_by_xpath('//*[@id="FrameNewForm"]')
	driver.switch_to_frame(frame)
	l = find_elements_by_xpath('//*[@id="T02"]/tbody/*')
	for i in range(1,len(l)):
		if l[i].find_element_by_xpath('td[9]/nobr').text != "" :
			print(l[i].find_element_by_xpath('td[9]/nobr').text)
			alarm()
	#now we should refresh the page but how ??	
	if (term != 1) :
		driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td[2]/img').click()
		time.sleep(10)
		driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td[1]/img').click()
	else:
		driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td[1]/img').click()
		time.sleep(10)
		driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td[2]/img').click()
	

username = raw_input('please enter you\'re username: ')
password = getpass.getpass('please enter you\'re password: ')
term = int(raw_input('which term ? '))
print 'now we start the process and you can stop it with CNTL + D'

Bot(username,password,term)
