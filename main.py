import praw

reddit = praw.Reddit(client_id="****",
    client_secret="****",
    username="****",
    password="****",
    user_agent="****")

changes = 0

while True:
    submission = reddit.submission(id="****")
    ratio = submission.upvote_ratio
    upvotes = round((ratio*submission.score)/(2*ratio-1)) if ratio != 0.5 else round(submission.score/2)
    downvotes = upvotes-submission.score
    edited = str(upvotes) + ' upvotes,' + '\n\n' + str(downvotes) + ' downvotes,' + '\n\n' + 'and ' + str(submission.num_comments) + ' comments!' + '\n\n' + 'Credit to u/Krukerfluk and Tom Scott!' + '\n\n' + 'Code: https://github.com/CalvinMiller190/reddit-post' + '\n\n' + 'This post uses the praw module to get the information about the post, then edits the post every second based on the information that it got!'
    submission.edit(edited)
    changes += 1
    print(f"Changed {changes} times!")
