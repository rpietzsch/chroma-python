import grapefruit
import rdflib
import hashlib
import sys

def colorsforConcepts(iri):
    colors = []
    g = rdflib.Graph()
    g.parse(iri)
    m = hashlib.md5()

    concepts_query = """
    SELECT DISTINCT ?concept
    WHERE {
        ?concept a ?something .
    }
    """

    qres = g.query(concepts_query)
    for row in qres:
        m.update(str(row.concept).encode('utf-8'))
        int_digets = int.from_bytes(m.digest(), sys.byteorder)
        h = ((0xFF000 & int_digets) % 360)  # H - hue / color -> 0-360°, we want anything
        s = ((((0xFF00 & int_digets) % 50) + 50) / 100)  # S - saturation -> 0-100%, we want 50-100%
        bl = ((((0xFF & int_digets) % 25) + 50) / 100)  # B/L - brightness/lightness -> 0-100%, we want 50-75%
        c = grapefruit.Color.NewFromHsl(h, s, bl)
        colors.append({"rgb": c.html, "concept": str(row.concept), "color_html": str(c.html), "color_hsl": str(c.hsl)})


    #L = ( ( ( 0xFF000 & hash_iri ) % 45 ) + 25 ) # valid values between 0 and 100, we only want between 25 (dark) and 70
    #a = ( ( ( 0xFF00 & hash_iri ) % 0xFF ) - 128 ) # values between -128 and 127
    #b = ( ( 0xFF & hash_iri ) - 128 ) # values between -128 and 127
    #print(f"L a b: {str(L)} {str(a)} {str(b)})

    return colors

iri = "http://www.w3.org/2002/07/owl#"
colors = colorsforConcepts(iri)
print (colors)
