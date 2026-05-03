# What

This is a python library to interact with the Estim 2B box.  Does nothing sepecial, it aims to be an easy to use building block for a bigger system.  I've tried my best to make it a modern python library that's easy to use.

But the best I can do in python is baby babble.

It's pronounced "ee stihm twoo pee".

# API
## Getting started
```python
connection = Estim2pyConnection("/serial/device") # /dev/ttyUSBx on linux

connection.set_channel('A',20) # Set's power level of channel a to 20
connection.set_channel('B',30) # Set's power level of channel b to 30
conneciton.set_channel('C',10) # Sets the first parameter, usually speed, to 10
connection.set_channel('D',50) # Sets the secoond parameeter, usually feeling, to 50
```

That's the basics of it.  Estim2pyConnection is an object that you use to speak to the box.

## Status

Every response it returns is an Estim2pyStatus object that you can use to query the current status of the box.  You can also call `get_status()` at any time.

```
s = connection.get_status()  # -> Estim2pyStatus
# s = connection.set_channel('A',20) # this would work too!

print(f" Battery: is {s.battery}, A:{s.a},B:{s.b},C:{s.c},D:{s.d=},Mode:{s.mode=},Power:{s.power=},Linked:{s.linked=},FW Version:{s.version})")
Those are the values right from the box, but I've provided a bunch of methods for ease of use:
s.get_scaled_level('A')  #-> would return "20", so scaled to what you see on the box, while the underlying serial protocol said "40".
s.high_power() # -> bool
s.low_power() # -> bool
s.linked() # -> bool
s.unlinked() # -> .... guess
```

You can test Status's for equality, and it will do the right thing!  Two status's are considered equal if all of the parameters are equal (A,B,C,D,Mode,Power,Linked) while ignoring information like version or battery level.

### Get Mode Details

`s.get_mode()` returns a Estim2pyMode object, it's a simple object that will return all the information about the current mode.  

```
m = s.get_mode()
print(f"Mode [{m.mid}] {m.name} C Param: {m.param_a} D Param: {m.param_b} Notes: {m.notes}")
```
I know param_a and param_b are bad names. Sorry.  Submit a bug report if it... uhh... bugs you.

Modes don't have a good equality test.  Just use `status.mode`.

You can get details of a mode by number too.
```
m = Estim2pyModes.get_mode(0)
```

### More commands

OH, you can do other things with the connection too!

```
connection.high() # go into high power mode
connection.low() # go into low power mode

connection.reset() # Reset everything, set power to 0
connection.kill() # Set power to 0, keep all other parameters
```

And you can use these, but they are BROKEN

```
# these are implemented, but don't work! I don't know why.
connection.link()   # Link channels, if ... yanno...
connection.unlink() # might actually work! Who knows?
```

Check the test in `test_connection.py` with the `@pytest.mark.hardware` tag for more examples.

# References

- **[Estim2bapi](https://github.com/fredhatt/estim2bapi):** My primary source.  I was using this as my library, but the error handling dind't work for me. 
- **[STPIHKAL](https://buttplug.io/stpihkal/protocols/estim-systems/):** An amazing resource.
- **[cornertime/2b](https://github.com/cornertime/2b):** A pretty good implementation, though I didn't like the aesthetics of the API.  Also, is basically just a big ball of python in a directory
- **[Chaturbase E-stim](https://github.com/cb-stimmer/chaturbate-estim-2b):**

# Ethos

Small little objects that do the right thing and get out of the way.

Abstract out the low level protocol nicely, so that you can build a higher level on top of simply.
