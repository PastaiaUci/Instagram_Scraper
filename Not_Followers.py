# importing libraries/dependancies
from selenium import webdriver
from time import sleep
from password import pw
import subprocess

# creating main class


class InstaBot:

    # deletes all content that exists in the output file
    def cleaner(self):
        my_file = open(
            r"D:\Programe\Python_Stuff\InstaBot\Not_Followers.txt", "r+")
        my_file.truncate(0)
        my_file.close()


# goes to the instagram profile by clicking


    def __init__(self, username, pas):
        self.driver = webdriver.Chrome("D:\Programe\chromedriver")
        self.driver.get("https://instagram.com")
        sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(username)
        sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(pas)
        sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div").click()
        sleep(4)
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[3]/button[2]").click()
        sleep(1)
        self.driver.find_element_by_xpath(
            "//a[contains(@href,'/{}')]".format("pastaiauci")).click()

# creating a list with followers and those you follow
    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div[2]")
        height = 0
        new_height = 1
        while height != new_height:
            height = new_height
            sleep(1)
            # using a js script for scrolling
            new_height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names

# prints in the output file the unfollowers

    def get_unfollowers(self):
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        not_following = [user for user in following if user not in followers]
        my_file = open(
            r"D:\Programe\Python_Stuff\InstaBot\Not_Followers.txt", "r+")
        for not_follower in not_following:
            my_file.write(not_follower)
            my_file.write("\n")

        my_file.close()


# closing the output file

    def closing(self):
        self.driver.close()


#Selenium = InstaBot("pastaiauci", pw)
# Selenium.cleaner()
# Selenium.get_unfollowers()
# Selenium.closing()
# subprocess.call([r'D:\Programe\Python_Stuff\InstaBot\Opener.bat'])
