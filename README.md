# Pymatica
Math-toolbox written in python 3 with CLI interface.

# Usage
Pymatica has two modes: interactive and standalone. 

## Interactive mode
This mode gives you a REPL-like interface where you type a command and then its arguments. 
For example: add 5 8
This command will run the "add" kernel and it will pass in the arguments "5" and "8". It will return "13".
After this you can enter another command.
The last answer wil be saved in a variable called "last". To use it type in "last" as one of the arguments:
add 2 last
This will return 15 (13 + 2).

## Standalone mode
This mode enables you to use a single kernel. This is especially useful if the kernel has subcommands.
