# bayes theorem to find a conditional probability
# what is the probability of this account being a bot given that they have an 8dig long username
pbot = 0.1          # prob of bot
p8_bot = 0.8        # prob of 8 digits given that it is a bot
p8_human = 0.05     # prob of 8 digits given that it is human


def bot8(pbot, p8_bot, p8_human):
    # p(8) = p(8nbot) + p(8nhuman) = p(8|bot) * p(bot) + p(8|human) * p(human)
    p8 = p8_bot * pbot + p8_human * (1 - pbot)
    pbot_8 = p8_bot * pbot / p8  # bayes rule
    print(pbot_8)


bot8(pbot, p8_bot, p8_human)
