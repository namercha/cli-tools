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