## Picker
### The problem
To take the bouquet designs and the stream of flowers as an input, and produce the stream of bouquets as
an output.
### The solution
The solution was inspired by the [greedy](https://en.wikipedia.org/wiki/Greedy_algorithm) algorithm solving 
the classical [Bin packing problem](https://en.wikipedia.org/wiki/Bin_packing_problem)

But it can be easily changed/extended to/with other algorithms, depending on business model.

Python was used based on the this [ranking](https://www.slant.co/topics/2469/~best-languages-for-writing-command-line-utilities).
### Installation
```bash
$ git clone
```
```bash
$ cd bouquets-cli
```
```bash
$ docker build -t bouquets .
```

### Usage
Help
```bash
$docker run --rm -it bouquets --help
```
Input from input file
```bash
$ docker run --rm -it bouquets --input_file input/input.txt
```
Without input file you have to provide a string divided by `\n` 
An example you can see in input/simple_input_string.txt
And output will be shown in the console
```bash
$ docker run --rm -it bouquets
```
With capacity limit you algorithm will stop when the storage is full
```bash
$ docker run --rm -it bouquets  --input_file input/input.txt --capacity 100 
```