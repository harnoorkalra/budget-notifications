import time
import pync
import pandas as pd
from datetime import date

salary = float(input("Enter this month's salary: ",))
file = 'budgeting.xlsx'
df = pd.read_excel('/Users/noorkalra/git/budget-notifications/budgeting.xlsx')
df.drop(labels = ['Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7'], axis = 1, inplace= True)
df.drop(labels = [17], axis = 0, inplace= True)
today = date.today()
#print(df)

def Food():
    if df.at[16,'Food'] >= 0.3*salary and df.at[16,'Food'] <= 0.35*salary:
        title = "Too much spent on Food"
        message = "Please stop spending, you're approaching the food limit for this month which is {}".format(round(salary*0.4),1)
        pync.notify(message)
    if df.at[16,'Food'] == 0.4*salary:
        title = "You have reached your limit for food."
        message = "Please stop now, you have reached your food limit for this month. You'll be broke."
        pync.notify(message)
    else:
        title = "You have exceeded the food limit"
        message = "You have spent {} on food this month. You have exceeded limit for the month, STOP SPENDING!!".format(round(df.at[16, 'Food']),1)
        pync.notify(message)

def Bills():
    d = today.day
    if d > 20:
        title = "Bills overdue!"
        message = "Bills were due on the 20th!! Pay them off if you haven't already!!!"
        pync.notify(message)
    if d == 19:
        title = "Bills due tomorrow!"
        message = "Get that money out. Bills are due tomorrow!"
        pync.notify(message)


def misc():
    if df.at[16, 'Misc'] >= salary*0.2 and df.at[16, 'Misc'] <= salary*0.25:
        title = "Approaching the shopping limit!!"
        message = "You have spent {} on miscellaneous purchases this month. Please stop. Your limit for the month is {}".format(round(df.at[16, 'Misc'], salary*0.25),1)
        pync.notify(message)
    if df.at[16, 'Misc'] > salary*0.25:
        title = "Over budget!!"
        message = "You have spent {} more than you were supposed to this month. STOP SPENDING!!!".format(round(df.at[16,'Misc']-(salary*0.25), 1))
        pync.notify(message)

if __name__ == "__main__":
    Food()
    time.sleep(3)
    Bills()
    time.sleep(3)
    misc()

  