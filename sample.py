#encoding: iso-8859-1
from languess import Languess
from glob import glob

def main():
    # create the object, then load all the knowledge
    lg = Languess()
    klm = {}
    for lm in glob('knowledge/*.lm'):
        klm[ lm[10:-3] ] = [n.strip() for n in open(lm).readlines()]
    lg.load_knowledge( klm  )

    # English
    print lg.getLang("This is just a bloody text")
    # Spanish
    print lg.getLang("Pues esto es un texto en español")
    # Guarani
    print lg.getLang("Mba'eteko chera'a mba'eichapa reiko?")
    # I just know those three langs, sorry ;)
    # Polish
    print lg.getLang("zdobyła srebrny medal poprawiając swoim wynikiem rekord")
    #Lithuanian
    print lg.getLang(" konstitucijos straipsnis dėl SSKP vadovaujančio vaidmens valstybėje. Politinės sistemos demokratizavimas")

if __name__ == "__main__":
    main()
