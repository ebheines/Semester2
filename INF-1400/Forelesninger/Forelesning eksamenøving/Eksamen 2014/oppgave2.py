POENG_JAGER = 10
POENG_HANGARSKIP = 100
POENG_FRAKTSKIP = 70

# Oppgave 2a
def team_score(romskip):
    score = 0

    for skip in romskip:
        if skip == Jager:
            score += POENG_JAGER
        
        if skip == Hangarskip:
            score += POENG_HANGARSKIP
        
        if skip == Fraktskip:
            score += POENG_FRAKTSKIP
    
    return score

# Oppgave 2b
def team_score(romskip):
    score = 0

    for skip in romskip:
        score += skip.STYRKEPOENG
    
    return score

