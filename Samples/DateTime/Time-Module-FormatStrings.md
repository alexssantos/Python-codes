[ Time Module ] 

# String names

- ## Week
### Weekday name 
> %a
### Full weekday name
> %A.

- ## Month
### Abbreviated month name
> %b
### Full month name.
> %B

# Date and Time (int)

- ## Date
### Appropriate date and time representation.
> %c
### Day of the month as a decimal number [01,31].
>%d	
	
### Day of the year as a decimal number [001,366].
> %j	
### Month as a decimal number [01,12].
> %m	

### Equivalent of either AM or PM.
> %p	

- ## Time
### Hour (24-hour clock) as a decimal number [00,23].
> %H	
### Hour (12-hour clock) as a decimal number [01,12].
> %I
### Minute as a decimal number [00,59].
> %M	
### Second as a decimal number [00,61].
> %S	


# Week days (int)
### Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.
>%U	
### Weekday as a decimal number [0(Sunday),6].
>%w	
### Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.
>%W	

# Data
### Appropriate date representation.
>%x	
### Apropriate time representation.
>%X	
### Year without century as a decimal number [00,99].
>%y	
### Year with century as a decimal number.
>%Y	
### Time zone name (no characters if no time zone exists).
>%Z	
### A literal ‘%’ character.
>%%	