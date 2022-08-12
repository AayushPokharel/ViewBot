import os
import time

from selenium import webdriver
import threading
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_logic():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://www.tiktok.com/@kuitmeet/video/7128724623625162010"
    driver.get(url)
    # Implement your test logic
    time.sleep(500)
    driver.quit()


N = 15   # Number of browsers to spawn
thread_list = list()

# Start test
for i in range(N):
    t = threading.Thread(name='Test {}'.format(i), target=test_logic)
    t.start()
    time.sleep(1)
    print(t.name + ' started!')
    thread_list.append(t)

# Wait for all threads to complete
for thread in thread_list:
    thread.join()

print('Test completed!')
