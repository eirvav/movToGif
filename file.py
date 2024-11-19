from moviepy.editor import VideoFileClip

def convert_mov_to_gif(input_path, output_path):
    # Load the video file
    clip = VideoFileClip(input_path)
    
    # Convert to GIF
    clip.write_gif(output_path, fps=10)  # Adjust fps as needed for GIF quality

# Example usage
if __name__ == "__main__":
    input_mov = "Poison Ivy Blood.mov"      # Replace with your .mov file path
    output_gif = "output.gif"    # Replace with your desired output GIF path
    convert_mov_to_gif(input_mov, output_gif)
