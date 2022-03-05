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

pancake = turtle.Turtle()
pancake.shape('circle')
pancake.color('orange')
pancake.shapesize(30)

sugar = turtle.Turtle()
sugar.shape('sugar.gif')
turtle.done()