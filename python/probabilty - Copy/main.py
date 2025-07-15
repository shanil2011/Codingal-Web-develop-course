import random
def pick_ball_experiment():
      ball = [1, 2, 3, 4, 5, 6]
      result = random.choice(ball)

      pro = ball.count(1)/len(ball)
      print("Probability of picking red ball is:", pro)

      if result == 'red':
        return "Red ball picked"
      else:
        return "Better luck next time."

result = pick_ball_experiment()
print(result)