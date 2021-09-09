# Crossed Square Fractal



# Definition

Point ![p_{x,y}](https://latex.codecogs.com/svg.latex?p_{x,y}) is described by ![p_x](https://latex.codecogs.com/svg.latex?p_x) coordinate and ![p_y](https://latex.codecogs.com/svg.latex?p_y) coordinate.

Line ![l(p^a,p^b)](https://latex.codecogs.com/svg.latex?l(p^a,p^b)) is described by two points.

Triangle ![t(p^a,p^b,p^c)](https://latex.codecogs.com/svg.latex?t(p^a,p^b,p^c)) is described by tree points. Each triangle is ai sosceles right triangles by default. Points ![p^a](https://latex.codecogs.com/svg.latex?p^a) and ![p^b](https://latex.codecogs.com/svg.latex?p^b) are points of hypotenuse and ![p^c](https://latex.codecogs.com/svg.latex?p^c) is point of right angle.

Crossed Square Fractal ![cs_{n}\big(p^a,p^b\big)](https://latex.codecogs.com/svg.latex?cs_{n}\big(p^a,p^b\big)) of iteration ![n](https://latex.codecogs.com/svg.latex?n) is a matrix ![{2^{n-1}}\times{2^{n-1}}](https://latex.codecogs.com/svg.latex?{2^{n-1}}\times{2^{n-1}}) of Crossed Squares for total of ![{2^{n-1}}^2](https://latex.codecogs.com/svg.latex?{2^{n-1}}^2) Crossed Squares. By default ![p^a=p_{0,0}](https://latex.codecogs.com/svg.latex?p^a=p_{0,0}) and ![p^b=p_{1,1}](https://latex.codecogs.com/svg.latex?p^b=p_{1,1}). Simple Crossed Square is as Crossed Square Fractal of iteration ![1](https://latex.codecogs.com/svg.latex?1) - ![cs_{1}](https://latex.codecogs.com/svg.latex?cs_{1}). Crossed Square is a collection of figures: lines or triangles.

Crossed Squared Fractal on different iterations

n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8
:-:|---|---|---|---|---|---|---|---
image | <img src="data/CrossedSquare0_table_1.svg" width="128" height="128"/></td> | <img src="data/CrossedSquare0_table_2.svg" width="128" height="128"/></td> | <img src="data/CrossedSquare0_table_3.svg" width="128" height="128"/></td> | <img src="data/CrossedSquare0_table_4.svg" width="128" height="128"/></td> | <img src="data/CrossedSquare0_table_5.svg" width="128" height="128"/></td> | <img src="data/CrossedSquare0_table_6.svg" width="128" height="128"/></td> | <img src="data/CrossedSquare0_table_7.svg" width="128" height="128"/></td> | <img src="data/CrossedSquare0_table_8.svg" width="128" height="128"/></td>

There are several ways to build a Crossed Square Fractal of iteration ![n](https://latex.codecogs.com/svg.latex?n). ![cs_{n}](https://latex.codecogs.com/svg.latex?cs_{n}) is built by adding figures, transforming the exist ones or both.



## Crossed Square 0 

![cs_{n}](https://latex.codecogs.com/svg.latex?cs_{n}) is built by CrossedSquare0 as follow:

1. Calculate constants: 
*	![num={2^{n-1}}](https://latex.codecogs.com/svg.latex?num={2^{n-1}}) - number of rows and cols in Crossed Square Fractal matrix; 
*	![num_{h}=num+1](https://latex.codecogs.com/svg.latex?num_{h}=num+1) - number of horizontal lines; 
*	![num_{v}=num+1](https://latex.codecogs.com/svg.latex?num_{v}=num+1) - number of vertical lines; 
*	![num_{d0}=num-1](https://latex.codecogs.com/svg.latex?num_{d0}=num-1) - number of lines in main diagonal; 
*	![num_{d1}=num-1](https://latex.codecogs.com/svg.latex?num_{d1}=num-1) - number of lines in side diagonal; 
*	![step=1/num](https://latex.codecogs.com/svg.latex?step=1/num) - the step value between lines.

2. Add horizontal lines:

![l_{i}(p_{0,i*step},p_{1,i*step})](https://latex.codecogs.com/svg.latex?l_{i}(p_{0,i*step},p_{1,i*step})) for ![i=\overline{0,...,num_{h}}](https://latex.codecogs.com/svg.latex?i=\overline{0,...,num_{h}})

3. Add vertical lines: 

![l_{i}(p_{i*step,0},p_{i*step,1})](https://latex.codecogs.com/svg.latex?l_{i}(p_{i*step,0},p_{i*step,1})) for ![i=\overline{0,...,num_{v}}](https://latex.codecogs.com/svg.latex?i=\overline{0,...,num_{v}})

4. Add lines for main diagonal:

![l_{0}=l(p_{0,0},p_{1,1})](https://latex.codecogs.com/svg.latex?l_{0}=l(p_{0,0},p_{1,1}))

![l_{i}=l_{0}+\begin{bmatrix}l(p_{0,i*step},p_{i*(-step),0})\\l(p_{i*step,0},p_{0,i*(-step)})\end{bmatrix}](https://latex.codecogs.com/svg.latex?l_{i}=l_{0}+\begin{bmatrix}l(p_{0,i*step},p_{i*(-step),0})\\\\l(p_{i*step,0},p_{0,i*(-step)})\end{bmatrix}) for ![i=\overline{1,...,num_{d0}}](https://latex.codecogs.com/svg.latex?i=\overline{1,...,num_{d0}})

5. Add lines for side diagonal:

![l_{0}=l(p_{1,0},p_{0,1})](https://latex.codecogs.com/svg.latex?l_{0}=l(p_{1,0},p_{0,1}))

![l_{i}=l_{0}+\begin{bmatrix}l(p_{i*(-step),0},p_{0,i*(-step)})\\l(p_{0,i*step},p_{i*step,0})\end{bmatrix}](https://latex.codecogs.com/svg.latex?l_{i}=l_{0}+\begin{bmatrix}l(p_{i*(-step),0},p_{0,i*(-step)})\\l(p_{0,i*step},p_{i*step,0})\end{bmatrix}) for ![i=\overline{1,...,num_{d1}}](https://latex.codecogs.com/svg.latex?i=\overline{1,...,num_{d1}})

<img src="data/a_CrossedSquare0_4.gif" width="256" height="256"/>



## Crossed Square 1
<img src="data/a_CrossedSquare1_4.gif" width="256" height="256"/>



## Crossed Square 2
<img src="data/a_CrossedSquare2_4.gif" width="256" height="256"/>



## Crossed Square 3
<img src="data/a_CrossedSquare3_4.gif" width="256" height="256"/>



## Crossed Square 4
<img src="data/a_CrossedSquare4_4.gif" width="256" height="256"/>



## Crossed Square 5
<img src="data/a_CrossedSquare5_4.gif" width="256" height="256"/>



# How To Run It?
You can create environment by using file [environment.yml](environment.yml).



# TODO
- To implement the [svg_decode](crossedsquare.py#L100) method for the CrossedSquare class.



# Critic
It was more fast with pure numpy implementation, but less elegant. Is there any other method to define ![cs_{n}](cs_{n})? It is fractal, isn't it?
