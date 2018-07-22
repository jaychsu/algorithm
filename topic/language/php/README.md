PHP Syntax Note
======

## General

- A PHP script starts with `<?php` and ends with `?>`. You can also use the shorthand PHP tags, `<?` and `?>`, as long as they're supported by the server.
- PHP statements end with semicolons `;`.
- Comment: single-line `//`, multi-line begins with `/*` and ends with `*/`.

## Variable and Constant

`$variable_name = value;`
`echo $variable_name;`

- A variable name can only contain alpha-numeric characters and underscores. (`A-z`, `0-9`, and `_`)
- A variable name must start with a letter or an underscore.
- Variable names are case-sensitive. (`$name` and `$NAME` would be two different variables)

`define(CONSTANT_NAME, value, case-insensitive);`
`echo CONSTANT_NAME;`

- Constants are similar to variables except that they cannot be changed or undefined after they've been defined.
- name: Specifies the name of the constant.
- value: Specifies the value of the constant.
- case-insensitive: Specifies whether the constant name should be case-insensitive. Default is `false`.
