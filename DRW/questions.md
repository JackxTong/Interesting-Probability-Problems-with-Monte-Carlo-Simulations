### Question 3 of 6:
Let \( X \sim \mathcal{N}(0, 1) \) be a normally distributed random variable. We want to "quantize \( X \) using 1 bit per symbol", that is, we want to choose \( c \in \mathbb{R}_+ \) in the following mapping

\[
Q(x) = \begin{cases} 
c, & \text{if } x \geq 0 \\
-c, & \text{if } x < 0
\end{cases}
\]

to minimize the "quantization error" \( \mathbb{E}[(X - Q(X))^2] \). Let \( c^* \) be the minimizer. What is the value of \( c^* \)? Round your number to 3 decimal places.

---

### Question 4 of 6:
You have a fair 5-sided die, and you want to roll it until you see all 5 different sides at least once. However, there is an additional condition: once you see 4 different sides, if you roll a side that you have already seen, you must start the process from the beginning, as if you have not seen any sides.

Calculate the expected number of rolls needed to see all 5 sides under this condition. Round your number to 3 decimal places.

---

### Question 5 of 6:
The Sharpe ratio is a metric used to characterize trading strategies, and is defined to be its expected return over some interval divided by the standard deviation of returns over the same interval. Assume we have two trading strategies whose returns are independent, one with Sharpe ratio 4, and the other with Sharpe ratio 5. 

By allocating the portfolio optimally between the two strategies, what is the maximum Sharpe ratio we can achieve? Round your number to 3 decimal places.

---

### Question 6 of 6:
Suppose you have a fair coin and start at step 0. Each time you toss the coin, if it lands on heads, you move forward 1 step; if it lands on tails, you move forward 2 steps. You continue tossing the coin and moving accordingly. Let \( p_n \) be the probability of ever landing exactly on step \( n \). Calculate

\[
1000(p_4 + p_8)
\]

Round your number to 3 decimal places.
