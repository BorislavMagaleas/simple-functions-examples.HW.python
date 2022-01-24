def wrap_brackets( text ):
    return "(" + text + ")"

def wrap_square_brackets( text ):
    return "[[[" + text + "]]]"

def wrap_angle_brackets( text ):
    return "<<<" + text + ">>>"

print( wrap_angle_brackets( wrap_square_brackets( wrap_brackets("12345") ) ) )