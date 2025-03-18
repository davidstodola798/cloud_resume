import markdown

with open("resume.md", "r", encoding="utf-8") as md_file:
    md_content = md_file.read()

html_content = markdown.markdown(md_content)

html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>David Stodola - Resume</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
        max-width: 800px;
        margin: 40px auto;
        padding: 20px;
        line-height: 1.6;
        background-color: #f4f4f4;
        }}

        h1 {{
    color: #003366;
    font-size: 2.5em;
        }}
        h2 {{
    color: #b22222; 
    font-size: 1.8em;
        }}

        a {{
            color: #0078D7;
            text-decoration: none;
        }}

        a:hover {{
            color: #b22222;
            text-decoration: underline;
        }}

        .container {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }}

        ul li {{
            margin-bottom: 10px;
        }}

        h1, h2, p {{
            margin-bottom: 10px;
        }}

        hr {{
            border: 1px solid #0078D7; /* Blue separator line */
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""

with open("resume.html", "w", encoding="utf-8") as html_file:
    html_file.write(html_template)

