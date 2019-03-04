from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

chromedriver_path = '/Users/jeffrosal1/Desktop/instabot/chromedriver' # Change this to your own chromedriver path!
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

hashtag_list = ['philippines','skating', 'lenscaptureofficial', 'nature', 'love', 'canon', 'travel', 'moodygrams', 'nikon', 'picoftheday', 'mypixeldiary', 'landscape', 'portrait', 'instagram', 'instagood', 'like4like','likeforlikes','likeforfollow','likeforlikeback', 'like4likes', 'likes4like', 'agameoftones', 'streetphotography', 'picture', 'photooftheday', 'art', 'photography', 'drawing', 'illustration', 'sketch', 'fashion', 'photo', 'design', 'artist', 'tattoo', 'color', 'colorful', 'painting', 'graffiti', 'doodle', 'watercolor', 'digitalart','filipino', 'graphicdesign', 'contemporaryart', 'abstract', 'comics', 'sculpture', 'logo', '3d', 'neon', 'animation', 'surrealism', 'glitch', 'beautiful', 'picoftheday', 'nature', 'travel', 'model', 'blackandwhite', 'love', 'food', 'instagood', 'games', 'installation', 'expressionism','filipina', 'minimalism', 'scooter', 'skate', 'explorepage', 'explore', 'viral', 'meme', 'explorepage', 'sports', 'snowboard', 'noexcuses', 'sport', 'mychicagopix','filipinophotographer', 'chicagogram','northwestern','yale', 'chicagojpg', 'photoshoot', 'losangeles', 'ootd', 'Style', 'InstaFashion', 'FashionBlogger', 'Fashionista', 'Luxuryliving', 'Stylish','pinay', 'LuxuryStyle', 'WomensFashion', 'InstaStyle', 'FashionGram', 'WhatIWore', 'FashionDiaries', 'StyleInspo', 'StyleInspiration', 'LookBook', 'WIWT', 'Chanel', 'FashionStyle', 'StyleBlog', 'Blog', 'StyleBlogger', 'StreetFashion', 'Louboutin', 'OutfitOfTheDay', 'BusinessAttire', 'LosAngeles', 'Chic', 'artofchi','pinoy', 'likechicago', 'chishooters', 'moodygrams', 'agameof10k', 'streetactivity', 'bwp028', 'way2ill', 'bnw_rose', 'streets_vision5k', 'all2epic', 'ig_color', 'visualambassadors', 'gramslayers', 'Shotzdelight', 'UrbanRomantix', 'creativeoptic', 'eclectic_shotz', 'meistershots', 'nikon', 'insta_chicago', 'killaframez', 'pr0ject_uno', 'streetclassics', 'ourcolourdays', 'visualambassadors', 'heatercentral', 'thelensbible', 'theimaged', 'enter_imagination', 'folkcreative', 'instamagazine_', 'creativesontherise', 'ourmoodydays', 'creativeoptic', 'folkvibe', 'visualseduction', 'shotzdelight', 'ig_color', 'food', 'yoga', 'yogaposes', 'beach', 'baseball', 'football', 'soccer', 'singularity', 'robots', 'follows', 'followforfollowback', 'likes', 'gamer', 'gamers', 'NewYork', 'skaters', 'skateboarders', 'artwork','Fashionista','beautiful','beauty','woman','female','feminist','mothernature','mother','nyc', 'NewYorkCity', 'illinois', 'california', 'la', 'austin', 'texas', 'miami', 'florida', 'photo', 'clothes', 'oakland', 'minimalist', 'cars', 'sportscars', 'importcars', 'travel', 'stars', 'photography', 'drawing', 'illustration', 'sketch', 'fashion', 'photo', 'design', 'artist', 'tattoo', 'color', 'colorful', 'painting', 'graffiti', 'doodle', 'watercolor', 'digitalart', 'graphicdesign', 'contemporaryart', 'abstract', 'comics', 'sculpture', 'logo', '3d', 'neon', 'animation', 'vaporwave', 'surrealism', 'glitch', 'beautiful', 'picoftheday', 'nature', 'travel', 'model', 'blackandwhite', 'love', 'food', 'instagood', 'games', 'installation', 'expressionism', 'minimalism', 'scooter', 'skate', 'explorepage', 'explore', 'viral', 'meme', 'explorepage', 'sports', 'surfing', 'snowboard', 'noexcuses', 'sport', 'chicity', 'midwestmoment', 'instagram312', 'lifeofchicago', 'night', 'nightphotography', 'sunsets', 'iphone', 'yogapants', 'nike', 'photoshoot', 'losangeles', 'ootd', 'Style', 'InstaFashion', 'FashionBlogger', 'Fashionista', 'Luxuryliving', 'Stylish', 'LuxuryStyle', 'WomensFashion', 'InstaStyle', 'FashionGram', 'WhatIWore', 'FashionDiaries', 'StyleInspo', 'StyleInspiration', 'LookBook', 'WIWT', 'Chanel', 'FashionStyle', 'StyleBlog', 'Blog', 'StyleBlogger', 'StreetFashion', 'Louboutin', 'OutfitOfTheDay', 'BusinessAttire', 'LosAngeles', 'Chic', 'artofchi', 'likechicago', 'chishooters', 'moodygrams', 'agameof10k', 'streetactivity', 'bwp028', 'way2ill', 'bnw_rose', 'streets_vision5k', 'all2epic', 'ig_color', 'visualambassadors', 'gramslayers', 'Shotzdelight', 'UrbanRomantix', 'creativeoptic', 'eclectic_shotz', 'meistershots', 'nikon', 'insta_chicago', 'killaframez', 'pr0ject_uno', 'streetclassics', 'ourcolourdays', 'visualambassadors', 'heatercentral', 'thelensbible', 'theimaged', 'enter_imagination', 'folkcreative', 'instamagazine_', 'creativesontherise', 'ourmoodydays', 'creativeoptic', 'folkvibe', 'visualseduction', 'shotzdelight', 'ig_color', 'food', 'yoga', 'yogaposes', 'fit', 'fitclub', 'beach', 'baseball', 'football','cooking','singularity', 'robots', 'follows', 'followforfollowback', 'likes', 'gamer', 'gamers', 'NewYork', 'nyc', 'NewYorkCity', 'illinois', 'california', 'la', 'austin', 'texas', 'miami', 'florida', 'photo', 'clothes', 'oakland', 'minimalist', 'cars', 'sportscars', 'importcars', 'travel', 'ocean', 'artist', 'dtla', 'hollywood', 'dogs', 'cats','foodie', 'tech','technology','hiphop', 'influencer', 'guitar', 'synth','music', 'creative','creativity','photoshop' ,'chicago', 'chicagophotography', 'photography', 'skateboard', 'art', 'minimalism', 'skateboardingisfun', 'skating', 'lenscaptureofficial', 'nature', 'love', 'canon', 'travel', 'moodygrams', 'nikon', 'picoftheday', 'mypixeldiary', 'landscape', 'portrait', 'instagram', 'instagood', 'like4like', 'agameoftones', 'streetphotography', 'picture', 'photooftheday', 'art', 'advertising','brandidentity','branded','brandname','brands','brandrep','branding','brandrepsearch','brand','brandambassador','realty','homes','houses','designer','rap','rapper','biology','science','engineer','engineering','rockmusic', 'ocean', 'artist', 'dtla', 'hollywood', 'dogs', 'cats','foodie', 'tech','technology','hiphop', 'influencer', 'guitar', 'synth', 'music', 'creative','creativity','photoshop' ,'chicago', 'chicagophotography', 'photography', 'skateboard', 'art', 'minimalism', 'vaporwave' ]

prev_user_list = [] #- if it's the first time you run it, use this line and comment the two below
#prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
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
    sleep(randint(3,5))
    print(likes)

    
