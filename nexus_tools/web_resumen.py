from bs4 import BeautifulSoup as bs #type: ignore
import requests

def web_resumen(url):
    try:
        headers = {'User-Agent': "Mozilla/5.0...", "Accept-Language": "es-ES,es;q=0.9"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = bs(response.text, 'html.parser')

        tag_h1 = soup.find('h1')

        if tag_h1:
            title = tag_h1.get_text().strip()
        else:
            title = "Sin título" #si no hay h1

        paginaCompleta = soup.find('div', {'class': "mw-content-ltr mw-parser-output"})
        
        if paginaCompleta:
            lista_parrafos = paginaCompleta.find_all('p') 
            text = ''
            parrafos = 0
            
            for p in lista_parrafos:
                textoLimpio = p.get_text().strip()
                
                if len(textoLimpio) > 20:
                    text += textoLimpio + '\n\n'
                    parrafos += 1

                if parrafos == 3:
                    break

        else:
            text = "No se pudo localizar el contenido principal."

        return {
            'title': title,
            'text': text
        }
    
    except Exception as e:
        return {'error': f'Error al procesar la web: {str(e)}'}