#Write a Python program to add a prefix text to all of the lines in a string.
import textwrap
sample_text = '''
        The textwrap module can be used to format text for output in situations
        where pretty-printing is desired.  It offers programmatic functionality similar
        to the paragraph wrapping or filling features found in many text editors.
        '''
dedented_text = textwrap.dedent(sample_text).strip()
wrapped = textwrap.fill(dedented_text,width=50)
final_result = textwrap.indent(wrapped,'!#')
print()
print(final_result)
print()
