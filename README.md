# Crossed Square Fractal




# Definition

Point ![p(x,y)](https://latex.codecogs.com/svg.latex?p(x,y)) is described by ![p_x](https://latex.codecogs.com/svg.latex?p_x) coordinate and ![p_y](https://latex.codecogs.com/svg.latex?p_y) coordinate.

Line ![l(p^a,p^b)](https://latex.codecogs.com/svg.latex?l(p^a,p^b)) is described by two points.

Triangle ![t(p^a,p^b,p^c)](https://latex.codecogs.com/svg.latex?t(p^a,p^b,p^c)) is described by tree points. Each triangle is ai sosceles right triangles by default. Points ![p^a](https://latex.codecogs.com/svg.latex?p^a) and ![p^b](https://latex.codecogs.com/svg.latex?p^b) are points of hypotenuse and ![p^c](https://latex.codecogs.com/svg.latex?p^c) is point of right angle.

Crossed Square Fractal ![cs_{n}\big(p^a,p^b\big)](https://latex.codecogs.com/svg.latex?cs_{n}\big(p^a,p^b\big)) of iteration ![n](https://latex.codecogs.com/svg.latex?n) is a matrix ![{2^{n-1}}\times{2^{n-1}}](https://latex.codecogs.com/svg.latex?{2^{n-1}}\times{2^{n-1}}) of Crossed Squares for total of ![{2^{n-1}}^2](https://latex.codecogs.com/svg.latex?{2^{n-1}}^2) Crossed Squares. By default ![p^a=p_{0,0}](https://latex.codecogs.com/svg.latex?p^a=p_{0,0}) and ![p^b=p_{1,1}](https://latex.codecogs.com/svg.latex?p^b=p_{1,1}). Simple Crossed Square is as Crossed Square Fractal of iteration ![1](https://latex.codecogs.com/svg.latex?1) - ![cs_{1}](https://latex.codecogs.com/svg.latex?cs_{1}). Crossed Square is a collection of figures: lines or triangles.

Crossed Squared Fractal on different iterations

n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8
:-:|---|---|---|---|---|---|---|---
image | <img src="data/CrossedSquare0_table_1.svg" width="128" height="128"/></td> | <img src="data/CrossedSquare0_table_2.svg" width="128" height="128"/></td> | <img src="data/CrossedSquare0_table_3.svg" width="128" height="128"/></td> | <img src="data/CrossedSquare0_table_4.svg" width="128" height="128"/></td> | <img src="data/CrossedSquare0_table_5.svg" width="128" height="128"/></td> | <img src="data/CrossedSquare0_table_6.svg" width="128" height="128"/></td> | <img src="data/CrossedSquare0_table_7.svg" width="128" height="128"/></td> | <img src="data/CrossedSquare0_table_8.svg" width="128" height="128"/></td>

There are several ways to build a Crossed Square Fractal of iteration ![n](https://latex.codecogs.com/svg.latex?n). ![cs_{n}](https://latex.codecogs.com/svg.latex?cs_{n}) is built by adding figures, transforming the existing ones or both.


## Crossed Square 0

<p align="center"><img src="data/a_CrossedSquare0_4.gif" width="256" height="256"/img></p>

![cs_{n}](https://latex.codecogs.com/svg.latex?cs_{n}) is built by CrossedSquare0 as follow:

1. Calculate constants: 
*	![num={2^{n-1}}](https://latex.codecogs.com/svg.latex?num={2^{n-1}}) - number of rows and cols in Crossed Square Fractal matrix;
*	![num_{h}=num+1](https://latex.codecogs.com/svg.latex?num_{h}=num+1) - number of horizontal lines;
*	![num_{v}=num+1](https://latex.codecogs.com/svg.latex?num_{v}=num+1) - number of vertical lines;
*	![num_{d0}=num-1](https://latex.codecogs.com/svg.latex?num_{d0}=num-1) - number of lines in main diagonal;
*	![num_{d1}=num-1](https://latex.codecogs.com/svg.latex?num_{d1}=num-1) - number of lines in side diagonal;
*	![step=1/num](https://latex.codecogs.com/svg.latex?step=1/num) - the step value between lines.

2. Calculate horizontal lines:

![l^{h}_{i}=l(p(0,i*step),p(1,i*step))](https://latex.codecogs.com/svg.latex?l^{h}_{i}=l(p(0,i*step),p(1,i*step))) for ![i=\overline{0,...,num_{h}}](https://latex.codecogs.com/svg.latex?i=\overline{0,...,num_{h}})

3. Calculate vertical lines: 

![l^{v}_{i}=l(p(i*step,0),p(i*step,1))](https://latex.codecogs.com/svg.latex?l^{v}_{i}=l(p(i*step,0),p(i*step,1))) for ![i=\overline{0,...,num_{v}}](https://latex.codecogs.com/svg.latex?i=\overline{0,...,num_{v}})

4. Calculate lines for main diagonal:

![l^{d0}_{0}=l(p(0,0),p(1,1))](https://latex.codecogs.com/svg.latex?l^{d0}_{0}=l(p(0,0),p(1,1)))

![\begin{bmatrix}l^{d0}_{i}\\l^{d0}_{num_{d0}+i}\end{bmatrix}=l^{d0}_{0}+\begin{bmatrix}l(p(0,i*step),p_{i*(-step),0})\\l(p(i*step,0),p(0,i*(-step)))\end{bmatrix}](https://latex.codecogs.com/svg.latex?\begin{bmatrix}l^{d0}_{i}\\\\l^{d0}_{num_{d0}+i}\end{bmatrix}=l^{d0}_{0}+\begin{bmatrix}l(p(0,i*step),p_{i*(-step),0})\\\\l(p(i*step,0),p(0,i*(-step)))\end{bmatrix}) for ![i=\overline{1,...,num_{d0}}](https://latex.codecogs.com/svg.latex?i=\overline{1,...,num_{d0}})

5. Calculate lines for side diagonal:

![l^{d1}_{0}=l(p_{1,0},p_{0,1})](https://latex.codecogs.com/svg.latex?l^{d1}_{0}=l(p_{1,0},p_{0,1}))

![\begin{bmatrix}l^{d1}_{i}\\l^{d1}_{num_{d1}+i}\end{bmatrix}=l^{d1}_{0}+\begin{bmatrix}l(p(i*(-step),0),p(0,i*(-step)))\\l(p(0,i*step),p(i*step,0))\end{bmatrix}](https://latex.codecogs.com/svg.latex?\begin{bmatrix}l^{d1}_{i}\\\\l^{d1}_{num_{d1}+i}\end{bmatrix}=l^{d1}_{0}+\begin{bmatrix}l(p(i*(-step),0),p(0,i*(-step)))\\\\l(p(0,i*step),p(i*step,0))\end{bmatrix}) for ![i=\overline{1,...,num_{d1}}](https://latex.codecogs.com/svg.latex?i=\overline{1,...,num_{d1}})

6. Collect all lines:

![cs_{n}=\left[l^{h},l^{v},l^{d0},l^{d1}\right]](https://latex.codecogs.com/svg.latex?cs_{n}=\left[l^{h},l^{v},l^{d0},l^{d1}\right])


## Crossed Square 1

<p align="center"><img src="data/a_CrossedSquare1_4.gif" width="256" height="256"/></p>

![cs^{scaled}_{n}](https://latex.codecogs.com/svg.latex?cs_{n}) is built by CrossedSquare1 as follow:

1. Calculate constants: 
*	![num={2^{n-1}}](https://latex.codecogs.com/svg.latex?num={2^{n-1}}) - number of rows and cols in Crossed Square Fractal matrix;
*	![step=1/num](https://latex.codecogs.com/svg.latex?step=1/num) - the step value between lines.

2. Calculate scaled Crossed Square of iteration ![1](https://latex.codecogs.com/svg.latex?1):

![cs_{1}=\begin{bmatrix}l(p(0.0,0.0),p(1.0,0.0))&l(p(1.0,0.0),p(1.0,1.0))&l(p(1.0,1.0),p(0.0,1.0))&l(p(0.0,1.0),p(0.0,0.0))\\l(p(0.0,0.0),p(0.5,0.5))&l(p(1.0,0.0),p(0.5,0.5))&l(p(1.0,1.0),p(0.5,0.5))&l(p(0.0,1.0),p(0.5,0.5))\end{bmatrix}](https://latex.codecogs.com/svg.latex?cs_{1}=\begin{bmatrix}l(p(0.0,0.0),p(1.0,0.0))&l(p(1.0,0.0),p(1.0,1.0))&l(p(1.0,1.0),p(0.0,1.0))&l(p(0.0,1.0),p(0.0,0.0))\\\\l(p(0.0,0.0),p(0.5,0.5))&l(p(1.0,0.0),p(0.5,0.5))&l(p(1.0,1.0),p(0.5,0.5))&l(p(0.0,1.0),p(0.5,0.5))\end{bmatrix})

![cs^{scaled}_{1}=step*cs_{1}](https://latex.codecogs.com/svg.latex?cs^{scaled}_{1}=step*cs_{1})

3. Collecting a matrix of scaled Crossed Squares:

![cs_{n}=\begin{Bmatrix}p(x,y)+cs^{scaled}_{1}|x=\overline{0.0,step,...,1.0-step},y=\overline{0.0,step,...,1.0-step}\end{Bmatrix}](https://latex.codecogs.com/svg.latex?cs_{n}=\begin{Bmatrix}p(x,y)+cs^{scaled}_{1}|x=\overline{0.0,step,...,1.0-step},y=\overline{0.0,step,...,1.0-step}\end{Bmatrix})


## Crossed Square 2

<p align="center"><img src="data/a_CrossedSquare2_4.gif" width="256" height="256"/></p>

![cs^{scaled}_{n}](https://latex.codecogs.com/svg.latex?cs_{n}) is built by CrossedSquare2 as follow:


## Crossed Square 3
<p align="center"><img src="data/a_CrossedSquare3_4.gif" width="256" height="256"/></p>


## Crossed Square 4
<p align="center"><img src="data/a_CrossedSquare4_4.gif" width="256" height="256"/></p>


## Crossed Square 5
<p align="center"><img src="data/a_CrossedSquare5_4.gif" width="256" height="256"/></p>

# How To Run It?
You can create environment by using file [environment.yml](environment.yml).

# TODO
- To implement the [svg_decode](crossedsquare.py#L100) method for the CrossedSquare class.

# Critic
It was more fast with pure numpy implementation, but less elegant. Is there any other method to define ![cs_{n}](cs_{n})? It is fractal, isn't it?
