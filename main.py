import torch

length = input()

array = []
mean = 0
for i in range(int(length)):
    array.append(int(input()))
    mean += array[i]
mean = mean / int(length)

array = torch.FloatTensor(array)
standard_deviation_tensor = torch.std(array)
standard_deviation = standard_deviation_tensor.item()

print("Normalization: ")
for i in range(int(length)):
    print(((array[i] - mean) / standard_deviation).item())

# https://atcold.github.io/pytorch-Deep-Learning/en/week02/02-2/
# Section Normalize the inputs to have zero mean and unit variance
