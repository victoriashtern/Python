
## What is Python's `locale` Module?

Python's **`locale` module** is a built-in module that helps programs work with **language- and region-specific formatting**.

For example, different countries format numbers and currencies differently:

## Common Uses

The `locale` module can be used for:

- 💰 **Currency formatting**
- 🔢 **Number formatting**
- 🌍 **Region-specific formatting**
- 🔤 **Locale-aware string comparison**
- 🔄 **Converting locale-formatted numbers**

## Simple Rule to Remember

> `locale` = formatting data according to a specific language and region.

| Country | Number Format |
|---|---:|
| 🇺🇸 US | `1,234.56` |
| 🇩🇪 Germany | `1.234,56` |
| 🇫🇷 France | `1 234,56` |


## Python `locale` Module

| Method / Function | Description | Example | Output / Result |
|---|---|---|---|
| locale.setlocale() | Sets the current locale | locale.setlocale(locale.LC_ALL, "en_US.UTF-8") | Sets locale to English (US) |
| locale.getlocale() | Gets the current locale | locale.getlocale() | ('en_US', 'UTF-8') |
| locale.localeconv() | Gets locale-specific formatting information | locale.localeconv() | Returns a dictionary of formatting settings |
| locale.currency() | Formats a number as currency | locale.currency(1234.50) | `$1,234.50` |
| locale.format_string() | Formats a number according to locale | locale.format_string("%.2f", 1234.5, grouping=True) | 1,234.50 |
| locale.format() | Formats a number according to locale | locale.format("%.2f", 1234.5) | 1234.50 |
| locale.atof() | Converts a locale-formatted string to a float | locale.atof("1234.50") | 1234.5 |
| locale.atoi() | Converts a locale-formatted string to an integer | locale.atoi("1,234") | 1234 |
| locale.str() | Converts a number to a locale-aware string | locale.str(1234.5) | Locale-formatted string |
| locale.delocalize() | Removes locale-specific formatting | locale.delocalize("1,234.50") | "1234.50" |
| locale.localize() | Applies locale-specific formatting | locale.localize("1234.50") | Locale-formatted string |
| locale.getpreferredencoding() | Gets the preferred system encoding | locale.getpreferredencoding() | UTF-8 |

```
import locale

locale.setlocale(locale.LC_ALL, "")

price = 1234.50

print(locale.currency(price, grouping=True))

```



