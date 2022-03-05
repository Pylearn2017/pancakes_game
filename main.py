import turtle
import random

def cream_add():
	pancake.color('white')
	pancake.shapesize(15)
	pancake.stamp()


def jam_add():
	pancake.color('red')
	pancake.shapesize(15)
	pancake.stamp()


def iscollision(obj1, obj2, w1, w2, h1, h2):
	if obj1.xcor() + w1 > obj2.xcor() - w2 and obj1.xcor() - w1 < obj2.xcor() + w2:
		if obj1.ycor() + h1 > obj2.ycor() - h2 and obj1.ycor() - h1 < obj2.ycor() + h2:
			return True
	return False

def click(x, y):
	hero.setposition(x,y)
	for ingredient in ingredients:
		if iscollision(ingredient, hero, 
			ingredient.width, 
			hero.width, 
			ingredient.height,
			hero.height):
			ingredient.add()

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

hero = turtle.Turtle()
hero.penup()
hero.hideturtle()
hero.speed(0)
hero.height = 10
hero.width = 10

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
sugar.height = 50
sugar.width = 50

jam = turtle.Turtle()
jam.shape('jam.gif')
jam.penup()
jam.setposition(-150, -300)
jam.height = 50
jam.width = 50
jam.add = jam_add

cream = turtle.Turtle()
cream.shape('cream.gif')
cream.penup()
cream.setposition(0, -300)
cream.height = 50
cream.width = 50
cream.add = cream_add

caviar = turtle.Turtle()
caviar.shape('caviar.gif')
caviar.penup()
caviar.setposition(150, -300)
caviar.height = 50
caviar.width = 50

banana = turtle.Turtle()
banana.shape('banana.gif')
banana.penup()
banana.setposition(300, -300)
banana.height = 50
banana.width = 50

pancake = turtle.Turtle()
pancake.shape('circle')
pancake.color('orange')
pancake.shapesize(25)
pancake.stamp()

ingredients = [sugar, jam, cream, caviar, banana]
window.onclick(click)

turtle.done()