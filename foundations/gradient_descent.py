class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        x = init
        for _ in range(iterations):
            d_f = 2*x 
            x = x - learning_rate * d_f

        return round(x, 5)
