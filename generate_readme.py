import random
import markdown
import black
from tqdm import tqdm

def combine_readme(top, middle, bottom):
    # Create dynamic badges for middle section
    badges = []
    # the files in the specific_topics folder are the topics
    badge_count = len(os.listdir("specific_topics"))
    for i in tqdm(range(badge_count)):
        badge_color = random.choice(["green", "orange", "red", "blue", "yellow", "pink", "purple", "grey", "blue", "blueviolet","brown", "darkgrey", "lightgreen", "darkgreen", "lightblue", "darkblue", "lightyellow", "darkyellow", "lightpink", "darkpink", "lightpurple", "darkpurple", "lightbrown", "darkbrown", "lightblack", "darkblack", "lightwhite", "darkwhite", "lightred", "darkred", "lightorange", "darkorange"])
        badge_text = f"Badge_{i + 1}"
        # get the name of the file
        badge_filename = os.listdir("specific_topics")[i] # get the name of the file
        badge_text = badge_filename.replace(".md", "") # remove the .md extension
        badge_text_two = badge_text.replace(" ", "_") # replace spaces with underscores
        badge_link = f"./specific_topics/{badge_text_two}.md"
        while ' ' in badge_text:
            badge_text = badge_text.replace(' ', '_')
        badge = f"[![{badge_text}](https://img.shields.io/badge/{badge_text}-{badge_color})]({badge_link})"
        badges.append(badge)
    # Concatenate top, middle, and bottom sections
    combined_readme = top + "\n\n" + "\n".join(badges) + "\n\n" + bottom
    return combined_readme


# Read in the top, middle, and bottom sections of the README
with open("docs/section_1.md", "r") as file:
    top = file.read()
    # Write the section to the top of the readme
    with open("README.md", "w") as file:
        file.write(top)

with open("docs/section_2.md", "r") as file:
    middle = file.read()
    # Convert to HTML
    middle = mistune.markdown(middle)
    # write the section to the bottom of the readme
    with open("README.md", "a") as file:
        file.write(middle)


with open("docs/section_3.md", "r") as file:
    bottom = file.read()
    # Format with black
    #bottom = black.format_str(bottom, mode=black.FileMode())
    # write the section to the bottom of the readme
    with open("README.md", "a") as file:
        file.write(bottom)

# Combine the sections
combined_readme = combine_readme(top, middle, bottom)

# Write the combined README to the root directory
with open("README.md", "w") as file:
    file.write(combined_readme)
