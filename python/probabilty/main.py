import random
def pick_ball_experiment():
      ball = ['red', 'blue', 'green']
      result = random.choice(ball)

      pro = ball.count('red')/len(ball)
      print("Probability of picking red ball is:", pro)

      if result == 'red':
        return "Red ball picked"
      else:
        return "Better luck next time."

result = pick_ball_experiment()
print(result)