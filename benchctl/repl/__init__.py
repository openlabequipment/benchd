"""\
 __                      __          __   __ 
|  |--.-----.-----.----.|  |--.----.|  |_|  |
|  _  |  -__|     |  __||     |  __||   _|  |
|_____|_____|__|__|____||__|__|____||____|__|
--A REPL for Lab Automation and Control------
"""


from IPython.terminal.embed import InteractiveShellEmbed
ipy = InteractiveShellEmbed()

def run():
	ipy.show_banner(__doc__)
	ipy.mainloop()