import numpy as np
import matplotlib.pyplot as plt


def draw_mandelbrot(height, width, top, left, bottom, right, iterations, threshold = 12.0):
    canvas = np.empty((height, width, 3))

    for x in range(height):
        for y in range(width):
            c_im = x * (bottom - top) / height + top
            c_re = y * (right - left) / width + left
            a, b = 0.0, 0.0

            steps = 0
            for _ in range(iterations):
                a, b = a * a - b * b + c_re, 2 * a * b + c_im

                distance = a*a + b*b
                if distance > threshold:
                    break

                steps += 1

            if steps == iterations:
                canvas[x,y] = np.array([0.0, 0.0, 1.0])
            else:
                gradient = (1.0 - steps / iterations)
                gradient *= gradient
                canvas[x, y] = np.array([gradient, gradient, 0])

    plt.imshow(canvas)
    plt.show()


draw_mandelbrot(2048, 2048, -1.5, -2.2, 1.5, 0.8, 128)
