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

