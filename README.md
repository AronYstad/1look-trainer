# 1look-trainer
A simple skewb trainer that lets you practice 1-look patterns with a number of random moves added to the end.

NS scrambles taken from mihlefeld's NS trainer (https://github.com/mihlefeld/Alg-Trainers/tree/master/Skewb-NS2-Trainer).

To use, simply run main.py in a terminal. I made it so the code includes some patterns that I want to practice, but if you want to modify it, change the scrambles in the "cases" array. These are the scrambles for the patterns, which are applied after the NS scrambles.

I put this together very quickly, so suggestions for improvements are welcome.

## Running the trainer (for those who haven't used Python before)
1. Install Python including pip
2. Run "pip install numpy"
3. Download the trainer and go into the folder with main.py
4. Open the terminal/powershell in the folder and run "python main.py"

On Linux, pip might be a bit annoying to deal with, so "apt install python3-numpy" might work instead. Also run the file with "python3 main.py" on Linux if you do not have a virtual environment.
