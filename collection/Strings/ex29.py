#Python: Set the indentation of the first line
import textwrap

from ex28 import sample_text

dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text,initial_indent='',subsequent_indent= "  "))
