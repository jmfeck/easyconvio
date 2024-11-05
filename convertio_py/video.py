from moviepy.editor import VideoFileClip

def convert_to_mp4(input_path, output_path=None):
    """
    Converts a video file (e.g., AVI, MOV) to MP4 format.
    """
    output_path = output_path or input_path.replace(".avi", ".mp4").replace(".mov", ".mp4")
    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path, codec="libx264")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_to_avi(input_path, output_path=None):
    """
    Converts a video file (e.g., MP4) to AVI format.
    """
    output_path = output_path or input_path.replace(".mp4", ".avi")
    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path, codec="png")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_to_webm(input_path, output_path=None):
    """
    Converts a video file (e.g., MP4) to WEBM format.
    """
    output_path = output_path or input_path.replace(".mp4", ".webm")
    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path, codec="libvpx")
    print(f"Converted {input_path} to {output_path}")
    return output_path