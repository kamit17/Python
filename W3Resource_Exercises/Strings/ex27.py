#Write a Python program to remove existing indentation from all of the lines in a given text.
import textwrap
sample_text = '''
        The textwrap module can be used to format text for output in situations
        where pretty-printing is desired.  It offers programmatic functionality similar
        to the paragraph wrapping or filling features found in many text editors.
        '''
dedented_text = textwrap.dedent(sample_text).strip()

print("Dedented:\n")
print (dedented_text)
