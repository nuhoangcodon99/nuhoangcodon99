import requests
from datetime import datetime

# Đường dẫn đến file README.md
file_path = 'README.md'

# Lấy GitHub username
github_username = 'nuhoangcodon99'

# Lấy dữ liệu GitHub Stats
github_stats = f"![GitHub Stats](https://github-readme-stats.vercel.app/api?username={github_username}&show_icons=true&theme=radical)"

# Lấy dữ liệu GitHub Trophies
github_trophies = f"![GitHub Trophies](https://github-profile-trophy.vercel.app/?username={github_username}&theme=radical)"

# Đọc nội dung của README.md
with open(file_path, 'r', encoding='utf-8') as file:
    readme_content = file.read()

# Cập nhật GitHub Stats
new_readme_content = readme_content
stats_start = new_readme_content.find("![GitHub Stats](")
stats_end = new_readme_content.find(")", stats_start) + 1

if stats_start != -1 and stats_end != -1:
    new_readme_content = new_readme_content[:stats_start] + github_stats + new_readme_content[stats_end:]

# Cập nhật GitHub Trophies
trophies_start = new_readme_content.find("![GitHub Trophies](")
trophies_end = new_readme_content.find(")", trophies_start) + 1

if trophies_start != -1 and trophies_end != -1:
    new_readme_content = new_readme_content[:trophies_start] + github_trophies + new_readme_content[trophies_end:]

# Ghi lại vào README.md
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(new_readme_content)
