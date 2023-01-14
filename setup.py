import os

industries = ["Software Engineering", "UX Design", "Web Development", "Literature", "Art", "Music", "Film", "Photography", "Architecture", "Interior Design", "Graphic Design", "Fashion", "Product Design", "Industrial Design", "Game Design", "Animation", "Videography", "Journalism", "Advertising", "Marketing", "Public Relations", "Business", "Economics", "Finance", "Law", "Politics", "Psychology", "Sociology", "History", "Philosophy", "Religion", "Education", "Medicine", "Health", "Nutrition", "Fitness", "Sports", "Travel", "Food", "Cooking", "Crafts", "Home Improvement", "Gardening", "Pets", "Parenting", "Beauty", "Lifestyle", "Science", "Technology", "Mathematics", "Engineering", "Astronomy", "Chemistry", "Physics", "Biology", "Computer Science", "Data Science", "Robotics", "Entrepreneurship", "Personal Development", "Productivity", "Self Improvement", "Career Development", "Hobbies", "Languages", "Other"]


def generate_readme(industries, readme_file):
    with open(readme_file, "w") as f:

        f.write("# chatGPT Prompts For Everyone! *Domain Agnostic Prompts for Savvy Professionals* \n## Industries List\n\n")

        for industry in industries:
            f.write(f"- [{industry}](./{industry}.md)\n")

# generate readme
generate_readme(industries, "README.md")

for industry in industries:
    with open(f"{industry}.md", "w") as f:
        f.write(f"# {industry}\n")