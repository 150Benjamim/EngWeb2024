import os, json


# Gera Index

preHTML = """
<!DOCTYPE html>
<html>
<style>
.w3-theme-portugal {
color:#fff !important;background-color:#da291c !important}
</style>
<body>
    <head>
        <title>Mapa Virtual</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="w3.css">
        <meta charset="utf-8"/>
    </head>
    <body>
        <header class="w3-container w3-theme-portugal">
            <h3>Mapa Virtual</h3>
        </header>
"""

postHTML = """
        <footer class="w3-container w3-theme-portugal">
            <h5>Generated by RDBApp::EngWeb2024::a93323</h5>
        </footer>            
    </body>
</body>
</html> 
"""


# Load the JSON file
with open('mapa-virtual.json', 'r') as f:
    data = json.load(f)

# Sort the list of cities by name
sorted_cidades = sorted(data['cidades'], key=lambda x: x['nome'])

# Generate HTML for the sorted list
conteudo = "<ul class='w3-ul w3-border'>"
for cidade in sorted_cidades:
    conteudo += f"<li><a href='http://localhost:7777/{cidade['id']}'>{cidade['nome']}</a></li>"
conteudo += "</ul>"


pagHTML = preHTML + conteudo + postHTML
f = open("mapa_site/index.html", "w")
f.write(pagHTML)
f.close()





# Gera Páginas

city_id_to_name = {cidade['id']: cidade['nome'] for cidade in data['cidades']}

# Iterate over each city
for cidade in data['cidades']:
    nome = cidade['nome']
    id_cidade = cidade['id']
    # Generate HTML content for the city
    preHTML = f"""
    <!DOCTYPE html>
    <html>
    <style>
    .w3-theme-portugal{'{'}
    color:#fff !important;background-color:#da291c !important{'}'}"
    </style>
    <body>
        <head>
            <title>{nome}</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="w3.css">
            <meta charset="utf-8"/>
        </head>
        <body>
            <header class="w3-container w3-theme-portugal">
                <h3>{nome}</h3>
            </header>
    """

    conteudo = f"""
            <div class="w3-container">    
                <p><b>População:</b> {cidade['população']}</p>
                <p><b>Descrição:</b> {cidade['descrição']}</p>
                <p><b>Distrito:</b> {cidade['distrito']}</p>
                <table class="w3-table-all" style="width:500px">
                    <tr>
                        <th>Ligação</th>
                        <th class="w3-center">Distância (KM)</th>
    """

    postHTML = """  
                </table>
            </div>
        </body>
    </body>
    </html> 
    """

    # Iterate over the connections of the current city
    connections = set()
    for connection in data['ligacoes']:
        if connection['destino'] == id_cidade:
            connections.add((connection['origem'],connection['distância']))
        elif connection['origem'] == id_cidade:
            connections.add((connection['destino'],connection['distância']))
    connections_sorted = sorted(connections, key=lambda x: city_id_to_name.get(x[0], ''))
    for ligacao,distancia in connections_sorted:
        destino_nome = city_id_to_name.get(ligacao, 'Desconhecido')
        conteudo += f"""
                    <tr>
                        <td> <a href='http://localhost:7777/{ligacao}'>{destino_nome} </td>
                        <td class="w3-center"> {distancia} <td>
                    </tr>
            """
    

    pagHTML = preHTML + conteudo + postHTML

    # Write the HTML content to a file
    filename = f"mapa_site/{id_cidade}.html"  # Create a filename based on city name
    with open(filename, 'w') as city_file:
        pagHTML = preHTML + conteudo + postHTML
        city_file.write(pagHTML)