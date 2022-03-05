import turtle
import random

font = ('Arial', 36, 'normal')
order_list = [
	'Блин с сахаром',
	'Блин с икрой',
	'Блин со сметаной',
	'Блин с вареньем',
	'Блин с бананом',
]

window = turtle.Screen()
window.register_shape('banana.gif')
window.register_shape('caviar.gif')
window.register_shape('cream.gif')
window.register_shape('jam.gif')
window.register_shape('sugar.gif')

order = turtle.Turtle()
order.penup()
order.setposition(-300, 330)
order.write(random.choice(order_list), font=font)

done = turtle.Turtle()
done.penup()
done.setposition(-370, 330)
done.shape('square')
done.color('green')
done.shapesize(5)

sugar = turtle.Turtle()
sugar.shape('sugar.gif')
sugar.penup()
sugar.setposition(-300, -300)
sugar.height = 100
sugar.width = 100

jam = turtle.Turtle()
jam.shape('jam.gif')
jam.penup()
jam.setposition(-150, -300)
jam.height = 100
jam.width = 100

cream = turtle.Turtle()
cream.shape('cream.gif')
cream.penup()
cream.setposition(0, -300)
cream.height = 100
cream.width = 100

caviar = turtle.Turtle()
caviar.shape('caviar.gif')
caviar.penup()
caviar.setposition(150, -300)
caviar.height = 100
caviar.width = 100

banana = turtle.Turtle()
banana.shape('banana.gif')
banana.penup()
banana.setposition(300, -300)
banana.height = 100
banana.width = 100

pancake = turtle.Turtle()
pancake.shape('circle')
pancake.color('orange')
pancake.shapesize(30)


print('Это новое ')

turtle.done()