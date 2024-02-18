import os, xml.etree.ElementTree as ET

# Folder path
folderXML_path = 'dados/texto/'

# List all files in the folder
filesXML = os.listdir(folderXML_path)

# Sort the files alphabetically
filesXML.sort()


preHTML = """
<!DOCTYPE html>
<html>
<style>
.w3-theme-braga {
color:#fff !important;background-color:#005097 !important}
</style>
<body>
    <head>
        <title>Ruas de Braga</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="w3.css">
        <meta charset="utf-8"/>
    </head>
    <body>
        <header class="w3-container w3-theme-braga">
            <h3>Ruas de Braga </h3>
        </header>
        <div class="w3-container">
"""

posHTML = """
                </table>
        </div>
        <footer class="w3-container w3-theme-braga">
            <h5>Generated by RDBApp::EngWeb2024::a93323</h5>
        </footer>            
    </body>
</body>
</html> 
"""


conteudo = f"""
                <table class="w3-table w3-striped" style="width: 500px;">
                    <tr>
                        <th>Nome</th>
                        <th class="w3-center">Número</th>
                    </tr>
        """



# Define the directory path
fotos_path = "./dados/atual/"

# Initialize an empty dictionary to store the filenames
fotos_dict = {}

# Iterate over the files in the directory
for filename in os.listdir(fotos_path):

    vista = filename.rsplit("-",1)[1].split(".",1)[0]
    
    # Get the part before the first "-"
    if vista == "Vista1":
        key = filename.split("-",1)[0]
        fotos_dict[key] = os.path.join("../",fotos_path, filename)



# Iterate over each file
for fileXML_name in filesXML:
    # Construct the full path to the file
    fileXML_path = os.path.join(folderXML_path, fileXML_name)
    
    # Check if the item in the folder is a file (not a subdirectory)
    if os.path.isfile(fileXML_path):
       # Load the XML file
        tree = ET.parse(fileXML_path)
        root = tree.getroot()
        # Find the 'meta' element
        meta_element = root.find('meta')
        if meta_element is not None:
            nomeRua = meta_element.find("nome").text
            numeroRua = meta_element.find("número").text
            conteudo += f"""
                                <tr>
                                    <td>
                                        <div class="w3-dropdown-hover">
                                            <a href="{nomeRua.lower().replace(" ","")}.html">
                                                {nomeRua}
                                            </a>
                                            <div class="w3-dropdown-content w3-card-4" style="width:250px">
                                                <img src="{fotos_dict[numeroRua]}" style="width:100%">
                                            </div>
                                        </div>
                                    </td>
                                    <td class="w3-center">
                                        {numeroRua}
                                    </td>
                                </tr>
        """
            

pagHTML = preHTML + conteudo + posHTML
f = open("ruas_site/index.html", "w")
f.write(pagHTML)
f.close()