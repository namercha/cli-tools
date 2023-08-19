# cli-tools

A selection of CLI programs built in python using Click

### greeter.py

Simple program that greets user

```
$ greetings First Last
Hello, First Last

$ greetings --help
```

### calculator.py
```
$ add 12 2345 234
2591

$ subtract 34 23 1
10

$ add 10 20 30 -v
60

$ add 10 20 30 -vv
10 = 10
10 + 20 = 30
10 + 20 + 30 = 60
```

### authenticate.py
```

$ authenticate    
Username: Nabil
Password: 
Repeat for confirmation: 
Error: The two entered values do not match.
Password: 
Repeat for confirmation: 
Logging in Nabil
```

### fileutils.py

```
$ note ./notes.txt
Enter lines of text below and CTRL + C to exit.
> This is the first line I have entered.
> There are more lines I can type.
> The output should show up in a new file called notes.txt
> ^C
output written to file ./notes.txt
```

```
$ concat file1.txt file2.txt file3.txt combined.txt
file1.txt written to combined.txt
file2.txt written to combined.txt
file3.txt written to combined.txt
```

### notes.py

```
$ notes --help
Usage: notes [OPTIONS] COMMAND [ARGS]...

  Program for managing notes.

Options:
  --help  Show this message and exit.

Commands:
  add     Adds note to notes database.
  delete  Deletes note in notes database.
  show    Shows notes in notes database.
  update  Updates note in notes database.
```
