#Python String method list
capitalize(	)
center(	width[, fillchar])
	Return centered in a string of length width. Padding is done using the specified fillchar (default is a space). Changed in version 2.4: Support for the fillchar argument.
count(	sub[, start[, end]])
	Return the number of occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation.
decode(	[encoding[, errors]])
	Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding. errors may be given to set a different error handling scheme. The default is 'strict', meaning that encoding errors raise UnicodeError. Other possible values are 'ignore', 'replace' and any other name registered via codecs.register_error, see section 4.8.1. New in version 2.2. Changed in version 2.3: Support for other error handling schemes added.
encode(	[encoding[,errors]])
	Return an encoded version of the string. Default encoding is the current default string encoding. errors may be given to set a different error handling scheme. The default for errors is 'strict', meaning that encoding errors raise a UnicodeError. Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' and any other name registered via codecs.register_error, see section 4.8.1. For a list of possible encodings, see section 4.8.3. New in version 2.0. Changed in version 2.3: Support for 'xmlcharrefreplace' and 'backslashreplace' and other error handling schemes added.
endswith(	suffix[, start[, end]])
	Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position. With optional end, stop comparing at that position.
expandtabs(	[tabsize])
	Return a copy of the string where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed.
find(	sub[, start[, end]])
	Return the lowest index in the string where substring sub is found, such that sub is contained in the range [start, end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
index(	sub[, start[, end]])
	Like find(), but raise ValueError when the substring is not found.
isalnum(	)
	Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise.
isalpha(	)
isdigit(	)
islower(	)
isspace(	)
isupper(	)
join(	seq)
ljust(	width[, fillchar])
	Return the string left justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than len(s). Changed in version 2.4: Support for the fillchar argument.
lower(	)
lstrip(	[chars])
replace(	old, new[, count])
	Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.
rfind(	sub [,start [,end]])
	Return the highest index in the string where substring sub is found, such that sub is contained within s[start,end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
rindex(	sub[, start[, end]])
	Like rfind() but raises ValueError when the substring sub is not found.
rjust(	width[, fillchar])
	Return the string right justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than len(s). Changed in version 2.4: Support for the fillchar argument.
rsplit(	[sep [,maxsplit]])
	Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done, the rightmost ones. If sep is not specified or None, any whitespace string is a separator. Except for splitting from the right, rsplit() behaves like split() which is described in detail below. New in version 2.4.
rstrip(	[chars])
split(	[sep [,maxsplit]])
splitlines(	[keepends])
	Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.
startswith(	prefix[, start[, end]])
strip(	[chars])
swapcase(	)
upper(	)
zfill(	width)
	Return the numeric string left filled with zeros in a string of length width. The original string is returned if width is less than len(s)
