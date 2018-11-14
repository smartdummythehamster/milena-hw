Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 20:42:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> #milena
>>> def remove_duplicates (new_list):
	"""
	Return a copy of old_list which has no duplicate elements.
	>>>remove_duplicates([1,1,3,3,5,5,7,9,9,9])
	[1,3,5,7,9]
	"""
	for e in new_list
	
SyntaxError: invalid syntax
>>> #milena
>>> def remove_duplicates (new_list):
	"""
	Return a copy of old_list which has no duplicate elements.
	>>>remove_duplicates([1,1,3,3,5,5,7,9,9,9])
	[1,3,5,7,9]
	"""
	
SyntaxError: invalid syntax
>>> def remove_duplicates (new_list):
	"""
	Return a copy of old_list which has no duplicate elements.
	>>>remove_duplicates([1,1,3,3,5,5,7,9,9,9])
	[1,3,5,7,9]
	"""
	for e in new_list:
		if e in L2:
			return True
		return False

	
>>> remove_duplicates([1,2,2,2,3,3,3,4,4,4,4,5,6,7,9])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    remove_duplicates([1,2,2,2,3,3,3,4,4,4,4,5,6,7,9])
  File "<pyshell#15>", line 8, in remove_duplicates
    if e in L2:
NameError: name 'L2' is not defined
>>> 
