(!) This program does require pygame to be installed.

This has been rather interesting to follow along. 
Understandably while it does hand hold me through out the entire process, it has been my own hands typing the code, my brain learning what is infront of me, and my own ability to debug my mistakes. A lot of it does involve understanding how the pygame library works,  that will be critical for any future games I may want to create. What has been really helpful through all of this: forcing me to troubleshoot when things happen and look for answers. I've gotten really good at reading errors and fixing them (which is like what 70% of computer science is).

Obstacles I had to Face: 
-	Pygame does not work for the homebrew version of Python3; must download from the original python site. 
-	Little bugs due to spelling situations (easy fixes) 
-	self.font = pygame.font.SysFont(None, 15) - freezes the game if pygame is not properly configured. There was a bug in pygame via the sysfont.py file where it pointed to a dead font list and I had to go in and change it to point to the correct front list. Took three hrs (Aug 26) but it has been done. (now points to /Library/Font/font-list) 

Based on the alien project from Python Crash Course BK </br> 
finished: Aug 27, 2019 (Tu) - taking approx one wk 