# v 0.4.1
## Bugfixes
- Deleting an Estim2pyConnection whose serial port is already closed (for example after your own disconnect()) no longer prints an ignored PortNotOpenError.

# v 0.4.0
Support for the beta firmwares.  The 2B has had three serial protocols, and the right one is now picked automatically:
- 2.106, the original firmware (9 field status)
- 2.119B (11 fields)
- 2.120B and later, e.g. 2.131B (13 fields)

See the design doc in the documentation for all the gory details.

## Breaking Changes
- Requires Python 3.12 or newer.  It already needed 3.12 (typing.override and the `type` statement), now pyproject.toml says so.
- str() and bytes() of an Estim2pyStatus write the status line in the format of its firmware, with the real battery and version.  They used to write a 9 field line with battery 230 and version 0.2.3.
- set_to_status() no longer changes the status you pass in.  It used to set its linked to 0.
- Estim2pyMode.get_mode() returns a mode named "unknown" for a number it does not know, instead of raising KeyError.

## Additions
- Estim2pyConnection detects the firmware when it connects.  connection.protocol tells you which one.  Pass protocol="2.106", "2.119B" or "2.120B" to skip the detection.
- Beta firmware commands on Estim2pyConnection: dynamic(), set_bias(), set_output_map(), step_channel(), set_warp() and set_ramp() (the last two 2.120B and later).  On firmware without them they raise the new Estim2pyUnsupportedError.
- set_mode_by_name("step") sends the right mode number for the box.  The betas number their modes differently: step is 12 on 2.106 and 15 on the betas.
- version() asks the box for its version, or just its status on 2.106.
- Estim2pyBias (A, B, AVERAGE, MAX) for set_bias() and status.get_bias().  The betas number the bias settings differently, this does the translation.
- Estim2pyStatus has bias, output_map, warp, ramp and protocol members (None when the firmware does not report them), get_bias() and is_dynamic_power().
- Estim2pyMode knows the beta modes, including the new flo, cycle and twist.  get_mode(), id_names() and the new get_id() take a protocol name.
- New module estim2py.protocol with a class per firmware.

## Changes
- link() and unlink() send J1/J0 on beta firmware, and work there.  Still no luck on 2.106.
- set_to_status() works between firmwares: modes are matched by name and the bias by setting.  It also handles dynamic power, link, and the beta settings.
- Status equality and changes() compare bias, output map, warp and ramp when both statuses have them.
- An ERR reply from the box (buffer overrun) is resent once.
- No reply raises "No reply from 2B.  Is it switched on and out of its menu?".  The box ignores serial commands while you are in its menu.

### Estim2pySimulatedConnection
- Simulates any firmware: Estim2pySimulatedConnection("2.120B").
- Rewritten to interpret the commands, so it runs the real connection code.  It follows what a 2.131B box does: low power keeps C and D (2.106 resets them), a new mode resets the channels but keeps the other settings, and dynamic power resets the bias.

## Bugfixes
- Estim2pyError printed "<exception str() failed>" instead of its message.  Now it shows the message and the line the box sent.
- The usage docs called methods that don't exist and said mode 5 is milk.  It's wave.

### Internals
- Tests for every protocol, mocked serial tests for the connection, and hardware tests that adjust to the detected firmware.

# v 0.3
## Breaking Changes 
- Estim2pyStatus methods are now all get_foo or is_foo.
- Estim2pyStatus as_items returns a tuple of tuples.  This sucks and will change I think
- Estim2pyMode internal modes datatype switched from mutable dictionary to tuple

## Additions
- Added an exception, Estim2pyError
- Estim2pyStatus now has >, <, >=, <= comparisons. See the accompanying zine for more information. 
- Estim2pyStatus has a changed method, to tell you which members of two different statuses are different
- much more tests, safe to run if the hardware is not plugged in.
- warning about scratch submissives

## Changes
- Estim2py now uses type hints

### Estim2pySimulatedConnection
- You can now simulate exceptions
- Every status is a deep copy, that way it behaves similarly to the real thing.

### Estim2pyConnection
- Sensible delay timing has been figured out, and set as the default.
- A destructor (__del__) is written to close the serial port
- set_a thru set_d defined 
- bug in setToStatus fixed

### Estim2pyStatus
- get_a thru get_d implemented
- Now handles str() and bytes() nicely
- If parsing a status fails, a proper exceptions will be thrown

### Internals
- unit tests do better checking of hardware existence
- unit tests added to check timing were created (and skipped by default).... SCIENCE
- unit test fixtures used for hardware connection, etc.

# v 0.2.2
## Additions
- (Slightly) Better documentation, trying out sphynx

## Changes
- Fixed logging to be better
- Added set_to_status which changes all settings of the box to the values of an Estim2Status object 
- Tweaked timeout and delay a little.  Not convinced it's right.

# v 0.2.1
## Additions
- Added Doc strings
- Added Documentation
## Changes
- Fixed a typo

# v 0.2.0
## Additions
- Added a changelog
- Added Logging
- Added a way to get key/vals from Estim2pyModes
- Added a simulated connection
## Changes
- Changed Estim2pyMode to be singular.
- Channel arguments have better names
- Channel arguments to status or connection can be upper or lower case
## Bugfixes
- Fixed a bug in get_mode()
- Comparison between two status's now respect type
- Some modes incorrectly reported None for param_b

# v 0.1.0

Babby's first package

