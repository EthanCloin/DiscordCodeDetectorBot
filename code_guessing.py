from guesslang import Guess
import streamlit as st


def guess_test(code_string: str):
    guess = Guess()
    return guess.language_name(code_string)


if __name__ == "__main__":
    # client.run(TOKEN)
    test_result = guess_test(
        """
    print("Hello World!") 
    """
    )
    print(test_result)

code = st.text_input("Code")
if st.button("TRY"):
    guess_test(code)
