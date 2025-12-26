import pathlib

# 1. Define the folder name (local to your script)
folder_path = pathlib.Path("./dnslogs")

# 2. Create the directory if it doesn't exist
folder_path.mkdir(exist_ok=True)

# 3. Define some dummy log content
# I included data from your screenshot, PLUS the IP 8.9.74.225
# so your script has something to find!
log_content_1 = """
01-Apr-2015 09:59:55.025 client 251.92.84.43#59338: query: u-ads.adap.tv IN A + ((8.8.8.8))
01-Apr-2015 09:59:55.189 client 8.9.74.225#51628: query: www.google.com IN A + ((8.8.8.8))
01-Apr-2015 09:59:55.315 client 162.85.35.54#52755: query: ping3.teamviewer.com IN A + ((8.8.8.8))
"""

log_content_2 = """
01-Apr-2015 10:00:01.000 client 8.9.74.225#52755: query: www.amazon.com IN A + ((8.8.8.8))
01-Apr-2015 10:00:02.000 client 135.130.71.166#51628: query: vpc.altitude-arena.com IN A + ((8.8.8.8))
"""

# 4. Write the files
(folder_path / "log1.txt").write_text(log_content_1)
(folder_path / "log2.txt").write_text(log_content_2)

print("Success! Created folder 'dnslogs' with 2 dummy files.")