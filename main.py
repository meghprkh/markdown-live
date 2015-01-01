#!/usr/bin/env python

from gi.repository import Gtk
from gi.repository import WebKit2
from gi.repository import GLib
import os

builder = Gtk.Builder()
builder.add_from_file("app.glade")

inithtml="""<html>
 <head>
  <link rel="stylesheet" type="text/css" href="markdown.css">
  <script src=\"marked.js\"></script>
  <script>
   var str=\""""
endhtml="""\";
  </script>
  <script src=\"markdown-view.js\"></script>
 </head>
 <body onload=\"preview()\">
  <div class=\"markdown-body\" id=\"preview\">
  </div>
 </body>
</html> 
"""
def redo(*args):
	content=textbuffer.get_text(textbuffer.get_bounds()[0],textbuffer.get_bounds()[1],False)
	content=GLib.strescape(content,"")
	webview.load_html(inithtml+content+endhtml,"file://"+filepath+"/index.html")

handlers = {
	"gtk_main_quit":Gtk.main_quit,
	"redo":redo
	}

window = builder.get_object("applicationwindow1")
window.maximize()
builder.connect_signals(handlers)
webkit_container = builder.get_object("webkit_container")
webview = WebKit2.WebView();
webkit_container.add(webview)

textbuffer = builder.get_object("textbuffer");
filepath=os.path.dirname(os.path.abspath(__file__))

window.show_all()
Gtk.main()
