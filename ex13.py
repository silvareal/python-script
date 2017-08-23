
'''
Created on Feb 29, 2016
 
@author: indrajit.n
'''
 
from __future__ import unicode_literals
import youtube_dl


ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['<https://www.youtube.com/watch?v=wOom6ize27o&list=PL385A53B00B8B158E>'])


