import os

industries = ["Software Engineering", "UX Design", "Web Development", "Literature", "Art", "Music", "Film", "Photography", "Architecture", "Interior Design", "Graphic Design", "Fashion", "Product Design", "Industrial Design", "Game Design", "Animation", "Videography", "Journalism", "Advertising", "Marketing", "Public Relations", "Business", "Economics", "Finance", "Law", "Politics", "Psychology", "Sociology", "History", "Philosophy", "Religion", "Education", "Medicine", "Health", "Nutrition", "Fitness", "Sports", "Travel", "Food", "Cooking", "Crafts", "Home Improvement", "Gardening", "Pets", "Parenting", "Beauty", "Lifestyle", "Science", "Technology", "Mathematics", "Engineering", "Astronomy", "Chemistry", "Physics", "Biology", "Computer Science", "Data Science", "Robotics", "Entrepreneurship", "Personal Development", "Productivity", "Self Improvement", "Career Development", "Hobbies", "Languages", "Other"]

industries = sorted(industries)
industries = [industry.lower().replace(" ", "_") for industry in industries]

def generate_readme(industries, readme_file):
    with open(readme_file, "w") as f:

        f.write("# chatGPT Prompts For Everyone! *Domain Agnostic Prompts for Savvy Professionals* \n## Industries List\n\n")
        for industry in industries:
            f.write(f"- [{industry}](./industries/{industry}.md)\n")

# generate readme
#!generate_readme(industries, "README.md")

# create a folder for all of the industries
#// os.remove("industries")
#!os.mkdir("industries")

for industry in industries:
    if not os.path.exists(f"./industries/{industry}.md"):
        with open(f"./industries/{industry}.md", "w") as f:
            f.write(f"# {str(industry).capitalize()}\n")


subfiles = ["JavaScript", "Python", "C#", "Java", "C++", "C", "Ruby", "Swift", "PHP", "Go", "Rust", "Kotlin", "TypeScript",
            "R", "Scala", "Perl", "Shell", "Objective-C", "SQL", "Excel Formulas", "Visio", "VBA", "Power BI", "SAS",
            "Tableau", "QlikView", "D3.js", "Data Visualization", "Data Analysis", "Machine Learning", "Deep Learning",
            "Computer Vision", "Natural Language Processing", "Data Science", "Big Data", "Data Engineering", "DevOps",
            "Cloud Computing", "Docker", "Kubernetes", "AWS", "Azure", "Google Cloud", "Linux", "Windows", "macOS",
            "iOS", "Android", "Pointers in Computer Science", "Algorithms", "Data Structures", "Operating Systems",
            "Networking", "Security", "Cryptography", "Blockchain", "IoT", "AR/VR", "Computer Graphics", "Computer Architecture",
            "Compilers", "Assembler", "Debugging", "Testing", "Agile", "Scrum", "Kanban", "Lean", "Waterfall", "PMP",
            "PRINCE2", "ITIL", "COBIT", "TOGAF", "SOA", "Microservices", "Monolithic", "Functional Programming",
            "Object-Oriented Programming", "Procedural Programming", "Event-Driven Programming", "Concurrent Programming",
            "Distributed Systems", "Parallel Computing", "High-Performance Computing", "Embedded Systems", "Firmware",
            "Low-Level Programming", "Real-Time Systems"]

subfiles = sorted(subfiles)
subfiles = [sub.replace(" ", "_").replace('.','_').replace('/','').lower() for sub in subfiles]


def generate_readme_topics(industries, readme_file, subfiles):
    # Create the specific_topics folder if it doesn't already exist
    if not os.path.exists("specific_topics"):
        os.makedirs("specific_topics")
    with open(readme_file, "w") as f:
        f.write("# Industry List\n")
        for industry in industries:
            # Create subfiles for each programming language and technical program
            for subfile in subfiles:
                subfile_path = os.path.join("specific_topics", f"{subfile}.md")
                with open(subfile_path, "w") as sf:
                    sf.write(f"# {industry} - {subfile}\n")
            f.write(f"- [{industry}](./{industry}.md)\n")

generate_readme_topics(industries, "specific_topics/specific_topics_directory.md", subfiles)