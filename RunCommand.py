import sublime, sublime_plugin, subprocess

class RunInCmdCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
		    if not region.empty():   
		        s = self.view.substr(region)
		        subprocess.call("cmd.exe /C " + s)
		        