import imageio, numpy as np, gi

# M.Hanny Sabbagh <mhsabbagh@outlook.com>, 2017.
# This program free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def imgcreategif(inputimages, outputgif, duration):
  images = []

  for i in inputimages:
    images.append(i)

  with imageio.get_writer(outputgif, mode='I', duration=duration) as writer:
    for filename in images:
		    image = imageio.imread(filename)
		    writer.append_data(image)
  writer.close()

def vidcreategif(inputvideo, outputgif, fps, colors):
  videofile = imageio.mimread(inputvideo)
  imageio.mimsave(outputgif, videofile, fps=fps, palettesize=int(colors))

def remapgif(inputgif, outputgif, duration, colors):
  gifimage = imageio.volread(inputgif)
  with imageio.get_writer(outputgif, mode='I', palettesize=int(colors), duration=duration) as writer:
      for x in range(len(gifimage)):
        writer.append_data(gifimage[x])
  writer.close()

def removeframes(inputgif, outputgif, duration):
  print "An indexerror was ignored.."
  gifimage = imageio.mimread(inputgif)
  with imageio.get_writer(outputgif, mode='I', duration=duration) as writer:
      for x in range(len(gifimage)):
        if x/2 == 0:
          pass
        else:
          del gifimage[x]
        writer.append_data(gifimage[x])
  writer.close()

def poffset(inputgif, outputgif, duration, offset):
  gifimage = imageio.mimread(inputgif)
  with imageio.get_writer(outputgif, mode='I', duration=duration) as writer:
      for x in range(len(gifimage)):
        gifimage[x][:][:][:][:] = gifimage[x][:][:][:]+offset
        writer.append_data(gifimage[x])
  writer.close()
  
def noffset(inputgif, outputgif, duration, offset):
  gifimage = imageio.mimread(inputgif)
  with imageio.get_writer(outputgif, mode='I', duration=duration) as writer:
      for x in range(len(gifimage)):
        gifimage[x][:][:][:][:] = gifimage[x][:][:][:]-offset
        writer.append_data(gifimage[x])
  writer.close()

def doffset(inputgif, outputgif, duration, offset):
  gifimage = imageio.mimread(inputgif)
  with imageio.get_writer(outputgif, mode='I', duration=duration) as writer:
      for x in range(len(gifimage)):
        gifimage[x][:][:][:][:] = gifimage[x][:][:][:]/offset
        writer.append_data(gifimage[x])
  writer.close()
  
def flip(inputgif, outputgif, duration):
  gifimage = imageio.mimread(inputgif)
  with imageio.get_writer(outputgif, mode='I', duration=duration) as writer:
      for x in range(len(gifimage)):
        shape = gifimage[x].shape
        gifimage[x] = np.fliplr(gifimage[x])
        writer.append_data(gifimage[x])
  writer.close()
  
def rotate(inputgif, outputgif, duration, numof90rotates):
  gifimage = imageio.mimread(inputgif)
  with imageio.get_writer(outputgif, mode='I', duration=duration) as writer:
      for x in range(len(gifimage)):
        shape = gifimage[x].shape
        gifimage[x] = np.rot90(gifimage[x], numof90rotates)
        writer.append_data(gifimage[x])
  writer.close()
  
imgcreategif(['desktop-1.png', 'desktop-2.png', 'desktop-3.png', 'desktop-4.png'], "output-0.gif", 1)
vidcreategif("video.mp4", 'output-1.gif', 25, 256)
poffset("output-0.gif", "output-4.gif", 1, 20)
noffset("output-0.gif", "output-5.gif", 1, 20)
doffset("output-0.gif", "output-6.gif", 1, 3)
flip("gif-2.gif", "output-7.gif", 0.05)
rotate('gif-3.gif', 'output-8.gif', 0.05, 2)
delarow('gif-4.gif', 'output-9.gif', 0.15)
removeframes("output-1.gif", "output-3.gif", 0.075)
