from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import numpy as np
import pyautogui
import imutils
import cv2

chromedriver_path = '/Users/jeffrosal1/Desktop/instabot/chromedriver' 
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('')
password = webdriver.find_element_by_name('password')
password.send_keys('')

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button')
button_login.click()
sleep(3)

hashtag_list = [ 'FashionGram', 'WhatIWore', 'FashionDiaries', 'StyleInspo', 'StyleInspiration', 'LookBook', 'WIWT', 'Chanel', 'FashionStyle', 'StyleBlog', 'Blog', 'StyleBlogger', 'StreetFashion', 'Louboutin', 'OutfitOfTheDay', 'BusinessAttire', 'LosAngeles', 'Chic', 'artofchi', 'likechicago', 'chishooters', 'moodygrams', 'agameof10k', 'streetactivity', 'bwp028', 'way2ill']

prev_user_list = [] 
#prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2]
#prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(2)
    first_thumbnail = webdriver.find_element_by_xpath('/html/body/span/section/main/article/div[2]/div/div[1]/div[1]/a')
    
    first_thumbnail.click()
    sleep(randint(1,2)) 
    webdriver.find_element_by_xpath('/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[1]/button/span').click()
                    
    likes += 1
    sleep(randint(1,2))

    #screencapture-start
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("in_memory_to_disk.png", image)
    sleep(60)
    #screencapture-end
    
    comm_prob = randint(1,40)
    if webdriver.find_element_by_xpath('/html/body/div[2]/div[2]/div/article/div[2]/section[3]/div/form/textarea'):
       print('yeah')
       webdriver.find_element_by_xpath('/html/body/div[2]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
       comment_box = webdriver.find_element_by_xpath('/html/body/div[2]/div[2]/div/article/div[2]/section[3]/div/form/textarea')

       if comm_prob == 1:
           comment_box.send_keys('super cool yo!')
           sleep(1)
       elif comm_prob == 2:
           comment_box.send_keys('so nice :)')
           sleep(2)
       elif comm_prob == 3:
           comment_box.send_keys('you are loved')
           sleep(1)
       elif comm_prob == 4:
           comment_box.send_keys('nice')
           sleep(3)
       elif comm_prob == 5:
           comment_box.send_keys('sweet')
           sleep(1)
       elif comm_prob == 6:
           comment_box.send_keys('rad')
           sleep(2)
       elif comm_prob == 7:
           comment_box.send_keys('so fyre')
           sleep(1)
       elif comm_prob == 9:
           comment_box.send_keys('you are loved')
           sleep(1)
       elif comm_prob == 10:
           comment_box.send_keys('Bellissimo! :)')
           sleep(2)
       elif comm_prob == 23:
           comment_box.send_keys('Bellissima! :)')
           sleep(2)
       elif comm_prob == 24:
           comment_box.send_keys('believe')
           sleep(2)
       elif comm_prob == 8:
           comment_box.send_keys('cool')
           sleep(3)  
       elif comm_prob == 11:
           comment_box.send_keys('fyre')
           sleep(1)
       elif comm_prob == 12:
           comment_box.send_keys('how?')
           sleep(3)
       elif comm_prob == 13:
           comment_box.send_keys('wow')
           sleep(2)
       elif comm_prob == 14:
           comment_box.send_keys('excellence')
           sleep(1)
       elif comm_prob == 15:
           comment_box.send_keys('that is awesome')
           sleep(4)
       elif comm_prob == 16:
           comment_box.send_keys('how do you do the things you do?')
           sleep(3)
       elif comm_prob == 17:
           comment_box.send_keys("There's always a story. It's all stories, really. The sun coming up every day is a story. Everything's got a story in it. Change the story, change the world")
           sleep(2)
       elif comm_prob == 18:
           comment_box.send_keys('so lit')
           sleep(3)
       elif comm_prob == 19:
           comment_box.send_keys('litty')
           sleep(1)
       elif comm_prob == 20:
           comment_box.send_keys('and the award goes to.....')
           sleep(3)
       elif comm_prob == 21:
           comment_box.send_keys('How sweet the morning air is! See how that one little cloud floats like a pink feather from some gigantic flamingo. Now the red rim of the sun pushes itself over the London cloud-bank. It shines on a good many folk, but on none, I dare bet, who are on a stranger errand than you and I. How small we feel with our petty ambitions and strivings in the presence of the great elemental forces of Nature!')
           sleep(3)
       elif comm_prob == 22:
           comment_box.send_keys('The future belongs to those who believe in the beauty of their dreams.')
           sleep(3)

           
    else:
       print('no')
                        # Enter to post comment
    comment_box.send_keys(Keys.ENTER)
    sleep(randint(5,7))  




#list2
hashtag_list_b = [ 'bnw_rose', 'artistofinstagram' 'streets_vision5k', 'all2epic', 'ig_color', 'visualambassadors', 'gramslayers', 'Shotzdelight', 'UrbanRomantix', 'creativeoptic', 'eclectic_shotz', 'meistershots', 'nikon', 'insta_chicago', 'killaframez', 'pr0ject_uno', 'streetclassics', 'ourcolourdays', 'visualambassadors', 'heatercentral', 'thelensbible', 'theimaged', 'enter_imagination', 'folkcreative', 'instamagazine_', 'creativesontherise', 'ourmoodydays', 'creativeoptic', 'folkvibe', 'visualseduction', 'shotzdelight', 'ig_color', 'food', 'yoga', 'yogaposes', 'beach', 'baseball', 'football', 'soccer', 'singularity', 'robots', 'follows', 'followforfollowback', 'likes', 'gamer', 'gamers', 'NewYork', 'skaters', 'skateboarders', 'artwork','Fashionista','beautiful','beauty','woman','female','feminist','mothernature','mother','nyc', 'NewYorkCity', 'illinois', 'california', 'la', 'austin', 'texas', 'miami', 'florida', 'photo', 'clothes', 'oakland', 'minimalist', 'cars', 'sportscars', 'importcars', 'travel', 'love', 'dance','beaches', 'vacationphotography', 'travelphotography', 'UXdesign', 'datascience', 'vacation', 'ocean', 'artist', 'dtla', 'hollywood', 'dogs', 'cats','foodie', 'chicagophotography', 'tech','technology','hiphop', 'influencer', 'guitar', 'synth','music', 'creative','creativity','photoshop' ,'chicago', 'photography', 'skateboard', 'art', 'minimalism', 'skateboardingisfun', 'skating', 'lenscaptureofficial', 'nature', 'love', 'canon', 'travel', 'moodygrams', 'nikon', 'picoftheday', 'mypixeldiary', 'landscape', 'portrait', 'instagram', 'instagood', 'like4like', 'agameoftones', 'streetphotography', 'picture', 'minimalmovement','yogapants','beautiful','wcw', 'bikini','funny','dslrofficial', 'photooftheday', 'art', 'photography', 'drawing', 'illustration','explorechicago', 'sketch', 'fashion', 'photo', 'design', 'artist', 'tattoo', 'color', 'colorful', 'painting', 'graffiti', 'doodle', 'watercolor', 'digitalart', 'graphicdesign', 'contemporaryart', 'abstract', 'comics', 'sculpture', 'logo', '3d', 'neon', 'animation', 'vaporwave', 'surrealism', 'glitch', 'beautiful', 'picoftheday', 'nature', 'travel', 'model', 'blackandwhite', 'love', 'food', 'instagood', 'games', 'installation', 'expressionism', 'minimalism', 'scooter', 'skate', 'explorepage', 'explore', 'viral', 'chigram', 'meme', 'explorepage', 'sports', 'snowboard', 'skateboardingisfun', 'noexcuses', 'sport', 'mychicagopix', 'chicagogram', 'insta_chicago', 'igerschicago', 'chitecture', 'wu_chicago', 'artofchi', 'flippinchi', 'enjoyillinois', 'chitown', 'windycity', 'illinois', 'likechicago', 'choosechicago', 'chicity_shots', 'chicagojpg', 'chicagoshots', 'chiarchitecture', 'instachicago','loved','bootyfordays','streetwear', 'midwestmoment', 'instagram312', 'lifeofchicago', 'photoshoot', 'losangeles', 'ootd', 'Style', 'InstaFashion', 'FashionBlogger', 'Fashionista', 'Luxuryliving', 'Stylish', 'InstaStyle', 'chicagolife','WomensFashion','LuxuryStyle', 'igchicago', 'sexy', 'thisischicago','instagood', 'chicity']
sleep(60)
prev_user_list = [] 
#prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2]
#prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list_b:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list_b[tag] + '/')
    sleep(2)
    first_thumbnail = webdriver.find_element_by_xpath('/html/body/span/section/main/article/div[2]/div/div[1]/div[1]/a')
    
    first_thumbnail.click()
    sleep(randint(1,2)) 
    webdriver.find_element_by_xpath('/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[1]/button/span').click()
                    
    likes += 1
    sleep(randint(1,2))

    comm_prob = randint(1,40)
    if webdriver.find_element_by_xpath('/html/body/div[2]/div[2]/div/article/div[2]/section[3]/div/form/textarea'):
       print('yeah')
       webdriver.find_element_by_xpath('/html/body/div[2]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
       comment_box = webdriver.find_element_by_xpath('/html/body/div[2]/div[2]/div/article/div[2]/section[3]/div/form/textarea')

       if comm_prob == 1:
           comment_box.send_keys('super cool yo!')
           sleep(1)
       elif comm_prob == 2:
           comment_box.send_keys('so nice :)')
           sleep(2)
       elif comm_prob == 3:
           comment_box.send_keys('you are loved')
           sleep(1)
       elif comm_prob == 4:
           comment_box.send_keys('nice')
           sleep(3)
       elif comm_prob == 5:
           comment_box.send_keys('sweet')
           sleep(1)
       elif comm_prob == 6:
           comment_box.send_keys('rad')
           sleep(2)
       elif comm_prob == 7:
           comment_box.send_keys('so fyre')
           sleep(1)
       elif comm_prob == 9:
           comment_box.send_keys('you are loved')
           sleep(1)
       elif comm_prob == 10:
           comment_box.send_keys('Bellissimo! :)')
           sleep(2)
       elif comm_prob == 23:
           comment_box.send_keys('Bellissima! :)')
           sleep(2)
       elif comm_prob == 24:
           comment_box.send_keys('believe')
           sleep(2)
       elif comm_prob == 8:
           comment_box.send_keys('cool')
           sleep(3)  
       elif comm_prob == 11:
           comment_box.send_keys('fyre')
           sleep(1)
       elif comm_prob == 12:
           comment_box.send_keys('how?')
           sleep(3)
       elif comm_prob == 13:
           comment_box.send_keys('wow')
           sleep(2)
       elif comm_prob == 14:
           comment_box.send_keys('excellence')
           sleep(1)
       elif comm_prob == 15:
           comment_box.send_keys('that is awesome')
           sleep(4)
       elif comm_prob == 16:
           comment_box.send_keys('how do you do the things you do?')
           sleep(3)
       elif comm_prob == 17:
           comment_box.send_keys("There's always a story. It's all stories, really. The sun coming up every day is a story. Everything's got a story in it. Change the story, change the world")
           sleep(2)
       elif comm_prob == 18:
           comment_box.send_keys('so lit')
           sleep(3)
       elif comm_prob == 19:
           comment_box.send_keys('litty')
           sleep(1)
       elif comm_prob == 20:
           comment_box.send_keys('and the award goes to.....')
           sleep(3)
       elif comm_prob == 21:
           comment_box.send_keys('How sweet the morning air is! See how that one little cloud floats like a pink feather from some gigantic flamingo. Now the red rim of the sun pushes itself over the London cloud-bank. It shines on a good many folk, but on none, I dare bet, who are on a stranger errand than you and I. How small we feel with our petty ambitions and strivings in the presence of the great elemental forces of Nature!')
           sleep(3)
       elif comm_prob == 22:
           comment_box.send_keys('The future belongs to those who believe in the beauty of their dreams.')
           sleep(3)

           
    else:
       print('no')
                        # Enter to post comment
    comment_box.send_keys(Keys.ENTER)
    sleep(randint(5,7))   
    
       
              

    
