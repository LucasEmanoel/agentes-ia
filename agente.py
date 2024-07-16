import pyautogui

#deve setar os pixels de acordo com sua tela
X = 2450
Y1 = 580
Y2 = 680

regras = {"obstaculo": "pular"}

def agente_reativo_simples(percepcao): 
    estado = interpreta_entrada(percepcao)
    regra = regra_correspondente(estado, regras)   
    acao = acao_da_regra(regra)
    return acao

def regra_correspondente(estado, regras):
    return regras.get(estado, None)

def interpreta_entrada(percepcao):
    aux_color = percepcao.getpixel((X - 100, Y1))


    for x in range(int(X), int(X+15)):
        for y in range(Y1, Y2):
            color = percepcao.getpixel((x, y))
            
            if color != aux_color:
                return "obstaculo"
    return "livre"
            
def acao_da_regra(regra):
    if regra == "pular":
        jump()
              
def jump():
    pyautogui.press("up")
