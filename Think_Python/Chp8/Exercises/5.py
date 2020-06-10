# Assign to a variable in your program a triple-quoted string that contains your favourite paragraph of text —
# perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.
# Write a function which removes all punctuation  from the string, breaks the string into a list of words, and counts
# the number of words in your text that contain the letter “e”. Your program should print an analysis of the text like
# this
# Your text contains 243 words, of which 109 (44.8%) contain an "e".

def remove_punctuation(p):
    lows = "abcedefghijklmnopqrstuvwxyz"
    ups = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    count_e = 0
    total_chars = 0
    for char in p:
        if char in lows or char in ups:
            total_chars = total_chars + 1
            if char == "e":
                count_e += 1
    percent_e = (count_e/total_chars) * 100
    print("Your text contains",total_chars,"alphabetic characters of w hich",count_e, "(",percent_e,"%)", "are 'e.'")




paragraph = """Howard Roark, a stern-faced young man, stands naked at the edge of a granite cliff. The year is
1922 and Roark has just been expelled from architecture school at the Stanton Institute of Technology. Although
Roark excels in engineering and mathematics, he is an individualist whose modern designs run contrary to everything
his school teaches. After serenely contemplating his future, Roark returns to his room in a local boardinghouse to
work on his drawings. His designs seem severe and simple, but the structures are actually complex. Roark forgets
that he has a meeting with the Dean of the college until his landlady, Mrs. Keating, whose son Peter is also a
student at the architecture school, reminds him. Roark goes to see the Dean.
The Dean says that Roark was expelled for turning in overly modern designs. The Dean assures Roark that he may be
able to return to the school once he has matured. Roark refuses the offer. The Dean is offended and informs Roark
that he will never become a real architect. Roark leaves the Dean’s office and thinks about how he does not
understand men like the Dean"""

remove_punctuation(paragraph)
