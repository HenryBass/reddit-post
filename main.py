import praw

reddit = praw.Reddit(client_id="****",
    client_secret="****",
    username="****",
    password="****",
    user_agent="****")

changes = 15500

while True:
    score = submission.score
    awards = len(submission.all_awardings)
    ratio = submission.upvote_ratio
    upvotes = round((ratio*score)/(2*ratio-1)) if ratio != 0.5 else round(score/2)
    downvotes = upvotes-score
    edited = f"{str(upvotes)} upvotes,\n\n{str(downvotes)} downvotes,\n\n{str(submission.num_comments)} comments, \n\n{score} score,\n\nand {awards} awards!\n\n\n\nEdits: {changes} since Friday, August 28, 2020 at 8:30PM EST.\n\nCredit to u/Krukerfluk and Tom Scott!\n\nCode: https://github.com/CalvinMiller190/reddit-post\n\nThis post uses the [praw module](https://praw.readthedocs.io/en/latest/) to get the information about the post, then edits the post every second based on the information that it got!"
    submission.edit(edited)
    changes += 1
    print(f"Changed {changes} times!")
