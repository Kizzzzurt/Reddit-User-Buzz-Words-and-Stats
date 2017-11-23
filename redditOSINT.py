#get age
#Necessary modules
import praw
import datetime
from collections import Counter
import os

#Reddit instance - From Reddit 'apps'
r = praw.Reddit(client_id='',
                client_secret='',
                password='',
                user_agent='',
                username='')

print( '\x1b[1;31;40m' +
' _____               _       _   _   _        ____     _____   _____   _   _   _______ ' '\n'
'|  __ \             | |     | | (_) | |      / __ \   / ____| |_   _| | \ | | |__   __|' '\n'
'| |__) |   ___    __| |   __| |  _  | |_    | |  | | | (___     | |   |  \| |    | |   ' '\n'
'|  _  /   / _ \  / _` |  / _` | | | | __|   | |  | |  \___ \    | |   | . ` |    | |   ' '\n'
'| | \ \  |  __/ | (_| | | (_| | | | | |_    | |__| |  ____) |  _| |_  | |\  |    | |   ' '\n'
'|_|  \_\  \___|  \__,_|  \__,_| |_|  \__|    \____/  |_____/  |_____| |_| \_|    |_|   ' '\n'
'                                                                                       ' '\n'
    + '\x1b[0m'
    )
print('\x1b[1;31;40m' + 'v0.1' + '\x1b[0m')

#Get Redditor Username
input_username = input('\x1b[1;31;40m' + "Redditor's username: " + '\x1b[0m')
user = r.redditor(input_username)

#Get new comments from Redditor that contain buzzwords
def getnew():
    # Buzzwords
    buzzwords = ['Trump', 'trump', 'Hillary', 'cuck', 'liberal', 'right wing', 'left wing', 'libtard', 'shill',
                 'The_Donald', 'T_D', 'the_donald', 'politics', 'political', 'McGregor', 'Mayweather', 'mcgregor',
                'mayweather', 'antifa', 'anti-fa', 'white', 'black', 'BLM', 'black lives matter', 'white supremacists',
                'trumpster', 'trumpets']

    with open("buzzcomments.txt",'w') as file1:
        file1.write("Posts containing buzzwords for " + str(user) + " " + "out of 1,000 new posts" + "\n"
                    + '------------------------------' + "\n")
        count = 1
        for comment in user.comments.new(limit = 1000):
            if any(buzzword in comment.body for buzzword in buzzwords):
                subreddit = comment.subreddit
                body = comment.body
                score = comment.score
                date_of_post = comment.submission.created
                date_of_post_datetime = datetime.date.fromtimestamp(date_of_post)
                file1.write(str(count) + "." + " " + body + "\n" + "\n" + str(date_of_post_datetime) + "," + " " + "Comment score: " +
                            str(score) + "\n" + str(subreddit) + ", "  + " " + 'https://www.reddit.com' +
                            comment.submission.permalink + "\n" + "\n")
                count = count + 1

#Get all submissions made by Redditor
def submissions():
    with open('submissions.txt', 'w') as file1:
        file1.write("All submissions made by " + str(user) + "\n" + "--------------------------------------" + "\n")
        count = 1
        for submission in user.submissions.top(limit=1000):
            subreddit = submission.subreddit
            title = submission.title
            url = submission.url
            score = submission.score
            date_of_post = submission.created
            date_of_post_datetime = datetime.date.fromtimestamp(date_of_post)
            file1.write(str(count) + ". " + title + "\n" + url + "\n" + "Subreddit: " + str(
                        subreddit) + ", " + "Karma score: " + str(score) + ", " + "Date of post: " +
                        str(date_of_post_datetime) + "\n" + "\n")
            count = count + 1

# Get new comments from Redditor that contain potential locations
def getloc():
    # Locations
    locations = ['America','American','US','Canada','Canadian','England','UK','English','China','Chinese', 'Germany', 'German'
                 'Ireland','Irish','India','Indian','Africa','African','Australia','New Zealand','Mexico','Brazil','France',
                 'French','Italy','Italian','Japanese','Japan','Spanish','Spain','Portugal','Sweden','Norway'
                 'Alabama', 'Alaska', 'Arizona','Arkansas','California', 'Colorado', 'Connecticut', 'Delaware',
                 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
                 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
                 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',
                 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
                  'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia','Washington', 'West Virginia' ,
                 'Wisconsin' , 'Wyoming']

    with open("location.txt", 'w') as file1:
        file1.write("Posts containing potential locations for " + str(user) + " " + "out of 1,000 new posts" + "\n"
                    + '------------------------------' + "\n")
        count = 1
        for comment in user.comments.new(limit=1000):
            if any(location in comment.body for location in locations):
                subreddit = comment.subreddit
                body = comment.body
                score = comment.score
                date_of_post = comment.submission.created
                date_of_post_datetime = datetime.date.fromtimestamp(date_of_post)
                file1.write(str(count) + "." + " " + body + "\n" + "\n" + str(date_of_post_datetime) + "," + " " +
                            "Comment score: " + str(score) + "\n" + str(subreddit) + ", " + " " +
                            'https://www.reddit.com' + comment.submission.permalink + "\n" + "\n")
                count = count + 1

