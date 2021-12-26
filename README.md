# Tribal Wars bot

The bot was created to save time by automating game functionalities.

## Description

So far bot allows sending troops to scavenge completely automatically. It's gonna calculate the number of troops to be most efficient. Users can choose how many troops will be used and how many will stay in the village. 

## Getting Started

### Dependencies

* Python 3.5+
* Selenium
* Chrome
* Chrome driver which can be found here [here](https://chromedriver.chromium.org/downloads)

### Installing

* Install selenium
```
pip install selenium
```
* Clone repository
* In file main.py in line 11 change path to your_cloned_repo_path/Cache

### Executing program

* In file scavenging.py in line 136 dict staying_troops allows setting how many troops of each type will stay in the village. In line 139 dict choosen_troops allows setting troops that will be sent to scavenging. By setting 0, all troops of a given type will be sent.
* After setting troops amount run file main.py by command:
```
python main.py
```
* On the first run user will have to log in manually. After logging close the browser and run the file once again.
* You can use windows task scheduler to run the script every x minutes. To do that edit in bot.bat your python path in the second line and add a task that will execute bot.bat.

I want you to know that in Tribal Wars you are not allowed to use third-party software. You are using it at your own risk and you might get banned.
