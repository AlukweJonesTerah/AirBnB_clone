"""
Command line interpreter

This module is runs the cmd module to allow the user
to Interact with the system
"""
import cmd
import readline
import re

print(dir(cmd.Cmd))
class MyCommand(cmd.Cmd):
	prompt = "(Type your command here): "

	def emptyline(self):
		"""This function does nothing on an empty line on the cmd interpreter """
		pass
	def do_EOF(self, line):
		"""Exit the console by holding (ctrl+D) command"""
		print()
		print()
		return True
	def do_add(self, s):
		l = s.split()
		if len(l) != 2:
			print("*** invalid number of arguments")
			return
		try:
			l = [int(i) for i in l]
		except ValueError:
			print("*** arguments should be numbers")
			return
		print(l[0] + l[1])

	def do_helloworld(self, line):
		print("Hello world" + line)

	def complete_helloword(self, text, line, begidx, endidx):
		possibilities = ["user", "oliver", "matterlear"]
		return [f for f in possibilities if f.startswith(text)]
	def help_add(self):
		print('add two integral numbers')
	def do_quit(self, arg):
		"""This quits or exits the program"""
		return True
	def help_quit(self, arg):
		""" Helps to define the quit function"""
		print("Quit command to exit the program\n")


	# aliasing
	do_exit = do_quit
# MyCommand().cmdloop()

if __name__ == "__main__":
	# readline.parse_and_bind("tab: complete") for UNIX
	readline.parse_and_bind("bind ^rl_complete") # for MAC
	interface = MyCommand()
	interface.cmdloop()