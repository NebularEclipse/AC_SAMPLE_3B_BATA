import math

import streamlit as st

def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        
    return True

number = st.number_input(label="Select a prime number", min_value=2)
if is_prime(number):
    st.write("Prime")
else:
    st.write("Not Prime")