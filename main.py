import os
import sys
import whisper
import subprocess

# Load the Whisper model
model = whisper.load_model("base")

def generate_subtitle(video_path, output_path):
    result = model.transcribe(video_path)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

def transcode_video(input_path, output_path, output_format, resolution=None):
    ffmpeg_cmd = ["ffmpeg", "-i", input_path]
    
    if resolution:
        ffmpeg_cmd.extend(["-vf", f"scale=-2:{resolution}"])
    
    ffmpeg_cmd.extend(["-c:v", "libx264", "-preset", "veryfast", "-crf", "28", "-c:a", "copy", output_path])
    subprocess.run(ffmpeg_cmd)

def main():
    if len(sys.argv) < 4:
        print("Usage: python main.py <operation> <input_path> <output_path> [resolution]")
        sys.exit(1)

    operation = sys.argv[1].lower()
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    resolution = sys.argv[4] if len(sys.argv) > 4 else None

    if operation == "subtitle":
        generate_subtitle(input_path, output_path)
        print(f"Subtitle generated successfully at {output_path}")

    elif operation == "transcode":
        transcode_video(input_path, output_path, "mp4", resolution)
        print(f"Video transcoded successfully at {output_path}")

    else:
        print("Invalid operation. Please try again.")

if __name__ == "__main__":
    main()