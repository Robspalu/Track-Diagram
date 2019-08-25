#!/usr/bin/env python3

#BHLR Track Display
"""
To provide a dynamic track display to Station Master
"""

from tkinter import *
import time


#Update the Tracks
def track(n,i):
        c = n
        
        c.itemconfig(i, fill="red") # change color
     #   print (c.gettags(i))
     #   tu = c.find_withtag('CA')
     #   tLen = len(tu)
     #   print ("First tuple length : ", len(tu))
        #if tLen != 0
        #        idx = tu[0]
        #else
        idx = 0
        t = "its index {0:3d} ".format(idx)
        c.create_text(20, 40, anchor=W, font="Purisa",text=t)
           
def readData(c,t,lines):
       for i in range(1,100):
           # Add Track Layout
           aTrack = lines[i]
           SX = int(aTrack[11:14])
           SY = int(aTrack[15:18])
           EX = int(aTrack[19:22])
           EY = int(aTrack[23:26])
           tName = aTrack[1:5]
           tName = tName.rstrip 
           item = c.create_line(SX,SY,EX,EY, fill="black", width = 5, tags=tName)
           c.tracks.append(item)

# The graphical interface
class TkBHLR:

    # Create our objects
    def __init__(self):
        self.tk = tk = Tk()
        self.tk.title('BHLR!!!')
        # Create the Canvas
        self.canvas = c = Canvas(tk,width=1000, height = 600)
        c.pack()
        width, height = tk.getint(c['width']), tk.getint(c['height'])
        # Read Data File
        f = open("Resources\Tracks", "r")
        # use readlines to read all lines in the file
        # The variable "lines" is a list containing all lines in the file
        lines = f.readlines()
        # close the file after reading the lines.
        f.close()
        self.tracks = []
        for i in range(1,100):
           # Add Track Layout
           aTrack = lines[i]
           SX = int(aTrack[11:14])
           SY = int(aTrack[15:18])
           EX = int(aTrack[19:22])
           EY = int(aTrack[23:26])
           tName = aTrack[0:5]
           #tName = tName.rstrip 
           item = c.create_line(SX,SY,EX,EY, fill="black", width = 5, tags=tName)
           self.tracks.append(item)        
           self.tk.update()
 #       readData(c,t,lines)
        
        TE1 = PhotoImage(file='Resources\CL-On.gif')
        z = c.create_image(100,100,image = TE1)
        
        #l = Listbox(self, height=10)
        
                                  


    # Run -- never returns
    def run(self):
        while 1:

          track(self.canvas,'CA')
          self.canvas.update_idletasks()
          time.sleep(1)



def main():
    import sys

    # First argument is number of pieces, default 4
    if sys.argv[1:]:
        n = int(sys.argv[1])
    else:
        n = 20

    # Second argument is bitmap file, default none
    if sys.argv[2:]:
        bitmap = sys.argv[2]
        # Reverse meaning of leading '@' compared to Tk
        if bitmap[0] == '@': bitmap = bitmap[1:]
        else: bitmap = '@' + bitmap
    else:
        bitmap = None

    # Create the graphical objects...
    h = TkBHLR()

    # ...and run!
    h.run()


# Call main when run as script
#if __name__ == '__main__':
#    main()
