import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    "Android developer, web builder, and DSA grinder. Currently pursuing B.Tech Computer Science Engineering at Lovely Professional University, Punjab. Shipping real projects and solving problems daily.": "Currently pursuing a B.Tech in Computer Science and Engineering at Lovely Professional University, Punjab. I enjoy building Android apps, websites, and practicing data structures and algorithms.",

    "<p>I am <strong>Singamreddy Tarakeswar Reddy</strong>, a Computer Science and Engineering student at Lovely Professional University, Punjab. I build things that work — Android apps, REST APIs, data analysis tools, web platforms, and OS-level visualizers.</p>": "<p>I am <strong>Singamreddy Tarakeswar Reddy</strong>, a Computer Science and Engineering student at Lovely Professional University, Punjab. I enjoy building a variety of software—from Android apps and web platforms to data visualization tools.</p>",

    "<p>My approach is simple: <strong>learn deeply, build persistently, ship consistently.</strong> I practice DSA on LeetCode every single day and commit every breakthrough to GitHub. Every project I take on has a real purpose behind it — from helping road safety authorities detect accident hotspots, to making task management smarter with algorithms.</p>": "<p>I focus a lot on problem-solving and solving DSA questions on LeetCode every day. I always try to tie my learning into practical projects, like finding ways to organize data more efficiently or analyzing road accident datasets to spot trends.</p>",

    "<p>Beyond technical skills, I actively contribute to social causes through NGO work, where I apply my <strong>leadership and communication skills</strong> in community settings. I believe strong engineers are not just great at code — they are great at impact.</p>": "<p>Outside of coding, I volunteer with local NGOs. Teaching kids and mentoring students has taught me public speaking, leadership, and how to effectively communicate technical concepts to beginners.</p>",

    "<p>I am actively seeking <strong>internship and entry-level software engineering roles</strong> where I can bring fresh energy, deep algorithmic thinking, and a proven ability to ship projects from zero to deployed.</p>": "<p>I am looking for <strong>internships and entry-level software engineering roles</strong> where I can keep learning, contribute to real-world projects, and grow as a developer.</p>",

    "Completed intermediate education with a strong focus on Mathematics and Sciences. This foundation in analytical thinking and problem decomposition directly shaped my approach to programming and algorithm design.": "Completed intermediate education with a strong focus on Mathematics, Physics, and Chemistry.",

    "Completed schooling in Nellore where curiosity in computers and mathematics first sparked. Early exposure to logical thinking and structured learning laid the groundwork for a career in engineering.": "Completed my primary and secondary schooling in Nellore, where I initially discovered my interest in mathematics and computers.",

    "Daily DSA practice documented on GitHub. Every new concept, pattern, and solved problem is committed and tracked — a living record of algorithmic growth.": "I maintain a daily DSA practice and document my progress on GitHub, pushing all my code and notes.",

    "<li>Clean Git commit history throughout</li>": "<li>Maintained version control with Git</li>",

    "Volunteered as a teacher with Pragathi Charities across two impactful programs — bringing computer literacy to students who otherwise had no access to it.": "Volunteered as a teacher with Pragathi Charities across two programs, helping students gain basic computer literacy.",

    "Taught foundational computer skills to students from Class 1 through Class 10. Covered hardware basics, operating system usage, typing, internet safety, and introductory software tools. Made complex concepts accessible and fun for young learners at every level.": "Taught computer skills to students from Class 1 to 10. Topics included hardware basics, typing, and how to browse the internet safely.",

    "Mentored students on IIT JEE preparation — explaining the exam structure, study strategies, subject importance, and how to plan their academic journey. Motivated students from underserved backgrounds to believe in and pursue top engineering institutions.": "Guided students on competitive exam preparation, going over study strategies and how to plan their subjects effectively.",

    "This experience sharpened the ability to break down hard concepts into digestible ideas — a skill that directly improves code documentation, technical communication, and team collaboration.": "This teaching experience helped me improve my communication skills and my ability to explain technical concepts simply.",

    "<strong>DSA Problems Solved</strong> across LeetCode and GeeksforGeeks, with daily LeetCode practice maintained consistently — building the algorithmic sharpness that powers every project I build.": "<strong>DSA Problems Solved</strong> across LeetCode and GeeksforGeeks. Practicing consistently has helped me improve my logic and problem-solving skills."
}

for old_val, new_val in replacements.items():
    html = html.replace(old_val, new_val)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
