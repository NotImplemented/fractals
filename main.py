import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img


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
                canvas[x, y] = np.array([0.75, 0.75, 0.0])
            else:
                gradient = (1.0 - steps / iterations)
                canvas[x, y] = np.array([gradient, gradient, 1.0])

    #plt.imshow(canvas)
    #plt.show()
    plt.imsave('mandelbrot.png', canvas)


def draw_julia(height, width, c_re, c_im, top, left, bottom, right, iterations, threshold = 12.0):
    canvas = np.empty((height, width, 3))
    
    for x in range(height):
        for y in range(width):
            a = y * (right - left) / width + left
            b = x * (bottom - top) / height + top

            steps = 0
            speed = 0
            for _ in range(iterations):
                c, d = a, b
                a, b = a * a - b * b + c_re, 2 * a * b + c_im
                
                speed += (a - c) * (a - c) + (b - d) * (b - d)
                    
                distance = a * a + b * b
                if distance > threshold:
                    break

                steps += 1

            if steps == iterations:
                canvas[x, y] = np.array([0.0, (np.sin(92.0 * speed / steps) + 1.0) / 2.0 , 0.0])
            else:
                gradient = (1.0 - steps / iterations)
                canvas[x, y] = np.array([0.0, 0.0, 1.0 / (1.0 + gradient)])

    plt.imshow(canvas)
    plt.show()
    img.imsave('julia_siegel.png', canvas)


def contrast_sigmoid(x):
    return 2.0 / (1.0 + 2.0 * np.exp(0.5 - x))


def contrast(x):
    return np.power(x, 4)


draw_mandelbrot(2048, 2048, -1.5, -2.2, 1.5, 0.8, 32)

# draw_julia(2048, 2048, -0.39054, -0.58679, -1.4, -1.4, 1.4, 1.4, 64)


