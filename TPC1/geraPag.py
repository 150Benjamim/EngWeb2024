import os, xml.etree.ElementTree as ET

# Define the folder path
folderXML_path = 'dados/texto/'

# List all files in the folder
filesXML = os.listdir(folderXML_path)


# Define the directory path
fotos_path = "dados/atual/"

# Initialize an empty dictionary to store the filenames
fotosAtual_dict = {}

# Iterate over the files in the directory
for filename in os.listdir(fotos_path):

    key = filename.split("-", 1)[0]

    # If key doesn't exist in dictionary, create a new entry with an empty list
    if key not in fotosAtual_dict:
        fotosAtual_dict[key] = []
    
    # Append the filename to the list corresponding to the key
    fotosAtual_dict[key].append(os.path.join("../",fotos_path, filename))
    fotosAtual_dict[key].sort()


def create_preHTML(nomeRua):
   return f"""
   <!DOCTYPE html>
    <html>
    <style>
    .w3-theme-braga {'{'}
    color:#fff !important;background-color:#005097 !important{'}'}"
    </style>
    <body>
        <head>
            <title>{nomeRua}</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="w3.css">
            <meta charset="utf-8"/>
        </head>
        <body>
            <header class="w3-container w3-theme-braga">
                <h3>{nomeRua}</h3>
            </header>
    """

def create_postHTML():
    return """  
        </body>
    </body>
    </html> 
    """

def formatText(text_element):
    if text_element is not None:
        for elem in text_element.findall('*'):
                if elem.tag=='lugar':
                    elem.tag = 'b'
                elif elem.tag=='data':
                    elem.tag = 'span style="color:red"'
                else:
                    elem.tag = 'span style="color:blue"'
        return ET.tostring(text_element,encoding='unicode')
    else:
        return ''



# Iterate through each XML file
for fileXML in filesXML:

    # Parse the XML file
    tree = ET.parse(os.path.join(folderXML_path, fileXML))
    root = tree.getroot()

    meta_element = root.find("meta")

    nomeRua = meta_element.find("nome").text
    numeroRua = meta_element.find("número").text


    preHTML = create_preHTML(nomeRua)
    
    posHTML = create_postHTML()

    conteudo = ''

    # fotos atuais
    conteudo += """
                <div class="w3-row-padding w3-margin-top">
    """

    for fotoAtual in fotosAtual_dict.get(numeroRua):
        conteudo += f"""
                    <div class="w3-half w3-center">
                        <img src={fotoAtual} style="width=100%;max-height:600px">
                    </div>
        """

    conteudo += "</div>"

    # figuras
    conteudo += """
                <div class="w3-row-padding w3-margin-top">
    """

    for figura in root.findall('corpo/figura'):
        imagem_path = "../dados/" + figura.find('imagem').get('path').split("/",1)[1]
        legenda = figura.find('legenda').text
        conteudo += f"""
                    <div class="w3-half w3-center">
                        <img src={imagem_path} style="height:200px">
                        <div class="w3-container w3-center">
                            <p>{legenda}</p>
                        </div>
                    </div>
        """

    conteudo += "</div>"

    # descricao da rua
    conteudo += """
                <div class="w3-container w3-border w3-large">
    """
    for para in root.findall('corpo/para'):
        conteudo += f"<p>{formatText(para)}</p>"

    conteudo += "</div>"


    # lista de casas
    conteudo += f"""<div>
                        <table class="w3-table-all">
                            <tr>
                                <th>Número</th>
                                <th>Vista</th>
                                <th>Enfiteuta</th>
                                <th>Foro</th>
                                <th>Descrição</th>
                            </tr>
    """

    for casa in root.findall('corpo/lista-casas/casa'):
        numero = casa.find('número').text
        vista_element = casa.find("vista")
        vista = vista_element.text if vista_element is not None and vista_element.text else ''
        enfiteuta_element = casa.find('enfiteuta')
        enfiteuta = enfiteuta_element.text if enfiteuta_element is not None and enfiteuta_element.text else ''
        foro_element = casa.find('foro')
        foro = foro_element.text if foro_element is not None and foro_element.text else ''
        desc = casa.find('desc/para')
        desc_conteudo = formatText(desc)
        conteudo += f'''
                    <tr>
                        <td>{numero}</td>
                        <td>{vista}</td>
                        <td>{enfiteuta}</td>
                        <td>{foro}</td>
                        <td>{desc_conteudo}</td>
                    </tr>
    '''
        
    conteudo += f"""
                    </table>
                </div>
    """



    pagHTML = preHTML + conteudo + posHTML
    fds = "ruas_site/" + nomeRua.lower().replace(" ","") + ".html"
    f = open(fds,"w")
    f.write(pagHTML)
    f.close()


