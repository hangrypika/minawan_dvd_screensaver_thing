Before running make sure you have the python language installed
Then in the terminal make sure you are in the correct directory
(should be in minawan_dvd_screensaver_thing_main) 
if not use command
  cd minawan_dvd_screensaver_thing_main

to start
Use commands:
  pip install pygame
  pip install PyQt5
  pip install pyinstaller

then to turn the code into a application
use the command
  pyinstaller --onefile --windowed --add-data "pixalwan.png;." app.py

this will create a file named app.exe under a folder named dist
to check if it works 

go to dist by using command
  cd dist
then test by using command
  app.exe
