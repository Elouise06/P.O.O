import turtle
from turtle import Turtle, done

kuromi = Turtle()
kuromi.shape('turtle')
kuromi.color('purple')
kuromi.forward(100)
kuromi.right(90)
kuromi.forward(100)
kuromi.right(90)
kuromi.forward(100)
kuromi.right(90)
kuromi.forward(100)

cherry = Turtle()
cherry.shape('turtle')
cherry.color('black')
cherry.circle(50)

kuromi.left(135)
kuromi.forward(141.4)
kuromi.left(135)
kuromi.forward(141.4)
done()