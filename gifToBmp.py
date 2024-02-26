from PIL import Image

OUTPUT_SIZE = (64, 64)  #specify  the size of output gif animation here.
FILENAME = r"path\\to\\gif_file"

gif = Image.open(FILENAME)
print(f'Size:{gif.size}')
print(f'Frames:{gif.n_frames}')

output = Image.new('1', (OUTPUT_SIZE[0] * gif.n_frames, OUTPUT_SIZE[1]), 0)

output_filename = f'icon{gif.n_frames}_frames.bmp'

for frame in range(gif.n_frames):
    gif.seek(frame)
    extracted_frame = gif.resize(OUTPUT_SIZE).convert('L') 
    threshold = 127  
    extracted_frame = extracted_frame.point(lambda p: p > threshold and 255) 
    position = (OUTPUT_SIZE[0] * frame, 0)
    output.paste(extracted_frame, position)

output.save(output_filename)
