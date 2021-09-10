# Crossed Square Fractal

# Definition

Point ![p(x,y)](https://latex.codecogs.com/svg.latex?p(x,y)) is described by ![p_x](https://latex.codecogs.com/svg.latex?p_x) coordinate and ![p_y](https://latex.codecogs.com/svg.latex?p_y) coordinate.

Line ![l(p^a,p^b)](https://latex.codecogs.com/svg.latex?l(p^a,p^b)) is described by two points.

Triangle ![t(p^a,p^b,p^c)](https://latex.codecogs.com/svg.latex?t(p^a,p^b,p^c)) is described by tree points. Each triangle is a isosceles right triangles by default. Points ![p^a](https://latex.codecogs.com/svg.latex?p^a) and ![p^b](https://latex.codecogs.com/svg.latex?p^b) are points of hypotenuse and ![p^c](https://latex.codecogs.com/svg.latex?p^c) is point of right angle.

Crossed Square Fractal ![cs_{n}\big(p^a,p^b\big)](https://latex.codecogs.com/svg.latex?cs_{n}\big(p^a,p^b\big)) of iteration ![n](https://latex.codecogs.com/svg.latex?n) is a matrix ![{2^{n-1}}\times{2^{n-1}}](https://latex.codecogs.com/svg.latex?{2^{n-1}}\times{2^{n-1}}) of Crossed Squares for total of ![{2^{2(n-1)}}](https://latex.codecogs.com/svg.latex?{2^{2(n-1)}}) Crossed Squares. By default ![p^a=p_{0,0}](https://latex.codecogs.com/svg.latex?p^a=p_{0,0}) and ![p^b=p_{1,1}](https://latex.codecogs.com/svg.latex?p^b=p_{1,1}). Simple Crossed Square is as Crossed Square Fractal of iteration ![1](https://latex.codecogs.com/svg.latex?1) - ![cs_{1}](https://latex.codecogs.com/svg.latex?cs_{1}). Crossed Square is a collection of figures: lines or triangles.

Crossed Squared Fractal on different iterations

n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8
:-:|---|---|---|---|---|---|---|---
image | <img src="data/CrossedSquare0_table_1.svg" width="128" height="128"/> | <img src="data/CrossedSquare0_table_2.svg" width="128" height="128"/> | <img src="data/CrossedSquare0_table_3.svg" width="128" height="128"/> | <img src="data/CrossedSquare0_table_4.svg" width="128" height="128"/> | <img src="data/CrossedSquare0_table_5.svg" width="128" height="128"/> | <img src="data/CrossedSquare0_table_6.svg" width="128" height="128"/> | <img src="data/CrossedSquare0_table_7.svg" width="128" height="128"/> | <img src="data/CrossedSquare0_table_8.svg" width="128" height="128"/>

There are several ways to build a Crossed Square Fractal of iteration ![n](https://latex.codecogs.com/svg.latex?n). ![cs_{n}](https://latex.codecogs.com/svg.latex?cs_{n}) is built by adding figures, transforming the existing ones or both.

name | CrossedSquare0 | CrossedSquare1 | CrossedSquare2 | CrossedSquare3 | CrossedSquare4 | CrossedSquare5
:-:|---|---|---|---|---|---
image | <img src="data/CrossedSquare0_4.svg" width="128" height="128"/> | <img src="data/CrossedSquare1_4.svg" width="128" height="128"/> | <img src="data/CrossedSquare2_4.svg" width="128" height="128"/> | <img src="data/CrossedSquare3_4.svg" width="128" height="128"/> | <img src="data/CrossedSquare4_4.svg" width="128" height="128"/> | <img src="data/CrossedSquare5_4.svg" width="128" height="128"/>


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

![l^{h}_{i}=l(p(0,{i}\cdot{step}),p(1,{i}\cdot{step}))](https://latex.codecogs.com/svg.latex?l^{h}_{i}=l(p(0,{i}\cdot{step}),p(1,{i}\cdot{step}))) for ![i=\overline{0,...,num_{h}}](https://latex.codecogs.com/svg.latex?i=\overline{0,...,num_{h}})

3. Calculate vertical lines: 

![l^{v}_{i}=l(p({i}\cdot{step},0),p({i}\cdot{step},1))](https://latex.codecogs.com/svg.latex?l^{v}_{i}=l(p({i}\cdot{step},0),p({i}\cdot{step},1))) for ![i=\overline{0,...,num_{v}}](https://latex.codecogs.com/svg.latex?i=\overline{0,...,num_{v}})

4. Calculate lines for main diagonal:

![l^{d0}_{0}=l(p(0,0),p(1,1))](https://latex.codecogs.com/svg.latex?l^{d0}_{0}=l(p(0,0),p(1,1)))

![\begin{bmatrix}l^{d0}_{i}\\l^{d0}_{num_{d0}+i}\end{bmatrix}=l^{d0}_{0}+\begin{bmatrix}l(p(0,{i}\cdot{step}),p_{{i}\cdot{(-step)},0})\\l(p({i}\cdot{step},0),p(0,{i}\cdot{(-step)}))\end{bmatrix}](https://latex.codecogs.com/svg.latex?\begin{bmatrix}l^{d0}_{i}\\l^{d0}_{num_{d0}+i}\end{bmatrix}=l^{d0}_{0}+\begin{bmatrix}l(p(0,{i}\cdot{step}),p_{{i}\cdot{(-step)},0})\\l(p({i}\cdot{step},0),p(0,{i}\cdot{(-step)}))\end{bmatrix}) for ![i=\overline{1,...,num_{d0}}](https://latex.codecogs.com/svg.latex?i=\overline{1,...,num_{d0}})

5. Calculate lines for side diagonal:

![l^{d1}_{0}=l(p_{1,0},p_{0,1})](https://latex.codecogs.com/svg.latex?l^{d1}_{0}=l(p_{1,0},p_{0,1}))

![\begin{bmatrix}l^{d1}_{i}\\l^{d1}_{num_{d1}+i}\end{bmatrix}=l^{d1}_{0}+\begin{bmatrix}l(p({i}\cdot{-step},0),p(0,{i}\cdot{-step}))\\l(p(0,{i}\cdot{step}),p({i}\cdot{step},0))\end{bmatrix}](https://latex.codecogs.com/svg.latex?\begin{bmatrix}l^{d1}_{i}\\\\l^{d1}_{num_{d1}+i}\end{bmatrix}=l^{d1}_{0}+\begin{bmatrix}l(p({i}\cdot{-step},0),p(0,{i}\cdot{-step}))\\\\l(p(0,{i}\cdot{step}),p({i}\cdot{step},0))\end{bmatrix}) for ![i=\overline{1,...,num_{d1}}](https://latex.codecogs.com/svg.latex?i=\overline{1,...,num_{d1}})

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

![cs^{scaled}_{1}={step}\cdot{cs_{1}}](https://latex.codecogs.com/svg.latex?cs^{scaled}_{1}={step}\cdot{cs_{1}})

3. Collecting a matrix of scaled Crossed Squares:

![cs_{n}=\begin{Bmatrix}p(x,y)+cs^{scaled}_{1}|x=\overline{0.0,step,...,1.0-step},y=\overline{0.0,step,...,1.0-step}\end{Bmatrix}](https://latex.codecogs.com/svg.latex?cs_{n}=\begin{Bmatrix}p(x,y)+cs^{scaled}_{1}|x=\overline{0.0,step,...,1.0-step},y=\overline{0.0,step,...,1.0-step}\end{Bmatrix})


## Crossed Square 2
<p align="center"><img src="data/a_CrossedSquare2_4.gif" width="256" height="256"/></p>

![cs^{scaled}_{n}](https://latex.codecogs.com/svg.latex?cs_{n}) is built by CrossedSquare2 as follow:

1. Crossed Square on iteration ![n=1](https://latex.codecogs.com/svg.latex?n=1) is:

![cs_{1}=\begin{bmatrix}l(p(0.0,0.0),p(1.0,0.0))&l(p(1.0,0.0),p(1.0,1.0))&l(p(1.0,1.0),p(0.0,1.0))\\l(p(0.0,1.0),p(0.0,0.0))&l(p(0.0,0.0),p(1.0,1.0))&l(p(1.0,0.0),p(0.0,0.1))\end{bmatrix}](https://latex.codecogs.com/svg.latex?cs_{1}=\begin{bmatrix}l(p(0.0,0.0),p(1.0,0.0))&l(p(1.0,0.0),p(1.0,1.0))&l(p(1.0,1.0),p(0.0,1.0))\\l(p(0.0,1.0),p(0.0,0.0))&l(p(0.0,0.0),p(1.0,1.0))&l(p(1.0,0.0),p(0.0,0.1))\end{bmatrix})

2. For each other iteration ![i=\overline{2,...,n}](https://latex.codecogs.com/svg.latex?i=\overline{2,...,n}) of Crossed Square next steps are repeating.

3. On iteration ![i](https://latex.codecogs.com/svg.latex?i) for each Crossed Square ![cs^{j}_{i-1},j=\overline{1,2,...,{2^{2(i-1)}}}](https://latex.codecogs.com/svg.latex?cs^{j}_{i-1},j=\overline{1,2,...,{2^{2(i-1)}}}) with center in ![p(x^{j}_{i-1},y^{j}_{i-1})](https://latex.codecogs.com/svg.latex?p(x^{j}_{i-1},y^{j}_{i-1})) in current matrix of Crossed Squares ![cs_{i-1}](https://latex.codecogs.com/svg.latex?cs_{i-1}), its translated (by ![p(-x^{j}_{i-1},-y^{j}_{i-1})](https://latex.codecogs.com/svg.latex?p(-x^{j}_{i-1},-y^{j}_{i-1})))scaled (by ![\sqrt{2}/{2}](https://latex.codecogs.com/svg.latex?\sqrt{2}/{2})), rotated (by ![45^{\circ}](https://latex.codecogs.com/svg.latex?45^{\circ})) and translated again (by ![p(x^{j}_{i-1},y^{j}_{i-1})](https://latex.codecogs.com/svg.latex?p(x^{j}_{i-1},y^{j}_{i-1}))) version is created:

![cs^{j,tsrt}_{i-1}=\begin{bmatrix}1&0&-x^{j}_{i-1}\\0&1&-y^{j}_{i-1}\\0&0&1\end{bmatrix}\cdot\begin{bmatrix}\frac{\sqrt{2}}{2}&0&0\\0&\frac{\sqrt{2}}{2}&0\\0&0&1\end{bmatrix}\cdot\begin{bmatrix}\cos(45^{\circ})&-\sin(45^{\circ})&0\\\sin(45^{\circ})&\cos(45^{\circ})&0\\0&0&1\end{bmatrix}\cdot{cs^{j}_{i-1}}\cdot\begin{bmatrix}1&0&x^{j}_{i-1}\\0&1&y^{j}_{i-1}\\0&0&1\end{bmatrix}=\begin{bmatrix}\frac{1}{2}&-\frac{1}{2}&-x^{j}_{i-1}\\\frac{1}{2}&\frac{1}{2}&-y^{j}_{i-1}\\0&0&1\end{bmatrix}\cdot{cs^{j}_{i-1}}\cdot\begin{bmatrix}1&0&x^{j}_{i-1}\\0&1&y^{j}_{i-1}\\0&0&1\end{bmatrix}](https://latex.codecogs.com/svg.latex?cs^{j,tsrt}_{i-1}=\\begin{bmatrix}1&0&-x^{j}_{i-1}\\\\0&1&-y^{j}_{i-1}\\\\0&0&1\\end{bmatrix}\\cdot\\begin{bmatrix}\\frac{\\sqrt{2}}{2}&0&0\\\\0&\\frac{\\sqrt{2}}{2}&0\\\\0&0&1\\end{bmatrix}\\cdot\\begin{bmatrix}\\cos(45^{\\circ})&-\\sin(45^{\\circ})&0\\\\\\sin(45^{\\circ})&\\cos(45^{\\circ})&0\\\\0&0&1\\end{bmatrix}\\cdot{cs^{j}_{i-1}}\\cdot\\begin{bmatrix}1&0&x^{j}_{i-1}\\\\0&1&y^{j}_{i-1}\\\\0&0&1\\end{bmatrix}=\\begin{bmatrix}\\frac{1}{2}&-\\frac{1}{2}&-x^{j}_{i-1}\\\\\\frac{1}{2}&\\frac{1}{2}&-y^{j}_{i-1}\\\\0&0&1\\end{bmatrix}\\cdot{cs^{j}_{i-1}}\\cdot\\begin{bmatrix}1&0&x^{j}_{i-1}\\\\0&1&y^{j}_{i-1}\\\\0&0&1\\end{bmatrix})

4. Each ![cs^{j,tsrt}_{i-1}](https://latex.codecogs.com/svg.latex?cs^{j,tsrt}_{i-1}) is inscribing into its original ![cs^{j}_{i-1}](https://latex.codecogs.com/svg.latex?cs^{j}_{i-1}) and four Crossed Squares are recieved by this operation. Finally ![cs_{i}](https://latex.codecogs.com/svg.latex?cs_{i}) is collected:

![cs_{i}=\begin{Bmatrix}{cs^{j}_{i-1}}\cap{cs^{j,tsrt}_{i-1}}|j=\overline{1,2,...,{2^{2(i-1)}}}\end{Bmatrix}](https://latex.codecogs.com/svg.latex?cs_{i}=\begin{Bmatrix}{cs^{j}_{i-1}}\cap{cs^{j,tsrt}_{i-1}}|j=\overline{1,2,...,{2^{2(i-1)}}}\end{Bmatrix})

Note: The [CrossedSquare2](crossedsquare.py#L188) implementation is a little bit different but the ideas behind it is described here. Also in some equations matrix of lines is a vector of line points in homogeneous coordinates.

## Crossed Square 3
<p align="center"><img src="data/a_CrossedSquare3_4.gif" width="256" height="256"/></p>

CrossedSquare3 is differ from CrossedSquare2 by ![cs_{1}](https://latex.codecogs.com/svg.latex?cs_{1}) definition:

![cs_{1}=\begin{bmatrix}l(p(0.5,0.0),p(0.0,0.0))&l(p(0.5,0.0),p(1.0,0.0))&l(p(1.0,0.5),p(1.0,1.0))&l(p(0.5,1.0),p(0.0,1.0))\\l(p(0.5,0.5),p(0.0,0.0))&l(p(0.5,0.5),p(1.0,0.0))&l(p(0.5,5.0),p(1.0,1.0))&l(p(0.5,0.5),p(0.0,1.0))\\l(p(0.0,0.5),p(0.0,0.0))&l(p(1.0,0.5),p(1.0,0.0))&l(p(0.5,1.0),p(1.0,1.0))&l(p(0.0,0.5),p(0.0,1.0))\end{bmatrix}](https://latex.codecogs.com/svg.latex?cs_{1}=\begin{bmatrix}l(p(0.5,0.0),p(0.0,0.0))&l(p(0.5,0.0),p(1.0,0.0))&l(p(1.0,0.5),p(1.0,1.0))&l(p(0.5,1.0),p(0.0,1.0))\\\\l(p(0.5,0.5),p(0.0,0.0))&l(p(0.5,0.5),p(1.0,0.0))&l(p(0.5,5.0),p(1.0,1.0))&l(p(0.5,0.5),p(0.0,1.0))\\\\l(p(0.0,0.5),p(0.0,0.0))&l(p(1.0,0.5),p(1.0,0.0))&l(p(0.5,1.0),p(1.0,1.0))&l(p(0.0,0.5),p(0.0,1.0))\end{bmatrix})


## Crossed Square 4
<p align="center"><img src="data/a_CrossedSquare4_4.gif" width="256" height="256"/></p>

![cs_{n}](https://latex.codecogs.com/svg.latex?cs_{n}) is built by CrossedSquare4 as follow:

1. ![cs_{1}](https://latex.codecogs.com/svg.latex?cs_{1}) Crossed Square of iteration ![1](https://latex.codecogs.com/svg.latex?1) is a set of triangles:

![cs_{1}=\begin{bmatrix}t(p(0.0,0.0),p(1.0,0.0)p(0.5,0.5))&t(p(1.0,0.0),p(1.0,1.0)p(0.5,0.5))\\t(p(1.0,1.0),p(0.0,1.0)p(0.5,0.5))&t(p(0.0,1.0),p(0.0,0.0)p(0.5,0.5))&\end{bmatrix}](https://latex.codecogs.com/svg.latex?cs_{1}=\begin{bmatrix}t(p(0.0,0.0),p(1.0,0.0)p(0.5,0.5))&t(p(1.0,0.0),p(1.0,1.0)p(0.5,0.5))\\\\t(p(1.0,1.0),p(0.0,1.0)p(0.5,0.5))&t(p(0.0,1.0),p(0.0,0.0)p(0.5,0.5))&\end{bmatrix})

2. For each other iteration ![i=\overline{2,...,n}](https://latex.codecogs.com/svg.latex?i=\overline{2,...,n}) of Crossed Square next steps are repeating.

3. On iteration ![i](https://latex.codecogs.com/svg.latex?i) each triangle ![t(p^{j,a}_{i-1},p^{j,b}_{i-1},p^{j,c}_{i-1}),j=\overline{1,2,...,2^{2(i-1)}}](https://latex.codecogs.com/svg.latex?t(p^{j,a}_{i-1},p^{j,b}_{i-1},p^{j,c}_{i-1}),j=\overline{1,2,...,2^{2(i-1)}}) of Crossed Square ![cs_{i-1}](https://latex.codecogs.com/svg.latex?cs_{i-1}) is splited two times:

3.1. Calculate points of triangle sides middles:

![p^{j,mab}_{i-1}=p^{j,a}_{i-1}+\frac{p^{j,a}_{i-1}-p^{j,b}_{i-1}}{2}](https://latex.codecogs.com/svg.latex?p^{j,mab}_{i-1}=p^{j,a}_{i-1}+\frac{p^{j,a}_{i-1}-p^{j,b}_{i-1}}{2})

![p^{j,mbc}_{i-1}=p^{j,b}_{i-1}+\frac{p^{j,b}_{i-1}-p^{j,c}_{i-1}}{2}](https://latex.codecogs.com/svg.latex?p^{j,mbc}_{i-1}=p^{j,b}_{i-1}+\frac{p^{j,b}_{i-1}-p^{j,c}_{i-1}}{2})

![p^{j,mca}_{i-1}=p^{j,c}_{i-1}+\frac{p^{j,c}_{i-1}-p^{j,a}_{i-1}}{2}](https://latex.codecogs.com/svg.latex?p^{j,mca}_{i-1}=p^{j,c}_{i-1}+\frac{p^{j,c}_{i-1}-p^{j,a}_{i-1}}{2})

3.2. Calculate new triangles:

![\begin{bmatrix}t^{k={4}\cdot{j}+0}_{i}\\t^{k={4}\cdot{j}+1}_{i}\\t^{k={4}\cdot{j}+2}_{i}\\t^{k={4}\cdot{j}+3}_{i}\end{bmatrix}=\begin{bmatrix}t(p^{j,a}_{i-1},p^{j,mab}_{i-1},p^{j,mca}_{i-1})\\t(p^{j,b}_{i-1},p^{j,mab}_{i-1},p^{j,mbc}_{i-1})\\t(p^{j,c}_{i-1},p^{j,mab}_{i-1},p^{j,mca}_{i-1})\\t(p^{j,c}_{i-1},p^{j,mab}_{i-1},p^{j,mbc}_{i-1})\end{bmatrix}](https://latex.codecogs.com/svg.latex?\begin{bmatrix}t^{k={4}\cdot{j}+0}_{i}\\\\t^{k={4}\cdot{j}+1}_{i}\\\\t^{k={4}\cdot{j}+2}_{i}\\\\t^{k={4}\cdot{j}+3}_{i}\end{bmatrix}=\begin{bmatrix}t(p^{j,a}_{i-1},p^{j,mab}_{i-1},p^{j,mca}_{i-1})\\\\t(p^{j,b}_{i-1},p^{j,mab}_{i-1},p^{j,mbc}_{i-1})\\\\t(p^{j,c}_{i-1},p^{j,mab}_{i-1},p^{j,mca}_{i-1})\\\\t(p^{j,c}_{i-1},p^{j,mab}_{i-1},p^{j,mbc}_{i-1})\end{bmatrix})

4. Empy Crossed Square ![cs_{i}](https://latex.codecogs.com/svg.latex?cs_{i}) collects triangles ![t^{k}_{i}](https://latex.codecogs.com/svg.latex?t^{k}_{i}):

![cs_{i}=\begin{Bmatrix}t^{k}_{i}|i=\overline{1,...,2^{2i}}\end{Bmatrix}](https://latex.codecogs.com/svg.latex?cs_{i}=\begin{Bmatrix}t^{k}_{i}|k=\overline{1,...,2^{2i}}\end{Bmatrix})


## Crossed Square 5
<p align="center"><img src="data/a_CrossedSquare5_4.gif" width="256" height="256"/></p>

CrossedSquare5 is a combination of CrossedSquare4 and CrossedSquare2 (step 3. and step 4.). After steps 2.-4. from CrossedSquare4 we perform step 3. and 4. from CrossedSquare2, but we put another translated-scaled-rotated-translated Crossed Square on its original instead of inscribing it into the last one. So there is a ![n](https://latex.codecogs.com/svg.latex?n) layers of overlapping triangles in ![cs_{n}](https://latex.codecogs.com/svg.latex?cs_{n}).

number of layers | number of triangles in layer
:-: | :-:
1 | 4
1 2 | 8 8
1 2 3 | 16 32 16
1 2 3 4 | 32 96 96 32
1 2 3 4 5 | 64 256 386 256 64
1 2 3 4 5 6 | 128 640 1280 1280 640 128
1 2 3 4 5 6 7 |256 1536 3840 5120 3840 1536 256
1 2 3 4 5 6 7 8 | 512 3584 10752 17920 17920 10752 3584 512

# How To Run It?
You can create environment by using file [environment.yml](requirements.txt).

# TODO
- To implement the [svg_decode](crossedsquare.py#L100) method for the CrossedSquare class.

# Critic
It was more fast with pure numpy implementation, but less elegant. Is there any other method to define ![cs_{n}](https://latex.codecogs.com/svg.latex?cs_{n})? It is fractal, isn't it?
