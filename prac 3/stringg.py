# get_strings_methods()

# 1. capitalize
text = "hello EVERYONE"
print(text.capitalize())

# 2. case-fold
text1 = "heLLo"
text2 = "HELlo"
print(text1.casefold())
print(text2.casefold())

# 3. center
text3 = "DJ"
print(text3.center(26, "_"))

# 4. count
text4 = "abc_abc_abc_abc_abc"
print(text4.count("ab"))

# 5. encode
text5 = "Elon Musk"
print(text5.encode(encoding="UTF-8", errors="strict"))

# 6. endswith
text6 = "Apple"
print(text6.endswith("e"))

# 7. expend-tads
text7 = "Hello \tEveryone \tI'm DJ."
print(text7.expandtabs(20))

# 8. find
text8 = "My name is DJ."
print(text8.find("DJ"))

# 9. format
text9 = "{0}, My mane is {1}"
print(text9.format("Hello everyone!", "DJ"))

# 10. format_map
age: dict = \
    {"x": 45,
     "y": 10}
text10 = "Joel is {x} and Elie is {y}"
print(text10.format_map(age))

# 11. index
text11 = "Hello"
index_num = text11.index("l")
print(index_num)

# 12. is_al_num
text12 = "10"
text13 = "Dj-03"
print(text12.isalnum())
print(text13.isalnum())

# 13. is_alpha
text14 = "Hello"
text15 = "10"
print(text14.isalpha())
print(text15.isalpha())

# 14. is_a_scii
text14 = "Hello"
text16 = "HeLLė"
print(text14.isascii())
print(text16.isascii())

# 15. is_decimal
text17 = "123"
print(text17.isdecimal())

# 16. is_digit
text18 = "765"
text19 = "123"
print(text18.isdigit())
print(text19.isdigit())

# 17. is_numeric
text17 = "875"
text18 = "123"
text20 = "879"
print(text17.isdigit())
print(text18.isdigit())
print(text20.isnumeric())

# 18. is_identifier
text21 = "textSample"
print(text21.isidentifier())

# 19. is_lower
text22 = "abc"
print(text22.islower())

# 20. is_printable
text23 = "text"
print(text23.isprintable())

# 21. is_space
text24 = "    "
print(text24.isspace())

# 22. is_title
text25 = "The Text"
print(text25.istitle())

# 23. is_upper
text26 = "THE"
print(text26.isupper())

# 24. join
x = ["A", "B", "C"]
print("_".join(x))

# 25. l_just
text27 = "A"
print(text27.ljust(99, "_"))

# 26. lower
text28 = "FUN"
print(text28.lower())

# 27. l strip
text29 = "Some text."
print(text29.lstrip('Some'))

# 28. & 29. make_trans & translate
dic = {"I": "nh"}
text30 = "Hello, I Dj."
table = text30.maketrans(dic)

print(table)
print(text30.translate(table))

# 30. partition
text31 = "a+b= c^2"
print(text31.partition("="))

# 31. remove_prefix
text32 = "Endanger"
print(text32.removeprefix("En"))

# 32. remove_suffix
text33 = "Happiness"
print(text33.removesuffix("ness"))

# 33. replace
text34 = "Remember to comment & comment!"
print(text34.replace("comment", "subscribe", 1))

# 34. r_find
text35 = "An apple a day keeps a doctor away!"
print(text35.rfind("a"))

# 35. r_index
text35 = "An apple a day keeps a doctor away!"
print(text35.rindex("a"))

# 36. r_just
text36 = "A"
print(text36.ljust(99, "_"))

# 37.
text37 = "a+b = c^2 = z^2"
print(text37.rpartition("="))

# 38. & 39.
text38 = "Hello everyone good morning."
print(text38.rsplit(sep=" "))
print(text38.split(maxsplit=2))

# 40.
text39 = "I'm Dj Dj."
print(text39.rstrip("Dj"))

# 41.
text40 = "Remember to comment\n or else...\n"
print(text40.splitlines(keepends=True))
print(text40.splitlines())

# 42.
text41 = "Hello"
print(text41.startswith("H"))
print(text41.startswith("h"))

# 43.
text42 = "Hello everyone good morning"
print(text42.strip("Hello"))

# 44.
text43 = "Hello everyone good morning"
print(text43.swapcase())