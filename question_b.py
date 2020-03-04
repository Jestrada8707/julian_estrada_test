from main_package import main_scripts
from main_package.sub_package import sub_scripts

"""This function accepts only two parameters in string format and 
and analise which number is greater or equal and import that function from main package"""

main_scripts.greater_than(9, 4)  # this values is for example only
main_scripts.greater_than(1.2, 1.4)
main_scripts.greater_than(7, 7)

"""This functions are imported from subpackage and one return is a even number and the other 
only is the one or two parameters are negative"""

sub_scripts.is_even_number(3, 6) # this values is only for examples
sub_scripts.is_even_number(2, 9)
sub_scripts.is_even_number(7, 7)
sub_scripts.is_even_number(1.4, 4.5)
