#!/usr/bin/env python

from gi.repository import Gtk
from gi.repository import Gio
from gi.repository import WebKit2
from gi.repository import GLib
import os

builder = Gtk.Builder()
builder.add_from_file("app.glade")

def redo(*args):
	async.cancel()
	content=textbuffer.get_text(textbuffer.get_bounds()[0],textbuffer.get_bounds()[1],False)
	content=GLib.strescape(content,"")
	webview.run_javascript("str = \""+content+"\";preview();",async,None,None)

handlers = {
	"gtk_main_quit":Gtk.main_quit,
	"redo":redo
	}

async = Gio.Cancellable()
window = builder.get_object("applicationwindow1")
window.maximize()
builder.connect_signals(handlers)
webkit_container = builder.get_object("webkit_container")
webview = WebKit2.WebView();
webkit_container.add(webview)

textbuffer = builder.get_object("textbuffer");
filepath=os.path.dirname(os.path.abspath(__file__))

webview.load_uri("file://"+filepath+"/index.html")

window.show_all()
Gtk.main()
