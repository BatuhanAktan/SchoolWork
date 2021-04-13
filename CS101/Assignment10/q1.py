code = "A lot of you are probably wondering about BreakTheCode, what it is we are doing and what we seek. Know that we love everything tech, vexing lines of code to engineers fighting the virus and  saving our asses as we speak. Unabatedly our brand has always been about providing the best domains to the craziest geeks in the gala.xy. However 2020 has been a pretty shit year for all, us included. Yes we could have pushed a promo on you guys, or run some ads but it just did not seem right this Black Friday. U and the amazing projects you create on dotTech Domains inspired this fun little game we have built. H opefully it will inspire you to use a Tech domain for your next cool creation."

possibleCode = ''
for i in range(len(code),-1,-1):
    if code[i] == '.':
        possibleCode += code[i+1]

print(possibleCode)
