def create_youtube_video(title, describtion):
	video_dict = {"title": title, "describtion": describtion, "likes": 0, "dislikes": 0, "comments":{} }
	return video_dict

def like(youtube_video): 
	if likes in youtube_video:
		youtube_video["likes"] = youtube_video["likes"] + 1
		return youtube_video

def dislike(youtube_video): 
	if dislikes in create_youtube_video:
		create_youtube_video["dislikes"] = create_youtube_video["dislikes"] + 1
		return create_youtube_video	

def add_comment(youtube_video, username, comment_text):
	youtube_video["comments"][username] = comment_text
	return youtube_video
	

youtube_video = create_youtube_video("new video", "cool video")
print(youtube_video)
like(youtube_video)
dislike(youtube_video)
add_comment(youtube_video, "alisa", "nice video")
print(youtube_video)

for i in range(495):
	like(youtube_video)

