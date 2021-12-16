# Genetic Algorithm
An AI program to build an image from scratch using genetic algorithm.

## Inputs and Hyperparameters:
* 28X28, color image of an apple in .png format.
* Loss Threshold is consisdered to be 15000.
* Intial set of chromosomes = 100.


## Procedure to view the output:
* Download the "apple.png" image to the directory where the pattern_recognition.py file is present.
* Incase the path or the image is change update the path in the code on line 28.
```
origImg = Image.open('apple.png').load()
```

## Output:
* The loss for every generation is prited until the loss reaches the threshhold.
* A 28X28 image with RGBA value of (105,105,105,125) is displayed in .hiec format for every 1000 generations.
* The frequency to view the output image can be changed on line 88.
```
if count % 1000 == 0:
```

### to run the code 
``` 
python3 genetic_algo.py
```