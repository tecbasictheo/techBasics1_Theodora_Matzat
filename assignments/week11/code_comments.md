
1. Where did you find the code and why did you choose it? (Provide the link)

I found my code on GitHub.com under the link: https://github.com/pyjama-dev/python-crossy-game/blob/master/crossy-road.py
I choose this code because it is similar for what I had in mind for my final project and is over one hundred lines of code. 
---

2. What does the program do? What's the general structure of the program? 

The program creates a game where you move a character and should avoid enemies crossing your path. The goal is to reach the treasure at the end of the path.  
As you reach higher levels the enemies become faster and multiply.
The program is structured in classes, the entire game structure is in these classes. How the game functions, the game loop and the gameplay is contained in the Class: Game. 
Only the initialization and the quiting of the game happens outside if the classes. 
There is a Class for the game design, with a method for the game loop. 
---

3. Function analysis: pick one function and analyze it in detail:

- What does this function do?

The function is a method in the class Game. The method is called run_game_loop. 
It creates all the characters and has the game-loop. 

- What are the inputs and outputs?

The method takes the speed of the enemies as a parameter. In the method these speed arguments of the enemies are created in the function, as it increases everytime a game is finished. 
Also, it tells the program when to end the game.

- How does it work (step by step)? 

First, it sets the game over variable and the win variable to false and sets the direction to 0. Then it loads and sizes the players character image and does the same for the three enemies, also it defines the speed or better it defines how the speed should increase. 
As next step it creates the game-loop and does it in a "while not game over" loop. 
It firstly creates a for loop for all events in the game. There are the events of Quit-game and the difference keys. This is achieved through an if statement for game_quit and elif for the key-events. It detects if the key is pressed or raised. This creates an output, which gets printed. This loop also updates all the graphics and sets the clock in the game, for updating the game. But this is at the end of the loop. 
After that the background and the treasure is drawn. And the players character and the enemies are drawn and updated. 
Followed up, with the adding of more enemies in the later levels. That happens when the speed is over two and over four, each time it adds a new enemies. This happens because the speed increases after every finished level, with that the player is able to achieve higher levels. 
Then, with an if-statement the code detects if the plyer collides with an enemies or with the treasure. Both end the game, but in different ways. First it checks if the player collided with an enemies. If that is true the game over variable equals true and the win variable equals false. This is followed up with the print of a text: "You Lose", this updates and stays on the screen through clock_tick until the statement breaks the loop. 
If collision with enemies is false, the code checks if the player collides with the treasure. Then the game over variable and the win variable equals true. This prints the text: "You WIN!" and waits before it brakes out of the loop. 
Here is now where the for loop for all events updates all the graphics. 
Lastly, the last part of the "while not game over" loop is there, which is an if statement that ask if the win variable is true. If yes it updates the speed of the enemies and creates through this a higher level. Otherwise, the else statement, just returns and ends or better restarts the game loop.  

4. Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)

My main takeaway is the structure of the program, it is really clear through the use of classes. Also, to make all functions methods was new for me, but made it so much easier to read the code.
Such program structure is the total opposite of my own programs, but it is my goal to be able to structure my own code this way. 
Furthermore, the detailed comments for others to understand the code really impressed me and I should definitely improve my codes in this way. 

5. What parts of the code were confusing or difficult at the beginning to understand?

At first, I had to figure out how the code works, with the game-loop in a method and additionally how the game can be a class. 
- Were you able to understand what it is doing after your own research?

Yes, I just had to take my time to understand the written code and read some pygame guides to understand how it is functioning. 

---
