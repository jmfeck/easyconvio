from pydub import AudioSegment


def convert_to_mp3(input_path, output_path=None):
    audio = AudioSegment.from_file(input_path)
    output_path = output_path or input_path.replace(os.path.splitext(input_path)[1], ".mp3")
    audio.export(output_path, format="mp3")
    return output_path

def convert_to_wav(input_path, output_path=None):
    audio = AudioSegment.from_file(input_path)
    output_path = output_path or input_path.replace(os.path.splitext(input_path)[1], ".wav")
    audio.export(output_path, format="wav")
    return output_path