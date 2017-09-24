#Necessary modules
import praw
import datetime

#Reddit instance - From Reddit 'apps'
r = praw.Reddit(client_id='',
                client_secret='',
                password='',
                user_agent='',
                username='')

#Get Redditor Username
input_username = input("Redditor's username: ")
user = r.redditor(input_username)

#Buzzwords
buzzwords = ['Trump','trump','Hillary','cuck','liberal','right wing','left wing','libtard','shill', 'The_Donald', 'T_D','the_donald'
             , 'politics','political','McGregor','Mayweather','mcgregor','mayweather','antifa','anti-fa','white'
             ,'black','BLM','black lives matter','white supremacists','trumpster','trumpets']

#Get new comments from Redditor that contain buzzwords
def getnew():
    with open("comment.txt",'w') as file1:
        file1.write("Posts containing buzzwords for " + str(user) + " " + "out of 500 new posts" + "\n"
                    + '------------------------------' + "\n")
        count = 1
        for comment in user.comments.new(limit = 500):
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

#Get 25 controversial posts from Redditor
def getcont():
    with open("controversial.txt",'w') as file2:
        file2.write("Top 25 most controversial posts for " + str(user) + "\n" + '------------------------------' +
            "\n")
        count = 1
        for comment in user.comments.controversial(limit=25):
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

#Run defined functions
getnew()
getcont()
getkarma()