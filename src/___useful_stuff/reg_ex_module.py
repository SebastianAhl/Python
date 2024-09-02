"Information about RegEx (Regular Expressions)"
# more information: https://www.w3schools.com/python/python_regex.asp

# source https://www.w3schools.com/python/python_regex.asp:
    # A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
    # RegEx can be used to check if a string contains the specified search pattern.

import re

Some_Text = "Hello World, today the weather is fine"

print(re.search("^Hello.*fine$", Some_Text))

# Metacharacters (source: https://www.w3schools.com/python/python_regex.asp)
    # Character     Description                                 Example
    # []            A set of characters	                        "[a-m]"	
    # \             Signals a special sequence (can also be     "\d"
    #               used to escape special characters)		
    # .	            Any character (except newline character)	"he..o"	
    # ^	            Starts with	                                "^hello"	
    # $	            Ends with	                                "planet$"	
    # *	            Zero or more occurrences	                "he.*o"	
    # +	            One or more occurrences	                    "he.+o"	
    # ?	            Zero or one occurrences	                    "he.?o"	
    # {}	        Exactly the specified number of occurrences	"he.{2}o"	
    # |	            Either or	                                "falls|stays"	
    # ()	        Capture and group

# Functions (source: https://www.w3schools.com/python/python_regex.asp)
    # Function	    Description
    # findall	    Returns a list containing all matches
    # search	    Returns a Match object if there is a match anywhere in the string
    # split	        Returns a list where the string has been split at each match
    # sub	        Replaces one or many matches with a string
