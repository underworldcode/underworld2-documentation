

$$
\require{color}
\newcommand{\dGamma}{\mathbf{d}\boldsymbol{\Gamma}}
\newcommand{\erfc}{\mbox{\rm erfc}}
\newcommand{\curly}{\sf }
\newcommand{\Red}[1]{\textcolor[rgb]{0.7,0.0,0.0}{ \#1}}
\newcommand{\Green}[1]{\textcolor[rgb]{0.0,0.7,0.0}{ \#1}}
\newcommand{\Blue}[1]{\textcolor[rgb]{0.0,0.0,0.7}{ \#1}}
\newcommand{\Emerald}[1]{\textcolor[rgb]{0.0,0.7,0.3}{ \#1}}
\newcommand{\curly}
$$



## Solving the matrix problem

Once the problem has been rendered into a matrix form, the finite element part is over !  The rest is matrix algebra. There are a number of standard techniques for solving such systems which we briefly outline in the context of the Earth dynamics problem. In most dynamic systems, the FEM can be formulated in a time-explicit manner (cf discrete element methods) that is robust and simple to implement, or using implicit methods which are more elaborate and are often more temperamental but which are capable of covering much larger time increments at each step. In our case, however, the fact that inertia is negligible, leaves the equation of motion independent of time and it can only be solved implicitly.

The original implicit solver in FEM was to build the matrix equation and solve it directly using an method such as Crout elimination. This can be done relatively efficiently by exploiting the fact that the finite element matrices are quite tightly banded.  Unfortunately, direct solution methods are limited to "small" problems since the solution-time scales very rapidly with the number of unknowns (in the worst case, as $N^3$ where $N$ is the number of unknowns, and even in the best case as $N^2$).

Iterative methods can achieve much better performance than this once the problems start to become larger. For example, preconditioned conjugate gradient methods can obtain a solution to a given accuracy in a time proportional to $N\log N$. However, preconditioning can be highly time consuming and may need careful tailoring for different problems as the iterations may not converge (compare this to our need to carefully choose how to discretise problems in our finite difference examples earlier)

The optimal method, in theory, for the Stokes problem is _multigrid_ which, when properly formulated, can find a solution in a time proportional to $N$.

An additional problem arises with direct methods. The number of unknowns in the vector $\mathbf{d}$ is slightly less than $n_{\rm dim}$ times the number of nodal points once the prescribed boundary velocities have been included. For a well-resolved problem the stiffness matrix $\mathbf{K}$ is often too large to be stored in full, even accounting for its sparsity. Some iterative methods can operate with only the element stiffness matrices which can be built and used on the fly. Although this requires significantly more computations, it can make some large problems soluble where otherwise memory limitations would block solution. It is also possible that computation can be more efficient than retrieving carefully-packed matrix coefficents and, in this case, element-by-element methods can be competitive for speed in their own right.  

Some simple iterative schemes  **for positive definite systems** are described next. Far more that this exist and many are more efficient but this usually depends on the actual application area.

### Jacobi relaxation

One of the simplest iterative methods of residual reduction is the Jacobi iteration. Given an approximate solution, $\mathbf{d}^{(0)}$, to $\mathbf{Kd}=\mathbf{f}$, an improved solution, $ \mathbf{d}^{(1)}$ is found by

\begin{equation}
  d _ i^{(1)} = \left( f _ i - \sum^{n} _ {j=1;j\not=i} k _ {ij}d_j^{(0)} \right) / k _ {ii} \nonumber
\end{equation}

It is clear that each iteration cycle requires only one matrix-vector multiplication. However, the convergence rate for this algorithm is usually poor and a large number of cycles is required.

### Gauss-Seidel relaxation

A trivial modification to the Jacobi iteration is to use updated information on the $\mathbf{d}$ componenents immediately they become available. This results in the Gauss-Seidel iteration which is considerably more efficient than Jacobi. It can, however, be harder to code efficiently because the independence of each degree of freedom during one iteration disappears.

### Conjugate Gradients

A more sophisticated iterative procedure for obtaining solutions to linear systems is the conjugate gradient method. This is a development of the method of steepest descent with better convergence properties. The 'search directions' along which the solution is improved are denoted by $\mathbf{s}$ and do not coincide with the residual vectors. In the following algorithm an inner product is denoted by $(\cdot,\cdot)$.

<!-- Not ideal - especially with the spaces etc, but I don't know a latex / pseudo code mode that works -->

   1.  $k=0; \mathbf{u}_0 = {\bf 0}; \mathbf{r}_0 = \mathbf{f}$  
   2.  while $(\mathbf{r}_k \not= {\bf 0})$
   3.  &emsp;  $k = k + 1$
   4.  &emsp;  if $(k=1)$  
   5.  &emsp;  &emsp; $\mathbf{s}_1 = \mathbf{r}_0$
   6.  &emsp;  else  
   7.  &emsp;  &emsp;   $\beta = (\mathbf{r} _ {k-1},\mathbf{r} _ {k-1})/(\mathbf{r} _ {k-2},\mathbf{r} _ {k-2})$
   8.  &emsp;  &emsp;   $\mathbf{s} _ k = \mathbf{r} _ {k-1} + \beta \mathbf{s} _ {k-1}$
   9.  &emsp;  end
   10. &emsp;  $\alpha = (\mathbf{r} _ {k},\mathbf{r} _ {k})/(\mathbf{s} _ {k},{\bf A s} _ {k})$
   11. &emsp;  $\mathbf{u} _ k = \mathbf{u} _ {k-1} + \alpha \mathbf{s} _ {k}$
   12. &emsp;  $\mathbf{r} _ k = \mathbf{r} _ {k-1} - \alpha {\bf As} _ {k}$
   13. end
   14. $\mathbf{u} = \mathbf{u} _ k$


In this case the use of residual vectors from previous iteration steps is necessary to ensure that there is only one matrix-vector multiplication. The convergence of the conjugate gradient algorithm is fastest when $\mathbf{K}$ is close to the identity matrix. For a general matrix the reduction of the residual may be  slow through the first few iterations then picks up speed as the procedure progresses. This property makes this iterative loop inefficient for relatively small numbers of iterations.

Note that the reduction of the residual is a measure of "improvement" of the solution which is internal to the iteration. Although the magnitude of the residual is usually reduced monotonically, the true error, when it can be calculated, may increase as well as decrease. In order to improve the rate of convergence it is necessary to reformulate the problem such that the solution to a _nearly diagonal_ system is sought. This procedure is known as preconditioning. The system $\mathbf{Kd} = \mathbf{f}$ is transformed to a case which can be solved more rapidly by the conjugate gradient algorithm:

\begin{equation}
    \tilde{\mathbf{K}}\tilde{\mathbf{u}} = \tilde{\mathbf{f}} \nonumber
  \end{equation}

where

\begin{align\*}
      \tilde{\mathbf{K}} &= {\bf C}^{-1}\mathbf{K} {\bf C}^{-1} \\\\
      \tilde{\mathbf{u}} &= {\bf Cu}   \\\\
      \tilde{\mathbf{f}} &= {\bf C}^{-1} {\bf b}
\end{align\*}

The preconditioning matrix $\bf M$ is defined by ${\bf M} = {\bf C}^2$, and  the preconditioned
conjugate gradient algorithm is then:

1.      $ k = 0; \mathbf{u}_0 = {\bf 0}; \mathbf{r}_0 = \mathbf{f}$  
2.      while $(\mathbf{r}_k \not= {\bf 0})$  
3.      &emsp;  _solve_ ${\bf M z}_k = \mathbf{r}_k$
4.      &emsp;  $ k = k + 1 $
5.      &emsp;  if $(k=1)$  
6.      &emsp;  &emsp; $ \mathbf{s}_1 = {\bf z}_0$
7.      &emsp;  else
8.      &emsp;  &emsp;  $\beta = (\mathbf{r} _ {k-1},{\bf z} _ {k-1})/(\mathbf{r} _ {k-2},{\bf z} _ {k-2})$
9.      &emsp;  &emsp;  $\mathbf{s} _ k = {\bf z} _ {k-1} + \beta \mathbf{s} _ {k-1}$
10.     &emsp;  end
11.     &emsp;  $\alpha = (\mathbf{r} _ {k},{\bf z} _ {k})/(\mathbf{s} _ {k},{\bf A s} _ {k})$
12.     &emsp;  $\mathbf{d} _ k = \mathbf{d} _ {k-1} + \alpha \mathbf{s} _ {k}$
13.     &emsp;  $\mathbf{r} _ k = \mathbf{r} _ {k-1} - \alpha \mathbf{Ks} _ {k}$
14.     end
15.     $\mathbf{d} = \mathbf{d}_k$


The choice of $\bf M$ has a dramatic effect on the rate of convergence of the method. Not only must the preconditioner improve the convergence properties of the system, but the solution to ${\bf Mz} = \mathbf{r}$ must be inexpensive. Clearly if ${\bf M} = \mathbf{K}$ then exact convergence is obtained in one iteration but the solution of the preconditioning step becomes impossible. The simplest preconditioner, and the one employed here, is to set ${\bf M} = \mathrm{diag}(\mathbf{K})$. This is not only simple to calculate (and invert) but requires very little storage. For simple systems the reduction of the residual is noticeably improved during the initial iterations. However, it is not clear how well this simple preconditioner will work when strong viscosity contrasts are present and off-diagonal terms in $\mathbf{K}$ may be large.

### Multigrid

---

![](../Diagrams/mg.png){. width="50%" id="multigrid-diagram"}

*Multigrid: (a) Error reduction during simple two level V cycle, (b) Shape functions on different grid scales, (c) V cycle on four grids, (d) W cycle on four grids, (e) Schematic of Full Multigrid V cycles*

---

The multigrid method works by formulating the finite element problem on a number of different scales - usually a set of grids which are nested one within the other sharing common nodes.  The solution progresses on all of the grids at the same time with each grid eliminating errors at a different scale. The effect is to propagate information very rapidly between different nodes in the grid which would otherwise be prevented by the local support of the element shape functions. In fact, by a single traverse from fine to coarse grid and back, all nodes in the mesh can be directly connected to every other - allowing nodes which are physically coupled but remote in the mesh to communicate directly during each iteration cycle.

The multigrid effect relies upon using an iterative solver on each of the grid resolutions which acts like a smoother on the residual error at the characteristic scale of that particular grid. People commonly use Gauss-Seidel iteration because it has exactly this property. On the coarsest grid it is possible to use a direct solver because the number of elements is usually very small.

For an elliptic operator such as the Laplacian of the Stokes' problem encountered in the algorithm above the discretized problem is now written

\begin{equation\*}
  {\bf K}_h {\bf d}_h = {\bf f}_h
\end{equation\*}

where  the $h$ subscript indicates that the problem has been discretized to a mesh of fineness $h$.  As before an initial estimate of the velocity can be improved by determining the solution to

\begin{equation\*}
  {\bf K}_h \delta {\bf d}_h = {\bf r}_h
\end{equation\*}

where ${\bf r}_h$ is the residual on this mesh, and $\delta {\bf d}$ is a correction to $\bf d$ which reduces $\bf r$. In the iterative methods described above, the initial approximation and the correction are found by solving a simplified version of the problem at the same gridpoints in such a way that computation time is reduced dramatically. However, another approach to the problem is to obtain an approximate solution by solving the problem on a more coarse grid. The reduction of the number of degrees of freedom also leads to a more manageable problem which can be solved fast. The correction term is therefore:

\begin{equation\*}
  {\bf K}_H \delta{\bf d}_H = {\bf r}_H
\end{equation\*}

where $H$ indicates a coarser level of discretization. The residual on the coarser mesh is determined by the use of a projection (restriction) operator:

\begin{equation\*}
  {\bf r}_H = {\bf P}_H^h {\bf r}_h
\end{equation\*}

and the approximate solution is then interpolated from the coarse to fine grid using an interpolation operator:

\begin{equation\*}
  \delta{\bf d}_h = {\bf I}_H^h \delta{\bf d}_H
\end{equation\*}

The power of the algorithm is in a recursive application. The coarse grid correction is also calculated through the use of a still-coarser grid and so on, until the problem is so small that an exact solution can be obtained very rapidly. One very simple, but instructive, algorithm for hierarchical residual reduction is the sawtooth cycle (the same logical layout as the [multigrid V cycle](#multigrid-diagram)).


      1. Obtain approximate solution, ${\bf d}_h$ at highest level $h$
      2. Calculate residual: ${\bf r}_h = {\bf f}_h - {\bf K}_h {\bf d}_h$
      3. Project residual by N levels to level $h-N$
      4. &emsp;  ${\bf r} _ {h-i} = {\bf  P} _ {h-i}^{h-i+1} {\bf r} _ {h-i+1}$
      5. Solve exactly: $\delta {\bf u} _ {h-N} = {\bf A} _ {h-N} {\bf r} _ {h-N}$
      6. Interpolation steps:
      7. &emsp;  ${\bf r} _ {h-i+1} += {\bf I} _ {h-i}^{h-i+1} {\bf K} _ {h-i} \delta {\bf d} _ {h-i}$  
      8. &emsp;  Improve $\delta {\bf d} _ {h-i+1}$  
      9.  ${\bf d} _ h += \delta {\bf d} _ h$


The step in which the velocity correction is "improved" is an iterative method for reducing the residual at the current level such as those described above. Although many methods of residual reduction are available, the class of methods which often work best with the multigrid approach are relaxation iterations which are also effective *smoothing* operators. At each level the smoothing operators reduce the residual most strongly on the scale  of the discretization - the hierarchical nesting of different mesh sizes allows the residual to be reduced at each scale very efficiently. (see Parsons and Hall).  The Jacobi relaxation above is a suitable algorithm for multigrid enhancement but still converges too slowly to build into an efficient code. Preconditioned conjugate gradient methods can better reduce the residual for the same number of operations but may not possess the smoothing properties which benefit the multigrid approach. The local inverse method appears to have both the smoothing and rapid convergence properties for the Stokes' problem which are required for effective multigridding.

The projection and interpolation operators have to be chosen fairly carefully to avoid poor approximations to the problem at the coarse levels and ineffectual corrections propogated to the fine levels. The interpolation operator is defined naturally from the shape functions at the coarse levels. The projection operator is then defined to complement this choice (the operators should be adjoint).

The sawtooth cycle given in this section is the simplest multigrid algorithm. Developments include improving the residual at each level of the *projection*, known as a _v-cycle_, and cycles in which the residual is interpolated only part way through the hierarchy before being reprojected and subjected to another set of improvements (a _w-cycle_).

The Full Multigrid Algorithm (see Brandt) introduces a further level of complexity. Instead of simply casting the problem at a single level and projecting/improving the residual on a number of grids, the whole problem is defined for all the grids. In this way the initial fine-grid approximation is obtained by interpolating from the solution to the coarsest grid problem. The solution at each level is still obtained by projecting to the finest level and reducing the residual at each projection step. The result is some sort of "Loch Ness Monster" cycle.

One of the major problems in multigrid is knowing how best to represent material properties at different levels of grid coarseness in order to obtain the optimal convergence rate. This has a simple solution in the particle in cell finite element methods which we will discuss later.




\begin{equation*}
{\bf Gd} + {\bf G K}^{-1}{\bf G}^T {\bf p} = {\bf G K}^{-1}{\bf  f}
\end{equation*}

where the first term is zero due to the incompressibility condition. Then the equation system is in the form $\hat{\bf K}{\bf p} = \hat{\bf f}$, where $\hat{\bf K}$ is  now positive definite, and so a conjugate gradient method can be used:


    1.      $k = 0; {\bf p}_0 = {\bf 0}; {\bf r}_0 = \hat{\bf f}$  
    2.      while $({\bf r}_k \not= {\bf 0})$  
    3.      &emsp;  $ k = k + 1 $
    4.      &emsp;  if $(k=1)$  
    5.      &emsp;  &emsp; ${\bf s}_1 = {\bf r}_0$
    6.      &emsp;  else  
    7.      &emsp;  &emsp;  $\beta = ({\bf r} _ {k-1},{\bf r} _ {k-1})/({\bf r} _ {k-2},{\bf r} _ {k-2})$
    8.      &emsp;  &emsp;  ${\bf s} _ k = {\bf r} _ {k-1} + \beta {\bf s} _ {k-1}$
    9.      &emsp;  end
    10.     &emsp;  ${\bf w} = \hat{\bf K} {\bf s}$
    11.     &emsp;  $\alpha = ({\bf r} _ {k},{\bf r} _ {k})/({\bf s}_{k},{\bf w})$
    12.     &emsp;  ${\bf p} _ k = {\bf p} _ {k-1} + \alpha {\bf s} _ {k}$
    13.     &emsp;  ${\bf r} _ k = {\bf r} _ {k-1} - \alpha {\bf w}$
    14.     end
    15.     ${\bf d} = {\bf d}_k$

However, it is not possible to obtain $\hat{\bf K}$ or $\hat{\bf f}$ directly because the form of ${\bf K}^{-1}$ is not known - the reason for the use of an iterative method in the first place. In order to obtain the initial residual, therefore, perform the following operation,


1. $k = 0$; ${\bf p}_0 = {\bf 0}$ ; $\cancel{ {\bf r}_0 = \hat{\bf f} }$  

    - (1.a) &emsp;  ${\bf r}_0 = {\bf G K}^{-1} {\bf f}$:
    - (1.b) &emsp;  solve: ${\bf K d} = {\bf f}$ for $\bf d$
    - (1.c) &emsp;  set: ${\bf r}_0 = {\bf G d} = {\bf G K}^{-1} {\bf f}$


and to find the $\bf w$ vector:

   10. $ \cancel{ {\bf w} = \hat{\bf K} {\bf s} }$  
     - (10.a) &emsp; ${\bf w} = \hat{\bf G K}^{-1}{\bf G}^T {\bf s}$:
     - (10.b) &emsp;  solve ${\bf K d} = {\bf G}^T {\bf s}$ for $\bf d$
     - (10.c) &emsp;  set ${\bf w} = {\bf K d} = {\bf G K}^{-1}{\bf G}^T {\bf s}$





## Time

We have concentrated on the solution to equilibrium equations without really touching on the way time is evolved in elasticity and slow flow where the equations themselves are independent of time. In the mantle dynamics problem, the energy equation contains time derivatives which the equation of motion lacks so it is unsurprising that these equations require entirely different computational methods.

We almost always want to know the time-history of our simulations, so we generally solve this equation explicitly or semi-implicitly in time.

Variational methods are not generally applicable because the energy equation with its strong advection term does not follow an extremum of some functional. In this case even the weak forms of the equation are quite similar to finite difference equations.

<!-- MORE - perhaps take some of the treatise article here and expand it -->


<!-- %## Ideas on a Particle in Cell Finite Element Code}
%   
%   The extension of standard finite element
%   methods to include a basic Lagrangian Particle reference
%   frame.
%   
%   Adapting integration schemes.
%   
%   Problems for highly active flow regimes.
%
%   Discussion: as this is ongoing, research work with
%   potentially exciting commercial applications, it will be discussed but
%   not written out here !!
%   
%### Geological Examples from a PIC / FE method}
%
%   To wind down the course, we will watch some movies
%   of finite elements in action. -->
