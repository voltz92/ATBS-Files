# assert statements

# assert is another method of raising error 

# this one raises an error when a certain valuable evaluates to false 

# syntax :::  assert condition_that_evaluates_True, what_to_show_in_that_Case


typo = input( '> ')

assert int(typo) > 1, "Typo Must Be Greater than 1"  # this raises an error when typo <= 1, this is useful for checking code
print(typo)