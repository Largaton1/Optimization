import argparse
import json
import random
import time
from PIL import Image, ImageDraw
import numpy as np


# Fonction pour générer une solution aléatoire
def generate_random_solution(n_shapes, width, height):
    shapes = []
    for _ in range(n_shapes):
        shape_type = random.choice(['circle', 'rect', 'triangle'])
        if shape_type == 'circle':
            shape = {
                'type': 'circle',
                'cx': random.randint(0, width),
                'cy': random.randint(0, height),
                'r': random.randint(5, 50),
                'color': f'#{random.randint(0, 0xFFFFFF):06x}'
            }
        elif shape_type == 'rect':
            shape = {
                'type': 'rect',
                'x': random.randint(0, width),
                'y': random.randint(0, height),
                'width': random.randint(5, 50),
                'height': random.randint(5, 50),
                'color': f'#{random.randint(0, 0xFFFFFF):06x}'
            }
        elif shape_type == 'triangle':
            shape = {
                'type': 'triangle',
                'points': [
                    (random.randint(0, width), random.randint(0, height)),
                    (random.randint(0, width), random.randint(0, height)),
                    (random.randint(0, width), random.randint(0, height)),
                ],
                'color': f'#{random.randint(0, 0xFFFFFF):06x}'
            }
        shapes.append(shape)
    return shapes


# Fonction pour générer un fichier SVG
def generate_svg(shapes, output_file, width, height):
    with open(output_file, 'w') as f:
        f.write(f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n')
        for shape in shapes:
            if shape['type'] == 'circle':
                f.write(f'<circle cx="{shape["cx"]}" cy="{shape["cy"]}" r="{shape["r"]}" fill="{shape["color"]}" />\n')
            elif shape['type'] == 'rect':
                f.write(f'<rect x="{shape["x"]}" y="{shape["y"]}" width="{shape["width"]}" height="{shape["height"]}" fill="{shape["color"]}" />\n')
            elif shape['type'] == 'triangle':
                points = " ".join([f"{x},{y}" for x, y in shape['points']])
                f.write(f'<polygon points="{points}" fill="{shape["color"]}" />\n')
        f.write('</svg>')


# Fonction pour calculer la fitness
def compute_fitness(source_image, shapes, width, height):
    generated_image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(generated_image)

    for shape in shapes:
        if shape['type'] == 'circle':
            x0 = shape['cx'] - shape['r']
            y0 = shape['cy'] - shape['r']
            x1 = shape['cx'] + shape['r']
            y1 = shape['cy'] + shape['r']
            draw.ellipse([x0, y0, x1, y1], fill=shape['color'])
        elif shape['type'] == 'rect':
            x0 = shape['x']
            y0 = shape['y']
            x1 = x0 + shape['width']
            y1 = y0 + shape['height']
            draw.rectangle([x0, y0, x1, y1], fill=shape['color'])
        elif shape['type'] == 'triangle':
            draw.polygon(shape['points'], fill=shape['color'])

    source_array = np.array(source_image)
    generated_array = np.array(generated_image)
    return np.mean((source_array - generated_array) ** 2)


# Mutation
def mutate(shapes, width, height):
    shape = random.choice(shapes)
    mutation_type = random.choice(['position', 'size', 'color'])
    if shape['type'] == 'circle':
        if mutation_type == 'position':
            shape['cx'] = random.randint(0, width)
            shape['cy'] = random.randint(0, height)
        elif mutation_type == 'size':
            shape['r'] = random.randint(5, 50)
        elif mutation_type == 'color':
            shape['color'] = f'#{random.randint(0, 0xFFFFFF):06x}'
    elif shape['type'] == 'rect':
        if mutation_type == 'position':
            shape['x'] = random.randint(0, width)
            shape['y'] = random.randint(0, height)
        elif mutation_type == 'size':
            shape['width'] = random.randint(5, 50)
            shape['height'] = random.randint(5, 50)
        elif mutation_type == 'color':
            shape['color'] = f'#{random.randint(0, 0xFFFFFF):06x}'
    elif shape['type'] == 'triangle':
        if mutation_type == 'position':
            shape['points'] = [
                (random.randint(0, width), random.randint(0, height)) for _ in range(3)
            ]
        elif mutation_type == 'color':
            shape['color'] = f'#{random.randint(0, 0xFFFFFF):06x}'
    return shapes


# Sauvegarder et charger une solution
def save_solution(shapes, file_path):
    with open(file_path, 'w') as f:
        json.dump(shapes, f)


def load_solution(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


# Algorithme génétique
def genetic_algorithm(source_image, n_generations, n_population, n_shapes):
    width, height = source_image.size
    population = [generate_random_solution(n_shapes, width, height) for _ in range(n_population)]
    fitness_values = [compute_fitness(source_image, sol, width, height) for sol in population]

    for generation in range(n_generations):
        sorted_population = [sol for _, sol in sorted(zip(fitness_values, population))]
        population = sorted_population[:n_population // 2]

        new_population = []
        while len(new_population) < n_population:
            parent1, parent2 = random.sample(population, 2)
            child = mutate(parent1.copy(), width, height)
            new_population.append(child)

        population = new_population
        fitness_values = [compute_fitness(source_image, sol, width, height) for sol in population]
        best_fitness = min(fitness_values)
        print(f"Generation {generation + 1}, Best Fitness: {best_fitness}")

    best_solution = population[fitness_values.index(min(fitness_values))]
    return best_solution


# Interface CLI
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Image recreation using geometric shapes.")
    parser.add_argument('--input', type=str, required=True, help="Input image file path.")
    parser.add_argument('--output', type=str, required=True, help="Output SVG file path.")
    parser.add_argument('--shapes', type=int, default=50, help="Number of shapes.")
    parser.add_argument('--generations', type=int, default=10, help="Number of generations.")
    parser.add_argument('--population', type=int, default=10, help="Population size.")
    parser.add_argument('--save', type=str, help="Save solution to file.")
    parser.add_argument('--load', type=str, help="Load solution from file.")

    args = parser.parse_args()
    if args.load:
        best_solution = load_solution(args.load)
    else:
        source_image = Image.open(args.input)
        best_solution = genetic_algorithm(source_image, args.generations, args.population, args.shapes)

    if args.save:
        save_solution(best_solution, args.save)

    generate_svg(best_solution, args.output, Image.open(args.input).size[0], Image.open(args.input).size[1])
