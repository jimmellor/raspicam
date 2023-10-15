from picamera2 import Picamera2
from picamera2.outputs import FfmpegOutput
output = FfmpegOutput("-f hls -hls_time 4 -hls_list_size 5 -hls_flags delete_segments -hls_allow_cache 0 stream.m3u8")