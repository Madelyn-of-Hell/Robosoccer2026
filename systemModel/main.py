class Protocol:
    DEFENCE = 0
    ATTACK = 1
    INTERFERENCE = 2

def getTeammateProtocol() -> Protocol:...

def protocolSelector() -> Protocol:
    match getTeammateProtocol():
        case Protocol.DEFENCE: 
            return Protocol.ATTACK
        case Protocol.ATTACK:
            return Protocol.INTERFERENCE
        case Protocol.INTERFERENCE:
            return Protocol.ATTACK







def main(
        

)
    


    