# Get new comments that may divulge age of Redditor
def age():
    # Potential age hits
    ageyears = ['1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985',
                '1986', '1987', '1988', '1989','1990', '1991', '1992', '1993', '1994', '1995', '1996',
                '1997', '1998', '1999', '2000','2001', '2002', '2003', '2004','2005', 'born', '13', '14',
                '15', '16', '17', '18', '19','20', '21', '22', '23', '24','25', '26', '27', '28', '29', '30',
                '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45',
                '80s', '90s', '00s', 'years old']

    with open("age.txt", 'w') as file1:
        file1.write("Posts containing approx. age for " + str(user) + " " + "out of 1,000 new posts" + "\n"
                                + '------------------------------' + "\n")
        count = 1
        for comment in user.comments.new(limit=1000):
            if any(ageyear in comment.body for ageyear in ageyears):
                subreddit = comment.subreddit
                body = comment.body
                score = comment.score
                date_of_post = comment.submission.created
                date_of_post_datetime = datetime.date.fromtimestamp(date_of_post)
                file1.write(str(count) + "." + " " + body + "\n" + "\n" + str(date_of_post_datetime) + "," + " " +
                                "Comment score: " + str(score) + "\n" + str(subreddit) + ", " + " " +
                                'https://www.reddit.com' + comment.submission.permalink + "\n" + "\n")
                count = count + 1

#Get 25 controversial posts from Redditor
def getcont():
    with open("controversial.txt",'w') as file2:
        file2.write("Top 100 most controversial posts for " + str(user) + "\n" + '------------------------------' +
            "\n")
        count = 1
        for comment in user.comments.controversial(limit=100):
            subreddit = comment.subreddit
            body = comment.body
            score = comment.score
            date_of_post = comment.submission.created
            date_of_post_datetime = datetime.date.fromtimestamp(date_of_post)
            file2.write(str(count) + "." + " " + body + "\n" + "\n" + str(date_of_post_datetime) + "," + " " + "Comment score: " +
                        str(score) + "\n" + str(subreddit) + ", " + " " + 'https://www.reddit.com' +
                        comment.submission.permalink + "\n" + "\n")
            count = count + 1

#Get Karma scores for Redditor
def getkarma():
    with open("karmacount.txt", 'w') as file3:
        file3.write("Karma Scores for " + str(user) + " for 1,000 most recent Comments" + '\n' + '--------------------------'
                    + '\n')
        total = 0
        for comment in user.comments.new(limit=1000):
            newnumber = int(comment.score)
            total += newnumber
        file3.write("Total karma Count for Last 1K Comments: " + str(total) + "\n" + "\n")
        karma_by_subreddit = {}
        for comment in user.comments.new(limit=1000):
            subreddit = comment.subreddit.display_name
            karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0) + comment.score)
        for sub,karma in sorted(karma_by_subreddit.items(), key=lambda x: x[1], reverse=True):
            file3.write(sub + ":" + " " + str(karma) + "\n")

#Get word count of 1,000 new comments
def wc():
    with open('commentWC.txt','w') as file1:
        for comment in user.comments.new(limit=1000):
            try:
                file1.write(comment.body + '\n' + '\n')
            except:
                pass

    with open('commentWC.txt','r') as file1, open('wordcount.txt','w') as file2:
        file2.write("Words used by " + str(user) + " in 1,000 most recent Comments" + '\n' + '--------------------------'
                    + '\n')
        wordcount = Counter(file1.read().split())
        for word, count in wordcount.most_common():
            file2.write("{0}: {1}".format(word, count) + "\n")
    os.remove('commentWC.txt')

print('\x1b[1;31;40m' + "RUNNING......." + '\x1b[0m')
#Run defined functions
getnew()
print('\x1b[1;31;40m' + "Buzz word comments - comment.txt complete!" + '\x1b[0m')
submissions()
print('\x1b[1;31;40m' + "Submissions made by user - submissions.txt complete!" + '\x1b[0m')
getloc()
print('\x1b[1;31;40m' + "Potential location comments - location.txt complete!" + '\x1b[0m')
age()
print('\x1b[1;31;40m' + "Potential age comments - age.txt complete!" + '\x1b[0m')
getcont()
print('\x1b[1;31;40m' + "Controversial comments - controversial.txt complete!" + '\x1b[0m')
getkarma()
print('\x1b[1;31;40m' + "Karma Count per Subreddit - karmacount.txt complete!" + '\x1b[0m')
wc()
print('\x1b[1;31;40m' + "Word Count for comments - wordcount.txt complete!" + '\x1b[0m')
print('\x1b[1;31;40m' + "DONE!" + '\x1b[0m')
