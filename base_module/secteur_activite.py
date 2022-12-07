import  re
def get_domaine(nom):
    nom = str(nom).lower().replace("é", "e").replace("è", "e").replace("ê", "e").replace("ô", "o").replace("â",
                                                                                                           "a").replace(
        "/", " ")

    # 1 Eaux, Assainissement, Hygiene et Environnement
    if re.search("^societe.*nationale.*eaux.*", nom) or \
            re.search("^office.*national.*assainissement.*", nom) or \
            re.search("^service.*regional.*assainissement.*", nom) or \
            re.search("^service regional de$", nom) or \
            re.search(".*office.*forage.*rurau.*", nom) or \
            re.search(".*office.*lac.*cours.*eau.*", nom) or \
            re.search(".*office.*lac.*guiers.*", nom) or \
            re.search("^projet.*restauration.*fonction.*ecologique.*economique.*lac.*guiers.*", nom) or \
            re.search("^sones$", nom) or \
            re.search("^onas.*", nom) or \
            re.search("^olac.*", nom) or \
            re.search("^olag$", nom) or \
            re.search("^o.la.g$", nom) or \
            re.search("^prefelag$", nom) or \
            re.search("^progebe$", nom) or \
            re.search("^agence.*nationale.*grande.*muraille.*verte.*", nom) or \
            re.search("^agence.*reforestation.*grande.*muraille.*verte.*", nom) or \
            re.search("^agence.*promotion.*reseau.*hydrographique.*", nom) or \
            re.search("^ministere.*ecologie.*protection.*nature.*", nom) or \
            re.search("^ministere.*hydraulique.*", nom) or \
            re.search("^ministere.*environnement.*", nom) or \
            re.search("^ministere.*eau.*assainissement.*", nom) or \
            re.search("^ministere.*restructuration.*amenagement.*zone.*inondation.*", nom) or \
            re.search("^ministere.*bassin.*retention.*", nom) or \
            re.search("^agence.*nationale.*proprete.*senegal.*", nom) or \
            re.search("^institut.*hygiene.*sociale.*", nom) or \
            re.search("^ministere.*hygiene.*publique.*", nom) or \
            re.search("^entente.*cadak.*car.*", nom):
        return "Eaux, Assainissement, Hygiene et Environnement"

    # 2 Pétrole et Energies
    elif re.search(".*societe.*nationale.*electricite.", nom) or \
            re.search("^senelec$", nom) or \
            re.search("^commission.*regulation.*secteur.*electricite.*", nom) or \
            re.search("^agence.*electrification.*", nom) or \
            re.search("^agence.*energie.*renouvelable.*", nom) or \
            re.search("^agence.*economie.*maîtrise.*energie.*", nom) or \
            re.search("^petrosen$", nom) or \
            re.search("^ministere.*energie.*renouvelable.*", nom) or \
            re.search("^minsitere.*energie.*renouvelable.*", nom) or \
            re.search("^ministere.*de.*energie.*", nom) or \
            re.search("^ministere.*petrole.*energie.*", nom) or \
            re.search("^minsitere.*petrole.*energie.*", nom) or \
            re.search("^societe.*petrole.*senegal.*", nom) or \
            re.search("^petrosen.*", nom) or \
            re.search("^progede$", nom):
        return "Pétrole et Energies"

    # 3 Transports  Terrestres
    elif re.search(".*agence.*gestion.*route.*", nom) or \
            re.search(".*agence.*travaux.*routiers.*", nom) or \
            re.search(".*agence.*natio.*nouveau.*chemin.*fer.*", nom) or \
            re.search("^ministere.*transport.*terrestre.*", nom) or \
            re.search("^fond.*entretien.*routier.*", nom) or \
            re.search("^fond.*developpement.*transport.*terrestres.*", nom) or \
            re.search(".*conseil.*transport.*urbain.*", nom) or \
            re.search(".*petit.*train.*banlieue.*", nom) or \
            re.search("^societe.*nationale.*gestion.*patrimoine.*train.*express.*regional.*", nom) or \
            re.search("^aatr$", nom) or \
            re.search("^ageroute$", nom) or \
            re.search("^cetud$", nom) or \
            re.search("^cetud .*", nom) or \
            re.search(".*dem.*dikk.*", nom) or \
            re.search("^ministere.*infrastructure.*terrestre.*desenclavement.*", nom):
        return "Transports Terrestres"

    # 4 Transports Aériens et Météorologie
    elif re.search(".*agence.*aeroport.*senegal.*", nom) or \
            re.search(".*agence.*aviation.*civile.*", nom) or \
            re.search("^aeroport.*blaise.*diagne.*", nom) or \
            re.search("^haute.*autorite.*aeroport.*", nom) or \
            re.search("^aibd .*", nom) or \
            re.search("^aibd$", nom) or \
            re.search("^irap$", nom) or \
            re.search("^irap .*", nom) or \
            re.search("agence.*nationale.*meteorologie.*", nom):
        return "Transports Aériens et Météorologie"

        # 5 Santé
    elif re.search("^hopital.*", nom) or \
            re.search("^pharmacie.*", nom) or \
            re.search("^centre.*hospital.*", nom) or \
            re.search("^centre.*sanguine.*", nom) or \
            re.search("^region.*medical.*", nom) or \
            re.search("^district.*sanitaire.*", nom) or \
            re.search("^hospitalier.*regional.*", nom) or \
            re.search("^centre.*hopitalier.*", nom) or \
            re.search("^chr .*", nom) or \
            re.search("^chr/.*", nom) or \
            re.search("^chrtc$", nom) or \
            re.search("^chrz$", nom) or \
            re.search("^chn .*", nom) or \
            re.search("^eps .*", nom) or \
            re.search("^epsh .*", nom) or \
            re.search("^esph .*", nom) or \
            re.search("^epsm .*", nom) or \
            re.search("^etablissement.*public.*de.*sante.*", nom) or \
            re.search("^chnmf.*touba.*", nom) or \
            re.search(".*hopital.*dalal.*jamm.*", nom) or \
            re.search("^centre.*national.*appareillage.*orthopedie.*", nom) or \
            re.search("^agence.*ouverture.*maladie.*universelle.*", nom) or \
            re.search("^endss.*", nom) or \
            re.search("^service.*assistance.*medicale.*urgence.*", nom) or \
            re.search("^ministere.*de.*la.*sante.*", nom) or \
            re.search("^centre.*de .*sante .*", nom) or \
            re.search("^haa sy dabakh.*", nom) or \
            re.search("^haas$", nom):
        return "Santé"

    # 6 Péche
    elif re.search(".*port.*autonome.", nom) or \
            re.search("^pad$", nom) or \
            re.search("^agence.*nationale.*affaire.*maritime.*", nom) or \
            re.search("^anam$", nom) or \
            re.search("^ministere.*maritime.*", nom) or \
            re.search("^haute.*autorite.*chargee.*coordination.*securite.*martime.*", nom) or \
            re.search(".*direction.*ports.*maritime.*", nom) or \
            re.search("^sirn$", nom):
        return "Péche"

    # 7 Agriculture Elévage
    elif re.search("^institut.*senegalais.*recherches.*senegalais.*", nom) or \
            re.search("^isra.*", nom) or \
            re.search("^institut.*technologie.*alimentaire.*", nom) or \
            re.search("^ita *", nom) or \
            re.search("^ita$", nom) or \
            re.search("^institut.*national.*pedologie.*", nom) or \
            re.search("^inp$", nom) or \
            re.search("^societe.*developpement.*agricole.*industriel.*senegal.*", nom) or \
            re.search("^sodagri$", nom) or \
            re.search("^sodagri .*", nom) or \
            re.search("^societe.*amenagement.*exploitation.*terre.*delta.*", nom) or \
            re.search("^saed$", nom) or \
            re.search("^budget.*saed.*", nom) or \
            re.search("^pdesoc$", nom) or \
            re.search("^prodam$", nom) or \
            re.search("^programme.*national.*domaine.*agricole.*communautaire.*", nom) or \
            re.search("^ministere.*agriculture.*", nom) or \
            re.search("^ministere.*elevage.*", nom) or \
            re.search("^projet.*developpement.*inclusif.*durable.*agribusiness.*senegal.*", nom) or \
            re.search("^projet.*appui.*developpement.*rural.*casamance.*", nom) or \
            re.search("^projet.*appui.*filiere.*agricole.*", nom) or \
            re.search("^projet.*organisation.*villageaoise.*", nom) or \
            re.search("^projet.*developpement.*agricole.*", nom) or \
            re.search("^projet.agri.*jeune.*", nom) or \
            re.search("^agri.*jeune.*", nom) or \
            re.search(".*tekki.*ndawni.*", nom) or \
            re.search("^agence.*aquaculture.*", nom) or \
            re.search("^agence.*nationale.*insertion.*developpement.*agricole.*", nom) or \
            re.search("^haras.*national.*", nom) or \
            re.search("^fonds.*national.*developpementagro.*sylvo.*pastoral.*", nom) or \
            re.search("^padaer$", nom) or \
            re.search("^pdidas$", nom) or \
            re.search("^projet.*appui.*securite.*alimentaire.*", nom) or \
            re.search("^ministere de l’agricu.*", nom):
        return "Agriculture Elevage"

    # 8 Mairie commune
    elif re.search(".*mairie .*", nom) or \
            re.search("^conseil.*regional.*", nom) or \
            re.search("^conseil.*departemen.*", nom) or \
            re.search("^communaute.*rurale.*", nom) or \
            re.search("^ville.*de.*", nom) or \
            re.search("^cr .*", nom) or \
            re.search("^comune .*", nom) or \
            re.search("^commune .*", nom):
        return "Commune"

    # 9 Education et Recherche
    elif re.search("^ministere.*de.*education.*", nom) or \
            re.search("^ministere.*enseignement.*technique.*", nom) or \
            re.search("^ministere.*enseignement.*secondaire.*", nom) or \
            re.search("^ministere.*enseignement.*superieur.*", nom) or \
            re.search("^centre.*œuvre.*universitaire.*", nom) or \
            re.search("^universite .*", nom) or \
            re.search("^univerisite .*", nom) or \
            re.search("^univers8te .*", nom) or \
            re.search("^rectorat$", nom) or \
            re.search("^rectorat .*", nom) or \
            re.search("^ecole .*", nom) or \
            re.search("^ufr.*", nom) or \
            re.search("^uadb$", nom) or \
            re.search("^uad .*", nom) or \
            re.search("^ugb .*", nom) or \
            re.search("^ugb$", nom) or \
            re.search("^ept$", nom) or \
            re.search("^lycee.*", nom) or \
            re.search("^ia .*", nom) or \
            re.search("^i a matam.*", nom) or \
            re.search("^i. a saint-louis.*", nom) or \
            re.search("^inspect.*academi.*", nom) or \
            re.search("^inspection.*education.*", nom) or \
            re.search("^ief .*", nom) or \
            re.search("^institut.*national.*education.*formation.*jeune.*aveugle.*", nom) or \
            re.search("^inefja$", nom) or \
            re.search("^inefja .*", nom) or \
            re.search("^faculte.*medecine.*", nom) or \
            re.search("^faculte.*science.*", nom) or \
            re.search("^agence.*case.*tous.*petit.*", nom) or \
            re.search("^coud .*", nom) or \
            re.search("^coud$", nom) or \
            re.search("^centre.*regional.*oeuvres.*universitaire.*", nom) or \
            re.search("^crous .*", nom) or \
            re.search("^budget.*crous.*", nom) or \
            re.search("^crous$", nom) or \
            re.search("^prytane.*militaire.*saint.*louis.*", nom) or \
            re.search("^centre.*excellence.*africain.*mathematique.*informatique.*", nom) or \
            re.search("^centre.*polyvalent.*kaolack.*", nom) or \
            re.search("^centre.*experimental.*recherche.*etude.*equipement.*", nom) or \
            re.search("^cereeq$", nom) or \
            re.search("^institut.*fondamental.*afrique.*noire.*", nom) or \
            re.search("^agence.*nationale.*recherche.*scientifique.*applique.*", nom):
        return "Education et Recherche"

    # 10 Formation Professionnelle et Finnancement des Jeunes
    elif re.search("^office.*formation.*professionnel.*", nom) or \
            re.search("^ministere.*emploi.*insertion.*professionnelle.*main.*œuvre.*", nom) or \
            re.search("^ministere.*formation.*professionnel.*", nom) or \
            re.search("^ministere.*de.*la.*jeunesse.*", nom) or \
            re.search("^ministere.*jeunesse.*emploi.*", nom) or \
            re.search("^ministere.*jeunesse.*construction.*citoyenne.*", nom) or \
            re.search("^institut.*superieur.*professionnel.*", nom) or \
            re.search("^institut.*superieur.*professionel.*", nom) or \
            re.search("^centre.*formation.*professionnel.*", nom) or \
            re.search("^centre.*national.*qualification.*professionnel.*", nom) or \
            re.search("^centre.*polyvalent.*diourbel.*", nom) or \
            re.search("^agence.*maison.*outil.*", nom) or \
            re.search("^onfp$", nom) or \
            re.search("^cnqp$", nom) or \
            re.search("^cnqp .*", nom) or \
            re.search("^3fpt$", nom) or \
            re.search("^fonds.*financement.*formation.*professionnelle.*technique.*", nom) or \
            re.search("^agence.*nationale.*emploi.*jeune.*", nom) or \
            re.search("^isep .*", nom) or \
            re.search("^isep$", nom) or \
            re.search("^cfp .*", nom):
        return "Formation Professionnelle"

    # 11 Sécurite Intérieur
    elif re.search(".*ministere.*de.*interieur.*", nom) or \
            re.search("^agence.*assistance.*securite.*proximite.*", nom) or \
            re.search("^asp$", nom) or \
            re.search("^groupement.*mobile.*intervention.*", nom) or \
            re.search("^gmi$", nom) or \
            re.search("^gmi .*", nom) or \
            re.search("^god gmi.*", nom) or \
            re.search("^camp.*penal.*de.*", nom) or \
            re.search("^inspection.*administration.*penitenciaire.*", nom) or \
            re.search("^inspection.*administration.*penitenciere.*", nom) or \
            re.search("^maison.*arret.*", nom) or \
            re.search("^maison.*arrët.*", nom) or \
            re.search("^maison.*arręt.*", nom) or \
            re.search("^mac$", nom) or \
            re.search("^mac .*", nom) or \
            re.search("^inspection.*penitentiaire.*", nom) or \
            re.search("^office.*national.*lutte.*contre.*fraude.*corruption.*", nom) or \
            re.search("^enoa$", nom):
        return "Sécurite Intérieur"

    # 12 Forces de Défense
    elif re.search(".*ministere.*armee.*", nom) or \
            re.search("^agence.*logement.*forces.*armees.*", nom) or \
            re.search("^agence.*reinsertion.*sociale.*militaire.*", nom):
        return "Forces de Défense"

    # 13 Economie  et Finance
    elif re.search(".*ministere.*des.*finances.*", nom) or \
            re.search(".*ministere.*economie.*", nom) or \
            re.search(".*ministere du.*plan.*", nom) or \
            re.search("^fonds.*garantie.*automobile.*", nom) or \
            re.search("^fga$", nom):
        return "Economie Finances"

    # 14 Urbanisme, Habitat et Hygiène
    elif re.search(".*ministere.*urbanisme.*habit.*", nom) or \
            re.search(".*ministere.*urbain.*habitat.*", nom) or \
            re.search(".*ministere.*urbanisme.*", nom) or \
            re.search("^agence.*construction.*batiment.*edifice.*public.*", nom) or \
            re.search("^agence.*construction.*rehabilitation.*patrimoine.*etat.*", nom) or \
            re.search("^acbep$", nom) or \
            re.search("^sicap$", nom) or \
            re.search("^sicap .*", nom) or \
            re.search("^societe.*immobiliere.*", nom) or \
            re.search("^societe.*nationale.*habitation.*loyer.*modere.*", nom) or \
            re.search("^delegation.*promotion.*poles.*urbain.*diamniadio.*", nom) or \
            re.search("^societe.*gestion.*infrastructure.*publique.*poles.*urbain.*diamniadio.*", nom) or \
            re.search(".*agence.*travaux.*public.", nom) or \
            re.search("^agetip$", nom):
        return "Urbanisme, Habitat et Hygiène"

    # 15 Primature (gestion du gouvernement)
    elif re.search("^primature.*", nom) or \
            re.search(".*secretariat.*gouvernement.*", nom) or \
            re.search(".*secretariat.*general.*presidence.*", nom) or \
            re.search(".*agence.*gestion.*patrimoine.*bati.*etat.*", nom) or \
            re.search(".*gouvernance .*", nom) or \
            re.search(".*ministere.*de.*la.*fonction.*publique.*", nom) or \
            re.search(".*imprimerie.*nationale.*", nom) or \
            re.search(".*budget.*etat.*", nom) or \
            re.search(".*ministere.*information.*relation.*institution.*porte.*parole.*gouvernement.*", nom):
        return "Primature"

    # 16 Justice
    elif re.search("^ministere.*justice.*", nom) or \
            re.search("^centre.*formation.*judiciaire.*", nom) or \
            re.search("^cour.*des.*comptes.*", nom) or \
            re.search("^cour.*appel.*dakar.*", nom) or \
            re.search("^cour.*supreme.*", nom) or \
            re.search("^centre.*sauvegarde.*kande.*", nom) or \
            re.search("^centre.*adaptation.*sociale.*", nom) or \
            re.search("^cas nianing.*", nom) or \
            re.search("^ministere.*charge.*elections.*", nom) or \
            re.search("^commission.*electorale.*nationale.*autonome.*", nom):
        return "Justice"

    # 17 Sport Losir
    elif re.search("^ministere.*sports.*loisir.*", nom) or \
            re.search("^ministere.*des.*sports.*", nom) or \
            re.search("^loterie.*nationale.*senegal.*", nom) or \
            re.search("^compagnie.*nationale.*theatre.*sorano.*", nom):
        return "Sport Loisir"

    # 18  Poste et Telecommunication
    elif re.search("^adie$", nom) or \
            re.search("^agence.*informatique.*", nom) or \
            re.search("^autorite.*regulation.*telecommunication.*", nom) or \
            re.search("^agence.*regulation.*telecommunication.*", nom) or \
            re.search("^minsitere.*telecommunication.*poste.*", nom) or \
            re.search("^minsitere.*poste.*telecommunication.*", nom) or \
            re.search("^societe.*nationale.*poste.*", nom) or \
            re.search("^societe.*telediffusion.*senegal.*", nom) or \
            re.search(".*gestion.*service.*universel.*telecommunication.*", nom) or \
            re.search("^postefinances.*", nom) or \
            re.search("^maison.*de.*la.*presse.*", nom) or \
            re.search("^radiodiffusion.*television.*", nom) or \
            re.search("^aps$", nom) or \
            re.search("^sspp.*soleil$", nom) or \
            re.search("^soleil .*", nom) or \
            re.search("^soleil$", nom) or \
            re.search("^express.*mail.*senegal.*", nom) or \
            re.search("^ministere.*communication.*telecommunication.*", nom) or \
            re.search("^conseil.*national.*regulation.*audiovisuel.*", nom):
        return "Poste et Telecommunication"

    # 19 Culture, Langues et Protection Sociale
    elif re.search("^ministere.*culture.*patrimoine.*", nom) or \
            re.search("^ministere.*culture.*genre.*cadre.*vie.*", nom) or \
            re.search("^ministere.*travail.*dialogue.*social.*", nom) or \
            re.search("^ministere.*travail.*organisation.*professionnelle.*", nom) or \
            re.search("^ministere.*culture.*communication.*", nom) or \
            re.search("^ministere.*de.*la.*culture.*", nom) or \
            re.search("^delegation.*generale.*organisation.*sommet.*francophonie.*", nom) or \
            re.search("^musee .*", nom):
        return "Culture"

    # 20 Investissement et Finnancement
    elif re.search("^agence.*promotion.*investissements.*grands.*travaux.*", nom) or \
            re.search("^ministere.*promotion.*investissements.*", nom) or \
            re.search("^apix$", nom) or \
            re.search("^apix .*", nom) or \
            re.search("^caisse.*depot.*consignation.*", nom) or \
            re.search("^agence.*developpement.*encadrement.*pme.*", nom) or \
            re.search("^fonds.*garantie.*investissement.*", nom) or \
            re.search("^societe.*nationale.*recouvrement.*", nom):
        return "Investissement"

    # 21 Religion
    elif re.search("^anoci$", nom) or \
            re.search("^agence.*conference.*islamique.*", nom):
        return "Religion"



    # 22 Industrie
    elif re.search("^societe.*oleagineux.*", nom) or \
            re.search("^agence.*amenagement.*promotion.*site.*industriel.*", nom) or \
            re.search("^ministere.*industrie.*", nom):
        return "Industrie"

    # 23 Socilal
    elif re.search("^ministere.*femme.*famille.*", nom) or \
            re.search("^ministere.*femme.*enfan.*entreprenariat.*feminin.*", nom) or \
            re.search("^ministere.*femme.*enfan.*entrepreneuriat.*feminin.*", nom) or \
            re.search("^ministere.*famille.*entreprenariat.*feminin.*", nom) or \
            re.search("^ministere.*entreprenariat.*feminin.*", nom) or \
            re.search("^ministere.*famille.*organisation.*feminin.*", nom) or \
            re.search("^delegation.*generale.*entreprenariat.*rapide.*femmes.*jeunes.*", nom) or \
            re.search("^delegation.*generale.*protection.*sociale.*solidarite.*nationale.*", nom):
        return "Socilal"

    # 24 Diaspora
    elif re.search("^ministere.*affaire.*etrangere.*", nom) or \
            re.search("^ministere.*senegalais.*exterieur.*", nom):
        return "Diaspora"

    # 25 Marchés Publics
    elif re.search("^autorite.*marche.*public.*", nom) or \
            re.search("^agence.*regulation.*marche.*", nom):
        return "Marchés Publics"

    # 26 Commerce
    elif re.search("^ministere.*du.*commerce.*", nom) or \
            re.search("^conseil.*senegalais.*chargeur.*", nom) or \
            re.search("^cosec$", nom) or \
            re.search("^cosec .*", nom) or \
            re.search("^agence.*nationale.*appui.*marchand.*ambulant.*", nom) or \
            re.search("^agence.*nationale.*sedentarisation.*marchand.*ambulant.*", nom) or \
            re.search("^agence.*senegalais.*promotion.*exportation.*", nom):
        return "Commerce"

    # 27 Financement Privé
    elif re.search("^afd$", nom) or \
            re.search("^banque.*ouest.*africaine.*developpement.*", nom):
        return "Financement Privé"

    # 28   Développement territorial
    elif re.search("^ard$", nom) or \
            re.search("^agence.*regional.*developpement.*", nom) or \
            re.search("^agence.*regional.*devellopement.*", nom) or \
            re.search("^ard .*", nom) or \
            re.search("^agence.*nationale.*amenagement.*territoire.*", nom) or \
            re.search("^anat .*", nom) or \
            re.search("^anat$", nom) or \
            re.search("^agence.*nationale.*eco.*village.*", nom) or \
            re.search("^anev$", nom) or \
            re.search("^agence.*developpement.*municipal.*", nom) or \
            re.search("^adm$", nom) or \
            re.search("^agence.*developpement.*local.*", nom) or \
            re.search("^agence.*nationale.*du.*plan.*", nom) or \
            re.search("^communaute.*agglomeration.*dakar.*", nom) or \
            re.search("^ministere.*decentralisation.*collectivite.*locale.*", nom) or \
            re.search("^ministere.*amenagement.*territoire.*collectivite.*local.*", nom) or \
            re.search("^ministere.*collectivite.*territoriale.*amenagement.*territoire.*", nom) or \
            re.search("^ministere.*developpement.*communautaire.*equite.*sociale.*territoriale.*", nom) or \
            re.search("^ministere.*gouvernance.*locale.*developpement.*amenagement.*territoire.*", nom) or \
            re.search("^programme.*national.*plates.*forme.*multifonctionnel.*lutte.*contre.*pauvrete.*", nom) or \
            re.search("^programme national$", nom) or \
            re.search("^projet.*appui.*developpement.*rural.*casamance.*", nom) or \
            re.search("^paderca$", nom) or \
            re.search("^projet.*pole.*developpement.*casamance.*", nom) or \
            re.search("^agence.*nationale.*relance.*activite.*economique.*sociale.*casamance.*", nom) or \
            re.search("^pacr.*vfs.*", nom):
        return "Développement territorial"

    # 9 Statistique et Démographie
    elif re.search("^agence.*statistique.*demographie.*senegal.*", nom) or \
            re.search("^ansd$", nom):
        return "Développement territorial"

    # 30 Tourisme (liant loisir)
    elif re.search("^agence.*senegalais.*promotion.*touristique.*", nom) or \
            re.search("^sapco$", nom) or \
            re.search("^societe.*amenagement.*promotion.*cotes.*zones.*touristique.*", nom) or \
            re.search("^ministere.*tourisme.*loisir.*", nom):
        return "Tourisme"

    # 31 Mines et de la Géologie
    elif re.search("^ministere.*mine.*geologie.*", nom):
        return "Mines et de la Géologie"
    # 32 Artisanat
    elif re.search("^agence.*promotion.*developpement.*artisanat.*", nom) or \
            re.search("^ministre.*artisanat.*transformation.*secteur.*informel.*", nom):
        return "Artisanat"

    else:
        return "Autres"

