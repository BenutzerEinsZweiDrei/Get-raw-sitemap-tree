import json

## get main.json from https://api.github.com/repos/[user]/[repo-name]/git/trees/[branch]?recursive=1


# config

path = "https://raw.githubusercontent.com/[user]/[repo-name]/[branch]/"


def save_txt_to_md(txt, filename):
	
	# open file to overwrite content
	f = open(filename + ".md", "w")
	f.write(txt)
	f.close()

def load_file_as_dict(name):
	     #open and read the file
	     # ressources to X
	f = open(name, "r")
	temp = f.read()
	tab = json.loads(temp)
	# return
	return tab

main = load_file_as_dict("main.json")
txt = "# Repo Tree<br><br>\n\n"


for item in main["tree"]:
	# check if item is file
	if item["type"] == "blob":
		## add name and url to txt
		txt = txt + "<br>\n"
		txt = txt + "## " + item["path"] + "<br>\n"
		# create url
		txt = txt + path + item["path"] + "<br>\n"
		


# save it at the end
save_txt_to_md(txt, "tree")