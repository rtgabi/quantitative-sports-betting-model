def kelly_criterion(odds: float, p: float) -> float:
    # Get "b" -> the net winnings for 1 unit of money
    b=odds-1

    # Losing probability
    q=1-p

    # Kelly fraction
    f=(b*p - q) / b

    return f

def alloc(odds: list[float], p: list[float], balance: float) -> list[float]:
    """
    :param odds: List of odds for every wanted event
    :param p: List of probabilities that match the list of odds (the probability should be the one found by the model)
    :param balance: Available balance to use for bets
    :return: List of allocated money on every event
    """

    kelly_fractions={}

    for i in range(len(odds)):
        f=kelly_criterion(odds[i],p[i])
        kelly_fractions[i]={}
        kelly_fractions[i]['f*']=round(f,3)
        # If the Expect Value EV is positive, there is an edge
        if f>0:
            kelly_fractions[i]['Decision']='Bet'
        else:
            kelly_fractions[i]['Decision']='No bet'

    total_fraction=0
    for i in range(len(odds)):
        if kelly_fractions[i]['Decision']=='Bet':
            total_fraction+=kelly_fractions[i]['f*']

    normalized_kelly_fractions=[]
    for i in kelly_fractions:
        a=kelly_fractions[i]['f*']
        normalized_kelly_fractions.append(a/total_fraction if a>0 else 0)

    bets=[]

    # Shows how much actual money to allocate on each bet
    for i in normalized_kelly_fractions:
        bet_amount=i*balance
        bets.append(round(bet_amount,3))

    return bets