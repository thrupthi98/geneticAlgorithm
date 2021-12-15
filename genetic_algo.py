from random import randint, choice, random
from PIL import Image, ImageDraw

# Creates a complete chromosome with 100 genes
def createChromosome():
    newChromosome = []
    for i in range(100):
        newChromosome.append(newGenes())
    return newChromosome

# Get new genes
# Used to create completely new chromosomes 
# Used while mutating the children
def newGenes():
    x = randint(0, 21)
    y = randint(0, 21)
    s = randint(1,5)
    return [(x,y),(x + s,y+ s)] 

# Find out the value of how close the created image is to the actual image
def valuation(chromosome):
  sample = Image.new("RGB", (32, 32),"white")
  img = ImageDraw.Draw(sample,'RGBA') 
  for ordinates in chromosome:
    img.rectangle(ordinates, (105,105,105,125))
  pixels = sample.load()
  value = 0
  origImg = Image.open('apple.png').load()
#   Calculate the difference of pixels
  for i in range(0,28):
    for j in range(0,28):
      try:
        diffRed   = abs(origImg[i,j]   - pixels[i,j][0]) 
        diffGreen  = abs(origImg[i,j]   - pixels[i,j][1])
        diffBlue  = abs(origImg[i,j]   - pixels[i,j][2])

        pctDiffRed   = diffRed / 255 
        pctDiffGreen = diffGreen / 255
        pctDiffBlue   = diffBlue  / 255
        value = value + (((pctDiffRed + pctDiffGreen + pctDiffBlue) / 3) * 100) 
      except:
        diffRed   = abs(origImg[i,j][0]   - pixels[i,j][0]) 
        diffGreen  = abs(origImg[i,j][1]   - pixels[i,j][1])
        diffBlue  = abs(origImg[i,j][2]   - pixels[i,j][2])

        pctDiffRed   = diffRed / 255 
        pctDiffGreen = diffGreen / 255
        pctDiffBlue   = diffBlue  / 255
        value = value + (((pctDiffRed + pctDiffGreen + pctDiffBlue) / 3) * 100)
  return value

#  Function to create children from chromosomes
def generateChildFrom(ch1, ch2):
  child = []
  for p1, p2 in zip(ch1, ch2):
    # Generate a random number 0 to 1
    probablity = random()
    # Check the probablity for mutating the genes
    if probablity < 0.45:
      child.append(p1)
    elif probablity < 0.9:
      child.append(p2)
    else:
      child.append(newGenes())
  return child

def main():
    count = 1
    aprxMatchFound = 0

    # Set of chromosomes
    chromosomes = [createChromosome() for i in range(100)]

    population = []

    # Create a dict with the values of how near they are
    for chromosome in chromosomes:
        population.append({
            "chromosome": chromosome,
            "value": valuation(chromosome)
        })

    # Check if there was a aproximate match found
    while not aprxMatchFound:
        population = sorted(population, key=lambda i : i['value'])
        print("Loss in gen", str(count),"-",str(population[0]['value']))
        # Show the evolution every 1000 generations
        if count % 1000 == 0:
            newImg = Image.new("RGB", (28, 28), "white")
            image = ImageDraw.Draw(newImg, 'RGBA')
            for ordinates in population[0]['chromosome']:
                image.rectangle(ordinates, (105,105,105,125))
            newImg.show()
        # Stop when the difference is about 15000
        if population[0]['value'] <= 15000:
            aprxMatchFound = 1
        newGen = []
        for i in range(10):
            newGen.append(population[i])
        # Generating random parents for mating
        for i in range(90):
            ch1 = choice(population[:50])
            ch2 = choice(population[:50])
            check = 0
            while ch1["chromosome"] == ch2["chromosome"] and check != len(population):
                ch2 = choice(population[:50])
                check += 1
            child = generateChildFrom(ch1["chromosome"], ch2["chromosome"])
            newGen.append({
                "chromosome": child,
                "value": valuation(child)
            })
        population = newGen

        count += 1

main()