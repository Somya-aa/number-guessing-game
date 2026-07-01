# 🎯 Number Guessing Game

A simple and interactive **Number Guessing Game** built with Python. The game generates a random number, and the player must guess it with the help of hints until the correct number is found.

## 🚀 Features

* 🎮 Three difficulty levels:

  * Easy (1–50)
  * Medium (1–100)
  * Hard (1–500)
* 🎲 Random number generation
* 💡 Hints if the guess is too high or too low
* 📊 Counts the number of attempts
* ✅ Input validation
* 🔄 Play Again option

## 🛠️ Technologies Used

* Python 3
* Random Module

## 📂 Project Structure

```text
number-guessing-game/
├── game.py
├── README.md
└── LICENSE
```

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/number-guessing-game.git
```

2. Navigate to the project folder:

```bash
cd number-guessing-game
```

3. Run the program:

```bash
python app.py
```

## 🎮 How to Play

1. Choose a difficulty level.
2. Enter your guess.
3. The game will tell you if your guess is **too high** or **too low**.
4. Keep guessing until you find the correct number.
5. Your total number of attempts will be displayed.
6. Choose whether to play another round.

## 📸 Sample Output

```text
🎮 Welcome to the Number Guessing Game!

Choose Difficulty:
1. Easy (1-50)
2. Medium (1-100)
3. Hard (1-500)

Enter your choice: 2

I have chosen a number between 1 and 100.

Enter your guess: 45
⬆️ Too low!

Enter your guess: 72
⬇️ Too high!

Enter your guess: 61

🎉 Congratulations!
You guessed the number in 3 attempts.
```

## 🔮 Future Improvements

* 🏆 High score system
* 💾 Save scores in a file
* ⏱️ Timer-based gameplay
* 💡 Additional hint system (odd/even, range)
* 🎨 Graphical User Interface (Tkinter)
* 🌐 Web version using Flask
* 👥 Multiplayer mode
* 📊 Leaderboard using SQLite

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project helpful, consider giving it a star on GitHub!
