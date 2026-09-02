
# Python `datetime` Module Reference Guide

A comprehensive reference table of the primary public methods available in Python's standard **`datetime`** module (covering the `datetime`, `date`, `time`, and `timedelta` classes), complete with descriptions, practical examples, and their return values.

## Methods Reference Table

| Method | Class | Description | Example | Return Value |
| :--- | :--- | :--- | :--- | :--- |
| `datetime.now()` | `datetime` | Returns the current local date and time. | `datetime.now()` | `datetime` object |
| `datetime.today()` | `datetime` / `date` | Returns the current local date. | `date.today()` | `date` or `datetime` object |
| `datetime.utcnow()` | `datetime` | Returns the current UTC date and time (naive). | `datetime.utcnow()` | `datetime` object |
| `datetime.strptime()` | `datetime` | Parses a string into a datetime object using a format. | `datetime.strptime("2026-06-05", "%Y-%m-%d")` | `datetime` object |
| `datetime.fromtimestamp()` | `datetime` / `date` | Creates an object from a POSIX timestamp. | `datetime.fromtimestamp(1775433600)` | `datetime` or `date` object |
| `datetime.fromisoformat()` | All core | Parses an ISO 8601 formatted string into an object. | `datetime.fromisoformat("2026-06-05T12:00:00")` | `datetime`, `date`, or `time` object |
| `datetime.fromordinal()` | `date` | Returns a date from a proleptic Gregorian ordinal. | `date.fromordinal(739773)` | `date` object |
| `datetime.combine()` | `datetime` | Combines a separate `date` and `time` object. | `datetime.combine(date(2026, 6, 5), time(12, 0))` | `datetime` object |
| `strftime()` | All core | Formats the object into a customized string. | `dt.strftime("%Y-%m-%d")` | `str` |
| `replace()` | All core | Returns a new object with specified fields updated. | `dt.replace(year=2030)` | Same object type |
| `date()` | `datetime` | Extracts the date portion from a datetime instance. | `dt.date()` | `date` object |
| `time()` | `datetime` | Extracts the time portion from a datetime instance. | `dt.time()` | `time` object |
| `timetz()` | `datetime` | Extracts the time portion along with timezone info. | `dt.timetz()` | `time` object |
| `astimezone()` | `datetime`, `time` | Converts a timezone-aware object to a target timezone. | `dt.astimezone(timezone.utc)` | `datetime` or `time` object |
| `weekday()` | `datetime`, `date` | Returns day of the week as an integer (**Monday = 0, Sunday = 6**). | `dt.weekday()` | `int` (0 to 6) |
| `isoweekday()` | `datetime`, `date` | Returns day of the week as an integer (**Monday = 1, Sunday = 7**). | `dt.isoweekday()` | `int` (1 to 7) |
| `isocalendar()` | `datetime`, `date` | Returns a named tuple containing ISO year, week number, and weekday. | `dt.isocalendar()` | Tuple: `(year, week, weekday)` |
| `toordinal()` | `datetime`, `date` | Returns the proleptic Gregorian ordinal of the date. | `dt.toordinal()` | `int` |
| `timestamp()` | `datetime` | Returns the POSIX timestamp corresponding to the datetime. | `dt.timestamp()` | `float` |
| `timetuple()` | `datetime`, `date` | Returns a `time.struct_time` representation. | `dt.timetuple()` | `time.struct_time` |
| `total_seconds()` | `timedelta` | Returns the total duration expressed in seconds. | `td.total_seconds()` | `float` |
| `utcoffset()` | All core | Returns the UTC offset as a timedelta, if available. | `dt.utcoffset()` | `timedelta` or `None` |
| `tzname()` | All core | Returns the timezone name as a string, if available. | `dt.tzname()` | `str` or `None` |
| `dst()` | All core | Returns the Daylight Saving Time offset, if available. | `dt.dst()` | `timedelta` or `None` |

## Date time format Formating

| Code | Description |
| :--- | :--- |
| `%d` | Day of month as a number |
| `%m` | Month as a number |
| `%y` | 2-digit year |
| `%Y` | 4-digit year |
| `%H` | Hour of day in 24-hour format |
| `%M` | Minute as number |
| `%S` | Second as number |

## strptime code format

| Code | Description | Example |
| :--- | :--- | :--- |
| `%a` | Abbreviated weekday name | Sat |
| `%A` | Full weekday name | Saturday |
| `%b` | Abbreviated month name | Oct |
| `%B` | Full month name | October |
| `%d` | Zero-padded day of month as a number | 01 |
| `%m` | Zero-padded month as a number | 01 |
| `%Y` | 4-digit year | 1977 |
| `%y` | 2-digit year | 77 |
| `%H` | Hour of day in 24-hour format | 13 |
| `%I` | Hour of day in 12-hour format | 01 |
| `%M` | Minute as number | 59 |
| `%S` | Second as number | 59 |
| `%p` | AM/PM specifier | AM |
| `%f` | Microsecond | 0153219 |



## Quick Example Usage

```python
from datetime import datetime, timedelta

# 1. Using .now() and .strftime()
current_dt = datetime.now()
formatted_str = current_dt.strftime("%B %d, %Y") 

# 2. Using .replace() and timedelta arithmetic
future_dt = current_dt.replace(year=2030) + timedelta(days=15)

# 3. Using .isocalendar()
year, week, day = current_dt.isocalendar()
