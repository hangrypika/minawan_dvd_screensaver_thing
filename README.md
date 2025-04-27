You need to have VSCode or something similar installed to make this work.
Open the files in your code editor.
Before running make sure you have the python language installed
if you don't download it from here: https://www.python.org/downloads/
Then go to the terminal (that little tab at the bottom of your screen should say terminal) 
make sure you are in the correct directory
(should be in minawan_dvd_screensaver_thing_main) 
if not type this in the terminal without the parentheses
  (cd minawan_dvd_screensaver_thing_main)

to start
type these commands in the terminal make sure to press enter after each one and wait for it to download:
  (pip install pygame)
  (pip install PyQt5)
  (pip install pyinstaller)

then to turn the code into a application
use the command in the terminal:
  (pyinstaller --onefile --windowed --add-data "pixalwan.png;." app.py)

this will create a file named app.exe under a folder named dist
to check if it works 

go to dist by using command in the terminal
  (cd dist)
then test by using command
  (app.exe)
