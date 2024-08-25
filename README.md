# Description
This is a super simple script that just allows you to get reminders on your desktop.

## How to use
Move to the repository `desktop-reminders` run `python3 main.py -c <PATH TO CONFIG FILE> ` or just run `python3 main.py` with the default config found in the repo.
To modify the config, just edit the message in the following format:
```
<MESSAGE ID>
  wait: <TIME TO WAIT BETWEEN NOTIFICATIONS>
  message: <THE BODY OF THE NOTIFICATION>
  title: <THE TITLE OF THE NOTIFICATION>
  max-number: <THE MAXIMUM NUMBER OF TIMES THE NOTIFICATION WILL BE POSTED>
```
Additionally, supports extra parameters as supported by [notify-py](https://ms7m.github.io/notify-py/).
