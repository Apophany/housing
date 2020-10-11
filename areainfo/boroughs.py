from areainfo.borough import Borough

CAMDEN = Borough("Camden", True, "5E93941")
GREENWICH = Borough("Greenwich", True, "5E61226")
HACKNEY = Borough("Hackney", True, "5E93953")
HAMMERSMITH_AND_FULHAM = Borough("Hammersmith and Fulham", True, "5E61407")
ISLINGTON = Borough("Islington", True, "5E93965")
KENSINGTON_AND_CHELSEA = Borough("Royal Borough of Kensington and Chelsea", True, "5E61229")
LAMBETH = Borough("Lambeth", True, "5E93971")
LEWISHAM = Borough("Lewisham", True, "5E61413")
SOUTHWARK = Borough("Southwark", True, "5E61518")
TOWER_HAMLETS = Borough("Tower Hamlets", True, "5E61417")
WANDSWORTH = Borough("Wandsworth", True, "5E93977")
WESTMINSTER = Borough("Westminster", True, "5E93980")
BARKING_AND_DAGENHAM = Borough("Barking and Dagenham", False, "5E61400")
BARNET = Borough("Barnet", False, "5E93929")
BEXLEY = Borough("Bexley", False, "5E93932")
BRENT = Borough("Brent", False, "5E93935")
BROMLEY = Borough("Bromley", False, "5E93938")
CROYDON = Borough("Croydon", False, "5E93944")
EALING = Borough("Ealing", False, "5E93947")
ENFIELD = Borough("Enfield", False, "5E93950")
HARINGEY = Borough("Haringey", False, "5E61227")
HARROW = Borough("Harrow", False, "5E93956")
HAVERING = Borough("Havering", False, "5E61228")
HILLINGDON = Borough("Hillingdon", False, "5E93959")
HOUNSLOW = Borough("Hounslow", False, "5E93962")
KINGSTON_UPON_THAMES = Borough("Kingston upon Thames", False, "5E93968")
MERTON = Borough("Merton", False, "5E61414")
NEWHAM = Borough("Newham", False, "5E61231")
REDBRIDGE = Borough("Redbridge", False, "5E61537")
RICHMOND_UPON_THAMES = Borough("Richmond upon Thames", False, "5E61415")
SUTTON = Borough("Sutton", False, "5E93974")
WALTHAM_FOREST = Borough("Waltham Forest", False, "5E61232")


def get_boroughs():
    return (
        CAMDEN,
        GREENWICH,
        HACKNEY,
        HAMMERSMITH_AND_FULHAM,
        ISLINGTON,
        KENSINGTON_AND_CHELSEA,
        LAMBETH,
        LEWISHAM,
        SOUTHWARK,
        TOWER_HAMLETS,
        WANDSWORTH,
        WESTMINSTER,
        BARKING_AND_DAGENHAM,
        BARNET,
        BEXLEY,
        BRENT,
        BROMLEY,
        CROYDON,
        EALING,
        ENFIELD,
        HARINGEY,
        HILLINGDON,
        HOUNSLOW,
        KINGSTON_UPON_THAMES,
        MERTON,
        NEWHAM,
        REDBRIDGE,
        RICHMOND_UPON_THAMES,
        SUTTON,
        WALTHAM_FOREST
    )
