import imageio, numpy as np, gi, os

gi.require_version('Gtk','3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("ui.glade")

window = builder.get_object("window1")
radio1 = builder.get_object("radio1")
radio2 = builder.get_object("radio2")
radio3 = builder.get_object("radio3")
radio4 = builder.get_object("radio4")
radio5 = builder.get_object("radio5")
radio6 = builder.get_object("radio6")
folderchooser = builder.get_object("filechooser")

radio1.set_label("Convert to GIF")
radio2.set_label("Reduce to 128 colors")
radio3.set_label("Reduce to 64 colors")
radio4.set_label("Reduce to 32 colors")
radio5.set_label("Reduce to 16 colors")
radio6.set_label("Remove Half Frames")
window.set_title("GIF Format Manipulator")

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
  gifimage = imageio.mimread(inputgif)
  with imageio.get_writer(outputgif, mode='I', palettesize=int(colors), duration=duration) as writer:
      for x in range(len(gifimage)):
        writer.append_data(gifimage[x])
  writer.close()

def colorgreen(inputgif, outputgif, duration):
  gifimage = imageio.mimread(inputgif)
  with imageio.get_writer(outputgif, mode='I', duration=duration) as writer:
      for x in range(len(gifimage)):
        writer.append_data(gifimage[x])
  writer.close()

#imgcreategif(['image-1.png','image-2.png'], 'output.gif', 0.5)
#remapgif('output.gif', 'output2.gif', 0.5, 16)

class Handler:
  def buttonclicked(self, GtkButton):
    folderpath = folderchooser.get_uri()
    folderpath = folderpath.replace("file://", "")
    files = os.listdir(folderpath)
    listoffiles = []
    for i in files:
      listoffiles.append(folderpath+"/"+i)
    for x in files:
      imgcreategif(listoffiles, 'output.gif', 0.5)

  def close(self, button):
    Gtk.main_quit()
    
  def chooserclicked(self, GtkButton):
    filechooserdialog.hide()
 
    
builder.connect_signals(Handler())

if __name__ == "__main__": 
    window.show_all()
    Gtk.main()
