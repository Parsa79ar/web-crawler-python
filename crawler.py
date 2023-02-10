from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from telegram import Bot
import time, os


# Bot token
bot_token = 'your bot token'

# Group or channel chat id
chat_id = 'chat id'

# Program message details
programs_details = \
"""
Program : {} 
Launch : {} 
Reports : {} 
Bounties (min) : {}
Bounties (avg) : {}
"""


# Return page with url
def get_page(url: str) -> object:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)
    return browser


# Listen for New Content in Hackerone.com (!! Only new programs section !!)
def hackerone_listen_content():
    # Load website
    url = "https://hackerone.com/directory/programs?order_direction=DESC&order_field=launched_at"
    page_content = get_page(url)
    time.sleep(60)

    # Get new programs name from website
    new_programs = []
    programs_table = page_content.find_element(By.CLASS_NAME ,"daisy-table-body")
    tr_tags = programs_table.find_elements(By.TAG_NAME, "tr")
    for tr_tag in tr_tags:
        program_name = tr_tag.find_element(By.CLASS_NAME, "daisy-link").text
        new_programs.append(program_name)
    
    # Save programs in file and compare with new programs
    old_programs_file_path = "./old_programs.txt"
    mode = "r+" if os.path.exists(old_programs_file_path) else "w+"
    old_programs_file = open(old_programs, mode)
    old_programs = [line.strip() for line in old_programs_file]
    for program in new_programs:
        if program not in old_programs:
            for tr_tag in tr_tags:
                td_tags = tr_tag.find_elements(By.TAG_NAME, "td")
                new_program_name = tr_tag.find_element(By.CLASS_NAME, "daisy-link").text
                if new_program_name == program:
                    send_message_with_bot(programs_details.format(new_program_name, td_tags[1].text, td_tags[2].text, td_tags[3].text, td_tags[4].get_attribute("textContent")))
            old_programs_file.write(program + "\n")
    old_programs_file.close()
    send_message_with_bot("Crawler still runing...")


# Send messages with telegram bot
def send_message_with_bot(message: str):
    print(message)
    bot = Bot(bot_token)
    bot.send_message(chat_id, message)


# Run     
hackerone_listen_content()