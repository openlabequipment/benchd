"""\
 __                      __          __   __ 
|  |--.-----.-----.----.|  |--.----.|  |_|  |
|  _  |  -__|     |  __||     |  __||   _|  |
|_____|_____|__|__|____||__|__|____||____|__|
--A REPL for Lab Automation and Control------
"""

from .magics import Magics

from IPython.terminal.embed import InteractiveShellEmbed
ipy = InteractiveShellEmbed()

ipy.register_magics(Magics)

def run():
	ipy.show_banner(__doc__)
	ipy.mainloop()