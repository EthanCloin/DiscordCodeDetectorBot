from guesslang import Guess
import streamlit as st


def guess_test(code_string: str):
    guess = Guess()
    return guess.language_name(code_string)


if __name__ == "__main__":
    # client.run(TOKEN)
    pass

code = st.text_area("Code")
if st.button("TRY"):
    language = guess_test(code)
    st.success(language)
