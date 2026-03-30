# 🎰 Lottery

A simple lottery game written in Python. The player picks 5 numbers, the program draws 5 winning numbers — the more matches, the bigger the prize!

---

## 📋 Requirements

- Python 3.x
- No external libraries required (uses only the built-in `random` module)

---

## 🚀 How to Run

```bash
python loteria.py
```

---

## 🎮 How to Play

1. Start the program — your starting balance is **50 PLN**
2. Decide whether you want to play (`Tak` / `Nie`)
3. Enter **5 numbers** in the range **0–25**
4. The program draws 5 winning numbers
5. Matches are checked and your balance is updated
6. The game ends when you run out of money or decline the next round

---

## 💰 Prize Table

| Matched Numbers | Win / Loss |
|:-:|:-:|
| 0 | -10 PLN |
| 1 | +1 PLN |
| 2 | +5 PLN |
| 3 | +10 PLN |
| 4 | +20 PLN |
| 5 | +50 PLN |

> Each ticket costs **10 PLN** (deducted on zero matches).

---

## 🏗️ Code Structure

### `Loteria` Class

| Method | Description |
|---|---|
| `wybierz()` | Takes 5 numbers as input from the player |
| `losuj()` | Draws 5 unique winning numbers |
| `sprawdz()` | Compares the player's numbers with the winning ones |
| `aktualizuj_kase()` | Adds winnings or deducts ticket cost |
| `resetuj()` | Clears numbers before the next round |
| `__repr__()` | Displays current balance and numbers |

---

