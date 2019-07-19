from django.shortcuts import render
from django.templatetags.static import static
import os

# Create your views here.
def index(request):
    video_path = "."+static('friends/videos')
    video_list = []
    for video_dir in os.listdir(video_path):
        video_path_full = video_path+'/'+video_dir
        if os.path.isdir(video_path_full):
            episode = []
            for episode_name in os.listdir(video_path+"/"+video_dir):
                episode_name_full = video_path_full+"/"+episode_name
                if os.path.isfile(episode_name_full):
                    episode_num = episode_name.split('_')
                    episode.append({'name':episode_num[1],'urlpath':'friends/videos/'+video_dir+"/"+episode_name})
                    print("path:"+'friends/videos/'+video_dir+"/"+episode_name)
            video_list.append({'section':video_dir,'episode':episode})
    return render(request,'friends/videos.html',{"video_list":video_list})
