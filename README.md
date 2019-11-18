# dijkstra

The following is an implementation of Dijkstra's algorithm.

## Usage

To use it you can do one of the following:

### 1. Using Docker (preferred)

#### Prerequsites

[Docker](https://docs.docker.com/v17.09/engine/installation/)

#### Running it:

> You could get the image from [dockerhub](https://hub.docker.com/r/danisnowman/dijkstra/builds)

We build the image:

```bash

docker build --rm -f "dockerfile" -t dijkstra:latest .

```

Followed by:

```bash

docker run -it dijkstra:latest  

```

### 2. Using Python

Running the app:

```bash

python app.py

```
