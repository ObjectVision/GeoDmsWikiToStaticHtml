---
title: special-characters
layout: default
nav_exclude: true
---
*[configuration-examples](configuration-examples) Special characters*

## escape characters

In the GeoDMS [escape characters](https://en.wikipedia.org/wiki/Escape_character) can be used to configure special characters, see the examples:

```
parameter<string> SingleQuote  := '\''';
parameter<string> DoubleQuote  := '\"'; 
//  The double quote with an escape character is needed in the expression syntax with expr = ".."
//, as the double quote is also used in this syntax to indicate the start and end of the expression.
parameter<string> tab          := '\t';
parameter<string> newline      := '\n';
parameter<string> backslash    : ['\\'];
parameter<string> forwardslash : ['//'];
```

## missing data

Missing data (null values) can be configured, based on the [value-type](value-type), in different ways; see the examples:

```
parameter<uint32> null_u32    := 4294967295;
parameter<uint32> null_u32    := 0 / 0;
// The null value for uint32 is used as the transparent colour in items with colour visualisation style.
   parameter<uint8>  null_u8     := 255b;
or parameter<uint32> null_u8     := 0b / 0b;
   parameter<string> null_string := string(0 / 0);

parameter<string> emptystring := '';
```

The emptystring [parameter](parameter) does not configure a null value, but a string with no characters.