---
title: operator
layout: default
has_children: true
nav_order: 28
---
An Operator is a symbolic representation of a function to be applied on [operands](https://en.wikipedia.org/wiki/Operand). This application is
called an operation. [Operands](https://en.wikipedia.org/wiki/Operand) can be [data-item](data-item) or [literals](https://en.wikipedia.org/wiki/Literal_(computer_programming)).

In [expression](expression) with multiple operators, the precedence of the evaluation is based on the precedence order and the associativity within this order. Operators with lower orders are evaluated first.

### **Examples:**

- -3^2 is evaluated as (-3)^2 or pow(neg(3), 2) due to the higher precedence order of the unary [sub](sub) operator.
- a / b * c is evaluated as (a / b) * c or mul(div(a,b), c) due to the equal order and left to right associativity of the [mul](mul) and [div](div) operator.
- a?b:c?d:e is evaluated as a?b:(c?d:e) due to the right to left associativity of the immediate if operators.
- a || b && c is evaluated as a || (b && c) or or(a, and(b, c) due to the higher precedence order of the and operator.

Use brackets to overrule the precedence rules.

<table>
<tbody>
<tr class="odd">
<td><strong>Operator</B></td>
<td><B>Name</B></td>
<td><B>Order Precedence</B></td>
<td><B>Associativity</B></td>
<td><B>Description</B></td>
<td><B>Equivalent Function</B></td>
</tr>
<tr class="even">
<td>+ (unary)</td>
<td>plus</td>
<td>0</td>
<td>right to left</td>
<td><B>+</B>a means a</td>
<td></td>
</tr>
<tr class="odd">
<td>- (unary)</td>
<td>minus</td>
<td>0</td>
<td>right to left</td>
<td><B>-</B>a means -a</td>
<td>[sub](sub)</a></td>
</tr>
<tr class="even">
<td>#</td>
<td>nrofrows</td>
<td>0</td>
<td>-</td>
<td><B>#</B>u means number of rows of unit u</td>
<td>[nrofrows](nrofrows)</a></td>
</tr>
<tr class="odd">
<td>^</td>
<td>power</td>
<td>1</td>
<td>left to right</td>
<td>a <B>^</B> b means a to the b-th power</td>
<td>[pow](pow)</a></td>
</tr>
<tr class="even">
<td>!</td>
<td>subitem</td>
<td>1</td>
<td>left to right</td>
<td>a<B>!</B>b means subitem(a, b)</td>
<td>[subitem](subitem)</a></td>
</tr>
<tr class="even">
<td>.</td>
<td>parent item</td>
<td>1</td>
<td>left to right</td>
<td>id(<B>.</B>) means id(parent item)</td>
<td></td>
</tr>
<tr class="odd">
<td>[..] or -> </td>
<td>array access</td>
<td>1</td>
<td>left to right</td>
<td>a<B>[</B>b<B>]</B> means lookup(b, a) if b is a data item</td>
<td>[lookup](lookup)</a></td>
</tr>
<tr class="even">
<td>[..]</td>
<td>value</td>
<td>1</td>
<td>left to right</td>
<td>a<B>[</B>b<B>]</B> means value(a,b) if b is a unit</td>
<td>[value](value)</td>
</tr>
<tr class="odd">
<td>*</td>
<td>multiply</td>
<td>2</td>
<td>left to right</td>
<td>a <B>*</B> b means a multiplied with b</td>
<td>[mul](mul)</a></td>
</tr>
<tr class="even">
<td>/</td>
<td>divide</td>
<td>2</td>
<td>left to right</td>
<td>a <B>/</B> b means a divided by b (spaces are necessary)</td>
<td>[div](div)</a></td>
</tr>
<tr class="odd">
<td>%</td>
<td>modulo</td>
<td>2</td>
<td>left to right</td>
<td>a <B>%</B> b means a modulo b</td>
<td>[mod](mod)</td>
</tr>
<tr class="even">
<td>+(binary)</td>
<td>plus</td>
<td>3</td>
<td>left to right</td>
<td>a <B>+</B> b means a plus b</td>
<td>[add](add)</td>
</tr>
<tr class="odd">
<td>- (binary)</td>
<td>minus</td>
<td>3</td>
<td>left to right</td>
<td>a <B>-</B> b means a minus b</td>
<td>[sub](sub)</a></td>
</tr>
<tr class="even">
<td>==</td>
<td>equal to</td>
<td>4</td>
<td>left to right</td>
<td>a <B>==</B> b means a equals b</td>
<td>[eq](eq)</td>
</tr>
<tr class="odd">
<td>!=</td>
<td>not equal to</td>
<td>4</td>
<td>left to right</td>
<td>a <B></B>b means a not equals b</td>
<td>[not](not)</a></td>
</tr>
<tr class="even">
<td>&lt;</td>
<td>less than</td>
<td>4</td>
<td>left to right</td>
<td>a <B>&lt;</B> b means a less than b</td>
<td>[lt](lt)</td>
</tr>
<tr class="odd">
<td>&lt;=</td>
<td>less than or<br />
equal to</td>
<td>4</td>
<td>left to right</td>
<td>a <B>&lt;=</B> b means a less than or equal to b</td>
<td>[le](le)</td>
</tr>
<tr class="even">
<td>&gt;</td>
<td>greater than</td>
<td>4</td>
<td>left to right</td>
<td>a <B>&gt;</B> b means a greater than b</td>
<td>[gt](gt)</td>
</tr>
<tr class="odd">
<td>&gt;=</td>
<td>greater than or<br />
equal to</td>
<td>4</td>
<td>left to right</td>
<td>a <B>&gt;=</B> b means a greater than or equal to b</td>
<td>[ge](ge)</td>
</tr>
<tr class="even">
<td>! (unary)</td>
<td>not</td>
<td>5</td>
<td>right to left</td>
<td><B>!</B>a means not a</td>
<td>[not](not)</td>
</tr>
<tr class="odd">
<td>&amp;&amp;</td>
<td>and</td>
<td>6</td>
<td>left to right</td>
<td>a <B>&amp;&amp;</B> b means a and b</td>
<td>[and](and)</td>
</tr>
<tr class="even">
<td>||</td>
<td>or</td>
<td>7</td>
<td>left to right</td>
<td>a <B>||</B> b means a or b</td>
<td>[or](or)</td>
</tr>
<tr class="odd">
<td>? :</td>
<td>then else (in an iif expression)</td>
<td>8</td>
<td>right to left</td>
<td><em>cond-expr<BR>? then-expr<BR>: else-expr</em></td>
<td>[iif](iif)</td>
</tr>
</tbody>
</table>