import praw

reddit = praw.Reddit(client_id="****",
    client_secret="****",
    username="****",
    password="****",
    user_agent="****")

changes = 0

while True:
    submission = reddit.submission(id="iiamfv")
    ratio = submission.upvote_ratio
    upvotes = round((ratio*submission.score)/(2*ratio-1)) if ratio != 0.5 else round(submission.score/2)
    downvotes = ups-submission.score
    edited = str(upvotes)+' upvotes,'+'\n\n'+str(downvotes)+' downvotes,'+ \n\n"+"and "+str(submission.num_comments)+' comments!'+'\n\n'+'Credit to u/Krukerfluk'+'\n\n'+'Source Code: '
    submission.edit(edited)
    changes += 1
    print(f"Changed {changes} times!")
