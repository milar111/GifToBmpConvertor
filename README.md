# GifToBmpConvertor
This repository hosts a simple yet efficient Python script for converting GIF files to BMP format. The script provides a straightforward solution for users looking to convert animated GIFs or single-frame images into the BMP format. With easy-to-follow instructions and minimal dependencies, this tool offers a hassle-free conversion process, making it suitable for both beginners and experienced developers alike. Whether you need to extract individual frames or transform entire animations, this repository provides a reliable solution for your GIF to BMP conversion needs. Additionally, the repository includes sample GIF files for testing the code and examples demonstrating its usage.

The code provided to test the animations is designed for the Pi Pico board. The code can be easily modified and adapted to work with any microcontroller utilizing CircuitPython.(to do so just change the pins)

## Steps

1. **Installing the Library**:
   - Ensure you have Python installed on your system.
   - Install the required library using pip:
     ```
     pip install pillow
     ```

2. **Changing the Output Size**:
   - Open the Python script in a text editor.
   - Locate the section where the output size is defined(line 3).
   - Modify the width and height parameters to the desired size.

3. **Changing the Path to the File**:
   - In the Python script, find the section where the input GIF file path is specified(line 4).
   - Replace the existing file path with the path to your desired input GIF file.

4. **Example**:
   - For demonstration, consider a GIF file named "icons8-running.gif" located in the same directory as the script.
   - Update the file path in the script to "icons8-running.gif".
   - Adjust the output size if necessary.
   - Run the script to convert "icons8-running.gif" to BMP format.
