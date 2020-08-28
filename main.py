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
    edited = f"{str(upvotes)} upvotes,\n\n{str(downvotes)} downvotes,\n\nand {str(submission.num_comments)} comments!\n\nCredit to u/Krukerfluk and Tom Scott!\n\nCode: https://github.com/CalvinMiller190/reddit-post\n\nThis post uses the [praw module](https://praw.readthedocs.io/en/latest/) to get the information about the post, then edits the post every second based on the information that it got!"
    submission.edit(edited)
    changes += 1
    print(f"Changed {changes} times!")
